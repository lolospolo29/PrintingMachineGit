from Interfaces.IStrategy import IStrategy


class TestStrategy(IStrategy):
    def __init__(self,name):
        self._name = name

    def isStrategyValid(self):
        pass

    def getExit(self):
        pass

    def getEntry(self):
        pass
