from Interfaces.ITrade import ITrade


class Trade(ITrade):

    def __int__(self, id, strategy, broker, assets, currentRisk, status, entryTime, entryPrice):
        self._id = id
        self._strategy = strategy
        self._broker = broker
        self._assets = assets
        self._currentRisk = currentRisk
        self._status = status
        self._entryTime = entryTime
        self._exitTime = 0
        self._entryPrice = entryPrice
        self._exitPrice = 0

    def getEntryPrice(self):
        pass

    def getExitPrice(self):
        pass

    def getExitTime(self):
        pass

    def getEntryTime(self):
        pass

    def getStatus(self):
        pass

    def getCurrentRisk(self):
        pass

    def getAsset(self):
        pass

    def getId(self):
        pass

    def getBroker(self):
        pass

    def getStrategy(self):
        pass



