class Trade:

    def __int__(self, id, strategy, broker, asset, status):
        self._id = id
        self._strategy = strategy #string
        self._broker = broker #string
        self._asset = asset
        self._currentRisk = None
        self._orders = None

    # @property
    # def exitPrice(self):
    #     return self._exitPrice
    #
    # @exitPrice.setter
    # def exitPrice(self, value):
    #     if value < 0:
    #         raise ValueError("Exit price cannot be negative.")
    #     self.exitPrice = value
