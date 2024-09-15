from abc import ABC, abstractmethod


class ITakeProfitStrategy(ABC): # wo der Stop-Loss liegt
    @abstractmethod
    def getTakeProfitStrategy(self):
        pass
