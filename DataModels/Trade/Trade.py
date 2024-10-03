class Trade:

    def __init__(self,asset,strategyName):
        self.status = None
        self.asset = asset
        self.orders = []
        self.strategyName = strategyName
        self.pnl = 0

    # @property
    # def exitPrice(self):
    #     return self._exitPrice
    #
    # @exitPrice.setter
    # def exitPrice(self, value):
    #     if value < 0:
    #         raise ValueError("Exit price cannot be negative.")
    #     self.exitPrice = value
