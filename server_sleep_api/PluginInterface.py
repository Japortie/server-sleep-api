from abc import ABC, abstractmethod
from enum import Enum


class AbstractCheckPlugin(ABC):

    """Initialize your Plugin Class"""
    @abstractmethod
    def __init__(self):
        pass

    """Check if the device should go to Sleep"""
    @abstractmethod
    def check(self):
        pass

    """Perform tasks that should be done before the device is set to sleep"""
    @abstractmethod
    def sleep(self):
        pass

    """Perform tasks that should be done after wake up"""
    @abstractmethod
    def wake(self):
        pass


class CheckReturn(Enum):
    SLEEP_READY = 1
    DONT_SLEEP = 2
    FORCE_SLEEP = 3
    UNKNOWN = 9