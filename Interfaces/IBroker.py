from abc import ABC, abstractmethod


class IBroker(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
