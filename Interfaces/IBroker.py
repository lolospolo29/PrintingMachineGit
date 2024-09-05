from abc import ABC, abstractmethod


class IBroker(ABC):

    # Abstract method: must be implemented by subclasses
    @abstractmethod
    def executeMarketOrder(self):
        pass

    @abstractmethod
    def setLimitOrder(self):
        pass

    @abstractmethod
    def cancelTrade(self):
        pass

    @abstractmethod
    def getBalance(self):
        pass

    @abstractmethod
    def getFees(self):
        pass

    @abstractmethod
    def addAsset(self):
        pass

    @abstractmethod
    def getSupportedAssets(self):
        pass
