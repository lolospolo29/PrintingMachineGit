from abc import ABC, abstractmethod


class IMartingale(ABC):
    @abstractmethod
    def getMartingaleModel(self):
        pass
    @abstractmethod
    def getPercentagesPerOrder(self):
        pass
