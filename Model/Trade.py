class Trade:

    def __int__(self, id, strategy, broker, assets, currentRisk, status, entryTime, entryPrice):
        self._id = id
        self._strategy = strategy #string
        self._broker = broker #string
        self._assets = assets
        self._currentRisk = currentRisk
        self._status = status #Open / Closed / Pending
        self._entryTime = entryTime
        self._exitTime = 0
        self._entryPrice = entryPrice
        self._exitPrice = 0

    @property
    def exitPrice(self):
        return self._exitPrice

    @exitPrice.setter
    def exitPrice(self, value):
        if value < 0:
            raise ValueError("Exit price cannot be negative.")
        self._exitPrice = value


