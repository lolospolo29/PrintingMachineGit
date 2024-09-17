from abc import ABC, abstractmethod


class ITimeWindow(ABC): # Entry / Exit Times
    @abstractmethod
    def getEntryWindow(self):
        pass
    @abstractmethod
    def getExitWindow(self):
        pass

