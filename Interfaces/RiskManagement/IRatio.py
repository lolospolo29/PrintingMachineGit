from abc import ABC, abstractmethod


class IRatio(ABC): # Fixed or Variable
    @abstractmethod
    def getRatio(self):
        pass
