class Trade:

    def __init__(self,brokerName,strategyName):
        self.status = None
        self.orders = []
        self.brokerName = brokerName
        self.strategyName = strategyName
        self.pnl = 0

    def to_dict(self):
        return {
            "Trade": {
                "status": self.status,
                "orders": self.orders,
                "brokerName": self.brokerName,
                "strategyName": self.strategyName,
                "pnl": self.pnl,
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
