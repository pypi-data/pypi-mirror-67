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
from typing import Dict, Generic, List, Optional, TypeVar

T = TypeVar('T')


class Scheduler(Generic[T]):
    """A class which can wrap things like Datasets and Ops to make their behavior epoch-dependent.
    """
    def get_current_value(self, epoch: int) -> Optional[T]:
        """Fetch whichever of the `Scheduler`s elements is appropriate based on the current epoch.

        Args:
            epoch: The current epoch.

        Returns:
            The element from the Scheduler to be used at the given `epoch`. This value might be None.
        """
        raise NotImplementedError

    def get_all_values(self) -> List[Optional[T]]:
        """Get a list of all the possible values stored in the `Scheduler`.

        Returns:
            A list of all the values stored in the `Scheduler`. This may contain None values.
        """
        raise NotImplementedError


class RepeatScheduler(Scheduler[T]):
    """A scheduler which repeats a collection of entries one after another every epoch.

    One case where this class would be useful is if you want to perform one version of an Op on even epochs, and a
    different version on odd epochs. None values can be used to achieve an end result of skipping an Op every so often.

    ```python
    s = fe.schedule.RepeatScheduler(["a", "b", "c"])
    s.get_current_value(epoch=1)  # "a"
    s.get_current_value(epoch=2)  # "b"
    s.get_current_value(epoch=3)  # "c"
    s.get_current_value(epoch=4)  # "a"
    s.get_current_value(epoch=5)  # "b"
    ```

    Args:
        repeat_list: What elements to cycle between every epoch. Note that epochs start counting from 1. To have nothing
        happen for a particular epoch, None values may be used.

    Raises:
        AssertionError: If `repeat_list` is not a List.
    """
    def __init__(self, repeat_list: List[Optional[T]]) -> None:
        assert isinstance(repeat_list, List), "must provide a list as input of RepeatSchedule"
        self.repeat_list = repeat_list
        self.cycle_length = len(repeat_list)
        assert self.cycle_length > 1, "list length must be greater than 1"

    def get_current_value(self, epoch: int) -> Optional[T]:
        # epoch-1 since the training epoch is 1-indexed rather than 0-indexed.
        return self.repeat_list[(epoch - 1) % self.cycle_length]

    def get_all_values(self) -> List[Optional[T]]:
        return self.repeat_list


class EpochScheduler(Scheduler[T]):
    """A scheduler which selects entries based on a specified epoch mapping.

    This can be useful for making networks grow over time, or to use more challenging data augmentation as training
    progresses.

    ```python
    s = fe.schedule.EpochScheduler({1:"a", 3:"b", 4:None, 100: "c"})
    s.get_current_value(epoch=1)  # "a"
    s.get_current_value(epoch=2)  # "a"
    s.get_current_value(epoch=3)  # "b"
    s.get_current_value(epoch=4)  # None
    s.get_current_value(epoch=99)  # None
    s.get_current_value(epoch=100)  # "c"
    ```

    Args:
        epoch_dict: A mapping from epoch -> element. For epochs in between keys in the dictionary, the closest prior key
            will be used to determine which element to return. None values may be used to cause nothing to happen for a
            particular epoch.

    Raises:
        AssertionError: If the `epoch_dict` is of the wrong type, is missing information for the first epoch, or
            contains invalid keys.
    """
    def __init__(self, epoch_dict: Dict[int, T]) -> None:
        assert isinstance(epoch_dict, dict), "must provide dictionary as epoch_dict"
        self.epoch_dict = epoch_dict
        self.keys = sorted(self.epoch_dict)
        assert 1 in self.epoch_dict, "epoch 1 is missing in dictionary, use None if no op is needed"
        for key in self.keys:
            assert isinstance(key, int), "found non-integer key: {}".format(key)
            assert key >= 1, "found non-positive key: {}".format(key)

    def get_current_value(self, epoch: int) -> Optional[T]:
        if epoch in self.keys:
            value = self.epoch_dict[epoch]
        else:
            value = self.epoch_dict[self._get_last_key(epoch)]
        return value

    def get_all_values(self) -> List[Optional[T]]:
        return list(self.epoch_dict.values())

    def _get_last_key(self, epoch: int) -> int:
        """Find the nearest prior key to the given epoch.

        Args:
            epoch: The current target epoch.

        Returns:
            The largest epoch number <= the given `epoch` that is in the `epoch_dict`.
        """
        last_key = 1
        for key in self.keys:
            if key > epoch:
                break
            last_key = key
        return last_key
