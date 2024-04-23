from abc import ABC, abstractmethod


class State(ABC):
    '''
    Abstract interface for the State class.
    Uses the ABC library to force implementation of all methods.
    '''
    @abstractmethod
    def onhook(self):
        pass

    @abstractmethod
    def offhook(self):
        pass

    @abstractmethod
    def call(self, other_phone):
        pass

    @abstractmethod
    def receive_call(self, other_phone):
        pass

    @abstractmethod
    def conference(self, other_phone):
        pass

    @abstractmethod
    def transfer(self, other_phone):
        pass

    @abstractmethod
    def get_status(self):
        pass
