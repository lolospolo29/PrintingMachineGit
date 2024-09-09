from abc import ABC, abstractmethod


class IStrategy(ABC):

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def getEntry(self):
        pass

    @abstractmethod
    def getExit(self):
        pass

    @abstractmethod
    def isStrategyValid(self):
        pass
