class Trade:

    def __init__(self, id, strategy, broker, asset, status,risk,currentRisk,orders):
        self.id = id
        self.strategy = strategy #string
        self.broker = broker #string
        self.asset = asset
        self.status = status
        self.risk = risk
        self.currentRisk = currentRisk
        self.orders = orders

    def to_dict(self):
        return {
            "Trade": {
                "id": self.id,
                "strategy": self.strategy,
                "broker": self.broker,
                "asset": self.asset,
                "status": self.status,
                "risk": self.risk,
                "currentRisk": self.currentRisk,
                "orders": self.orders,
            }
        }

    # @property
    # def exitPrice(self):
    #     return self._exitPrice
    #
    # @exitPrice.setter
    # def exitPrice(self, value):
    #     if value < 0:
    #         raise ValueError("Exit price cannot be negative.")
    #     self.exitPrice = value
