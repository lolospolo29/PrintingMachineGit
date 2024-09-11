from abc import ABC, abstractmethod


class IStrategy(ABC):
    @abstractmethod
    def getEntry(self):
        pass

    @abstractmethod
    def getExit(self):
        pass

    @abstractmethod
    def isStrategyValid(self):
        pass
