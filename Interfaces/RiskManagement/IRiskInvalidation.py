from abc import ABC, abstractmethod


class IRiskInvalidation(ABC):
    @abstractmethod
    def getRiskInvalidation(self):
        pass
