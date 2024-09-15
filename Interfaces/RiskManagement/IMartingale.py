from abc import ABC, abstractmethod


class IMartingale(ABC):
    @abstractmethod
    def getMartingale(self):
        pass
