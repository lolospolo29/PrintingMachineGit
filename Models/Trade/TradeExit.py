class TradeExit:
    def __init__(self, exitPrice, riskPercentage, stopLoss):
        self._exitPrice = exitPrice
        self._riskPercentage = riskPercentage
        self._stopLoss = stopLoss
        self._linkedEntryId = None
