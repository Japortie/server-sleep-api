from abc import ABCMeta, abstractmethod


class AbstractCheckPlugin(object):
    __metaclass__ = ABCMeta

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