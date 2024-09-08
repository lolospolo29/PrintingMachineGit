from abc import ABC, abstractmethod


class IBroker(ABC):
        # Abstract methods: must be implemented by subclasses
    @property
    @abstractmethod
    def name(self):
        pass
