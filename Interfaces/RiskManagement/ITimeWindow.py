from abc import ABC, abstractmethod


class ITimeWindow(ABC): # Entry / Exit Times
    @abstractmethod
    def getTimeWindow(self):
        pass
