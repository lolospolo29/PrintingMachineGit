from Interfaces import IStrategy, IBroker
from Models import Trade


class TradeManager:
    def __init__(self, name):
        self._name = name
        self._strategies = []
        self._brokers: list[IBroker] = []
        self._openTrades = []
        self._maxdrawdown = 2

    @property
    def strategies(self):
        return self._strategies

    @property
    def brokers(self):
        return self._brokers

    @property
    def openTrades(self):
        return self._openTrades

    def add_strategy(self, strategy: IStrategy):
        if strategy not in self._strategies:
            self._strategies.append(strategy)

    def add_broker(self, broker: IBroker):
        if broker not in self._brokers:
            self._brokers.append(broker)

    def add_trade(self, trade: Trade):
        if trade not in self._openTrades:
            self._openTrades.append(trade)

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

    def checkOpenTrades(self,asset):
        for trade in self._openTrades:
            if trade._status == "Open" and trade._asset == asset:
                return trade._groupId
        return False

