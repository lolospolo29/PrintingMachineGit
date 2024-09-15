from Models.StrategyModels.TestStrategy import TestStrategy


class StrategyFactory:
    @staticmethod
    def returnStrategie(strategyName):
        if strategyName == "FVG":
            return TestStrategy("Name")
        return None
