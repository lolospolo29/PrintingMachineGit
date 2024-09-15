from Models.BrokerModels.TestBroker import TestBroker


class StrategyFactory:
    @staticmethod
    def returnStrategie(brokername):
        if brokername == "Tst":
            return TestBroker("Tst")
        return None
