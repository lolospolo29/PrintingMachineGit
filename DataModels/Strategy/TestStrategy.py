from Interfaces.IStrategy import IStrategy


class TestStrategy(IStrategy):
    def __init__(self,name):
        self._name = name
        self._TimeWindow = "LondonOpen"

    def isInTime(self):
        pass

    def isStrategyValid(self):
        pass

    def getExit(self):
        pass

    def getEntry(self):
        pass
