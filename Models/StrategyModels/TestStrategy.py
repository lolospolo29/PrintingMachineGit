from Interfaces.IStrategy import IStrategy
from Services.Factory.RiskManagement.RegistryPattern.BrokerFactory import BrokerFactory
from Services.Factory.StrategyFactory import StrategyFactory


class TestStrategy(IStrategy):
    def __init__(self,name):
        self._name = name
        self._StrategyFactory = StrategyFactory()
        self._TimeWindow = "LondonOpen"
        self._BrokerFactory = BrokerFactory()

    def isInTime(self):
        pass

    def isStrategyValid(self):
        pass

    def getExit(self):
        pass

    def getEntry(self):
        pass
