from abc import ABC, abstractmethod


class IEntryStrategy(ABC):  # Drill Fill CE
    @abstractmethod
    def getEntryList(self):  # return list of possible entrys
        pass

    @abstractmethod
    def getEntry(self):  # get new Entry
        pass
