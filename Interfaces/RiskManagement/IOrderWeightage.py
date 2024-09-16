from abc import ABC, abstractmethod


class IOrderWeightage(ABC):
    @abstractmethod
    def getOrderWeightage(self):
        pass
