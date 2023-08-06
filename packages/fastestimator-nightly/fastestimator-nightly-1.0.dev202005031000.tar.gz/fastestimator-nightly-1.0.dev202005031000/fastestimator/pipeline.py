# Copyright 2019 The FastEstimator Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
import os
import time
import warnings
from copy import deepcopy
from functools import lru_cache
from typing import Any, Dict, List, MutableMapping, Optional, Set, TypeVar, Union

import numpy as np
import tensorflow as tf
from fastestimator.dataset.batch_dataset import BatchDataset
from fastestimator.dataset.op_dataset import OpDataset
from fastestimator.op.numpyop.numpyop import NumpyOp, forward_numpyop
from fastestimator.op.op import get_current_ops
from fastestimator.schedule.schedule import EpochScheduler, RepeatScheduler, Scheduler
from fastestimator.util.util import lcms, pad_batch, to_list
from torch.utils.data import DataLoader, Dataset, RandomSampler
from torch.utils.data.dataloader import default_collate

DataSource = TypeVar('DataSource', Dataset, DataLoader, tf.data.Dataset)


class Pipeline:
    """A data pipeline class that takes care of data pre-processing.

    Args:
        train_data: The training data, or None if no training data is available.
        eval_data: The evaluation data, or None if no evaluation data is available.
        test_data: The testing data, or None if no evaluation data is available.
        batch_size: The batch size to be used by the pipeline. NOTE: This argument is only applicable when using a
            FastEstimator Dataset.
        ops: NumpyOps to be used for pre-processing. NOTE: This argument is only applicable when using a FastEstimator
            Dataset.
        num_process: Number of CPU threads to use for data pre-processing. NOTE: This argument is only applicable when
            using a FastEstimator Dataset. None will default to the system CPU count. Multiprocessing can be disabled by
            passing 0 here, which can be useful for debugging.
        drop_last: Whether to drop the last batch if the last batch is incomplete.
        pad_value: The padding value if batch padding is needed. None indicates that no padding is needed. NOTE: This
            argument is only applicable when using a FastEstimator Dataset.
    """
    ops: List[Union[NumpyOp, Scheduler[NumpyOp]]]

    def __init__(self,
                 train_data: Union[None, DataSource, Scheduler[DataSource]] = None,
                 eval_data: Union[None, DataSource, Scheduler[DataSource]] = None,
                 test_data: Union[None, DataSource, Scheduler[DataSource]] = None,
                 batch_size: Union[None, int, Scheduler[int]] = None,
                 ops: Union[None, NumpyOp, Scheduler[NumpyOp], List[Union[NumpyOp, Scheduler[NumpyOp]]]] = None,
                 num_process: Optional[int] = None,
                 drop_last: bool = False,
                 pad_value: Optional[Union[int, float]] = None):
        self.data = {x: y for (x, y) in zip(["train", "eval", "test"], [train_data, eval_data, test_data]) if y}
        self.batch_size = batch_size
        self.ops = to_list(ops)
        self.num_process = num_process if num_process is not None else os.cpu_count() if os.name != 'nt' else 0
        self.drop_last = drop_last
        self.pad_value = pad_value
        self._verify_inputs(**{k: v for k, v in locals().items() if k != 'self'})

    def _verify_inputs(self, **kwargs) -> None:
        """A helper method to ensure that the Pipeline inputs are valid.

        Args:
            **kwargs: A collection of variable / value pairs to validate.

        Raises:
            AssertionError: If `batch_size`, `ops`, or `num_process` were specified in the absence of a FastEstimator
                Dataset.
        """
        fe_dataset = False
        for mode, dataset in self.data.items():
            if isinstance(dataset, Scheduler):
                for ds in dataset.get_all_values():
                    fe_dataset = self._verify_dataset(mode, ds, **kwargs) or fe_dataset
            else:
                fe_dataset = self._verify_dataset(mode, dataset, **kwargs) or fe_dataset
        if not fe_dataset:
            assert kwargs['batch_size'] is None, "Pipeline only supports batch_size with built-in (FE) datasets"
            assert kwargs['ops'] is None, "Pipeline only supports ops with built-in (FE) datasets"
            assert kwargs['num_process'] is None, "Pipeline only support num_process with built-in (FE) datasets"

    def _verify_dataset(self, mode: str, dataset: DataSource, **kwargs) -> bool:
        """A helper function to ensure that all of a dataset's arguments are correct.

        Args:
            mode: The mode for which to verify the dataset. One of 'train', 'eval', or 'test'.
            dataset: The dataset to validate against.
            **kwargs: A selection of variables and their values which must be validated.

        Returns:
            True iff the `dataset` is a PyTorch Dataset (as opposed to a DataLoader or tf.data.Dataset).

        Raises:
            AssertionError: If the `kwargs` are found to be invalid based on the given `dataset`.
            ValueError: If the `dataset` is of an unknown type.
        """
        if isinstance(dataset, Dataset):
            # batch_size check
            assert isinstance(self.batch_size, (Scheduler, int, type(None))), \
                "unsupported batch_size format: {}".format(self.batch_size)
            if isinstance(self.batch_size, Scheduler):
                for batch_size in self.batch_size.get_all_values():
                    assert isinstance(batch_size, (int, type(None))), \
                        "unsupported batch_size format: {}".format(self.batch_size)
            # ops check
            for op in self.ops:
                if isinstance(op, Scheduler):
                    for epoch_op in op.get_all_values():
                        assert isinstance(epoch_op, (type(None), NumpyOp)), \
                            "unsupported op format, must provide NumpyOp in Pipeline"
                else:
                    assert isinstance(op, NumpyOp), "unsupported op format, must provide NumpyOp in Pipeline"
            # num_process check
            assert isinstance(self.num_process, int), "number of processes must be an integer"
            return True
        elif isinstance(dataset, (DataLoader, tf.data.Dataset)):
            if kwargs['batch_size'] is not None:
                warnings.warn("batch_size will only be used for built-in dataset")
            if kwargs['ops'] is not None:
                warnings.warn("ops will only be used for built-in dataset")
            if kwargs['num_process'] is not None:
                warnings.warn("num_process will only be used for built-in dataset")
            return False
        else:
            raise ValueError("Unsupported dataset type for {}".format(mode))

    def get_modes(self) -> Set[str]:
        """Get the modes for which the Pipeline has data.

        Returns:
            The modes for which the Pipeline has data.
        """
        return set(self.data.keys())

    def benchmark(self, mode: str = "train", epoch: int = 1, num_steps: int = 1000, log_interval: int = 100) -> None:
        """Benchmark the pipeline processing speed.

        Args:
            mode: The execution mode to benchmark. This can be 'train', 'eval' or 'test'.
            epoch: The epoch index to benchmark. Note that epoch indices are 1-indexed.
            num_steps: The maximum number of steps over which to perform the benchmark.
            log_interval: The logging interval.
        """
        loader = self.get_loader(mode=mode, epoch=epoch)
        if isinstance(loader, tf.data.Dataset):
            loader = loader.take(num_steps)
        start = time.perf_counter()
        for idx, _ in enumerate(loader, start=1):
            if idx % log_interval == 0:
                duration = time.perf_counter() - start
                iters_per_sec = log_interval / duration
                print("FastEstimator: Step: {}, Epoch: {}, Steps/sec: {}".format(idx, epoch, iters_per_sec))
                start = time.perf_counter()
            if idx == num_steps:
                break

    def transform(self, data: Dict[str, Any], mode: str, epoch: int = 1) -> Dict[str, Any]:
        """Apply all pipeline operations on a given data instance for the specified `mode` and `epoch`.

        Args:
            data: Input data in dictionary format.
            mode: The execution mode in which to run. This can be "train", "eval", "test" or "infer".
            epoch: The epoch index to run. Note that epoch indices are 1-indexed.

        Returns:
            The transformed data.
        """
        data = deepcopy(data)
        ops = get_current_ops(self.ops, mode, epoch)
        forward_numpyop(ops, data, mode)
        for key, value in data.items():
            data[key] = np.expand_dims(value, 0)
        return data

    def get_results(self, mode: str = "train", epoch: int = 1, num_steps: int = 1,
                    shuffle: bool = False) -> Union[List[Dict[str, Any]], Dict[str, Any]]:
        """Get sample Pipeline outputs.

        Args:
            mode: The execution mode in which to run. This can be "train", "eval", or "test".
            epoch: The epoch index to run. Note that epoch indices are 1-indexed.
            num_steps: Number of steps (batches) to get.
            shuffle: Whether to use shuffling.

        Returns:
            A list of batches of Pipeline outputs.
        """
        results = []
        loader = self.get_loader(mode=mode, epoch=epoch, shuffle=shuffle)
        if isinstance(loader, tf.data.Dataset):
            loader = loader.take(num_steps)
        for idx, batch in enumerate(loader):
            if idx == num_steps:
                break
            results.append(batch)
        if len(results) == 1:
            results = results[0]
        return results

    def get_loader(self, mode: str, epoch: int = 1,
                   shuffle: Optional[bool] = None) -> Union[DataLoader, tf.data.Dataset]:
        """Get a data loader from the Pipeline for a given `mode` and `epoch`.

        Args:
            mode: The execution mode for the loader. This can be 'train', 'eval' or 'test'.
            epoch: The epoch index for the loader. Note that epoch indices are 1-indexed.
            shuffle: Whether to shuffle the data. If None, the value for shuffle is based on mode. NOTE: This argument
                is only used with FastEstimator Datasets.

        Returns:
            A data loader for the given `mode` and `epoch`.
        """
        data = self.data[mode]
        if isinstance(data, Scheduler):
            data = data.get_current_value(epoch)
        if isinstance(data, Dataset):
            # batch size
            batch_size = self.batch_size
            if isinstance(batch_size, Scheduler):
                batch_size = batch_size.get_current_value(epoch)
            # batch dataset
            if isinstance(data, BatchDataset):
                assert batch_size is None, "batch_size must be None when using BatchDataset"
                data.pad_value = self.pad_value
            else:
                assert batch_size is not None, "batch_size should not be None"
            # shuffle
            if shuffle is None:
                shuffle = mode == "train"
            # collate_fn
            if self.pad_value is None or isinstance(data, BatchDataset):
                collate_fn = None
            else:
                collate_fn = self._pad_batch_collate
            op_dataset = OpDataset(data, get_current_ops(self.ops, mode, epoch), mode)
            data = DataLoader(op_dataset,
                              batch_size=batch_size,
                              shuffle=False if isinstance(data, BatchDataset) else shuffle,
                              sampler=RandomSampler(op_dataset) if isinstance(data, BatchDataset) and shuffle else None,
                              num_workers=self.num_process,
                              drop_last=self.drop_last,
                              worker_init_fn=lambda _: np.random.seed(),
                              collate_fn=collate_fn)
        return data

    def _pad_batch_collate(self, batch: List[MutableMapping[str, Any]]) -> Dict[str, Any]:
        """A collate function which pads a batch of data.

        Args:
            batch: The data to be batched and collated.

        Returns:
            A padded and collated batch of data.
        """
        pad_batch(batch, self.pad_value)
        return default_collate(batch)

    def get_signature_epochs(self, total_epochs: int) -> Set[int]:
        """Find the epochs on which the behavior of the Pipeline changes (due to Schedulers).

        Args:
            total_epochs: The maximum epoch number to consider when searching for signature epochs.

        Returns:
            The epoch indices on which the behavior of the Pipeline changes.
        """
        signature_epochs = {1}
        epoch_keys = {1}
        repeat_cycles = {1}
        for x in self.ops + list(self.data.values()) + [self.batch_size]:
            if isinstance(x, EpochScheduler):
                epoch_keys.update(x.epoch_dict.keys())
            elif isinstance(x, RepeatScheduler):
                repeat_cycles.add(x.cycle_length)
        least_common_cycle = lcms(*repeat_cycles)
        epoch_keys = sorted(epoch_keys)
        for idx, epoch in enumerate(epoch_keys):
            if idx + 1 < len(epoch_keys):
                signature_epochs.update(range(epoch, epoch + min(epoch_keys[idx + 1] - epoch, least_common_cycle)))
            else:
                signature_epochs.update(range(epoch, epoch + least_common_cycle))
        signature_epochs = set(epoch for epoch in signature_epochs if epoch <= total_epochs)
        return signature_epochs

    @lru_cache(maxsize=None, typed=True)
    def get_all_output_keys(self, mode: str, total_epochs: int) -> Set[str]:
        """Get the pipeline output keys for a given `mode`.

        Args:
            mode: The execution mode to be considered. This can be "train", "eval", "test", or "infer".
            total_epochs: The maximum number of epochs to consider when searching for output keys.

        Returns:
            All of the output keys which the pipeline will generate for the given `mode`.

        Raises:
            AssertionError: If the Pipeline contains improperly formatted data.
        """
        output_keys = set()
        for epoch in self.get_signature_epochs(total_epochs):
            loader = self.get_loader(mode=mode, epoch=epoch)
            if isinstance(loader, DataLoader):
                if isinstance(loader.dataset, OpDataset) and not isinstance(loader.dataset.dataset, BatchDataset):
                    data = loader.dataset.dataset[0]
                    for op in loader.dataset.ops:
                        output_keys.update(op.outputs)
                else:
                    data = loader.dataset[0]
            else:
                data = next(iter(loader))
            assert isinstance(data, dict), "please make sure data output format is dictionary"
            output_keys.update(data.keys())
        return output_keys
