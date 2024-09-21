from Interfaces import IStrategy, IBroker
from Models import Trade


class TradeService:
    def __init__(self):
        self._strategies = []
        self._brokers: list[IBroker] = []

    @property
    def strategies(self):
        return self._strategies

    @property
    def brokers(self):
        return self._brokers

    def addStrategy(self, strategy: IStrategy):
        if strategy not in self._strategies:
            self._strategies.append(strategy)

    def addBroker(self, broker: IBroker):
        if broker not in self._brokers:
            self._brokers.append(broker)

    def isBrokerNew(self, brokerName):
        for broker in self._brokers:
            if broker.name == brokerName:
                return True
        return False

    def isStrategyNew(self, strategyName):
        for strategy in self._strategies:
            if strategy.name == strategyName:
                return True
        return False
