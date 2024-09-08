from abc import ABC, abstractmethod
from datetime import datetime


class ITrade(ABC):

    @property
    def entryPrice(self):
        return self._entryPrice

    @entryPrice.setter
    def entryPrice(self, value):
        if value < 0:
            raise ValueError("Entry price cannot be negative.")
        self._entryPrice = value

    @property
    def exitPrice(self):
        return self._exitPrice

    @exitPrice.setter
    def exitPrice(self, value):
        if value < 0:
            raise ValueError("Exit price cannot be negative.")
        self._exitPrice = value
