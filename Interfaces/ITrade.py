from abc import ABC, abstractmethod


class ITrade(ABC):

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def getStrategy(self):
        pass

    @abstractmethod
    def getBroker(self):
        pass

    @abstractmethod
    def getId(self):
        pass

    @abstractmethod
    def getAsset(self):
        pass

    @abstractmethod
    def getCurrentRisk(self):
        pass

    @abstractmethod
    def getStatus(self):
        pass

    @abstractmethod
    def getEntryTime(self):
        pass

    @abstractmethod
    def getExitTime(self):
        pass

    @abstractmethod
    def getEntryPrice(self):
        pass

    @abstractmethod
    def getExitPrice(self):
        pass
