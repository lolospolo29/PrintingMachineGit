from Interfaces.IFactory import IFactory
from Models.StrategyModels.TestStrategy import TestStrategy


class StrategyFactory(IFactory):
    def returnClass(self,name):
        if name == "TestStrategy":
            return TestStrategy(name)
