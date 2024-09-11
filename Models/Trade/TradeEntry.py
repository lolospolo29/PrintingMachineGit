class TradeEntry:
    def __init__(self, entryPrice, orderType, pendingUntilTime,status):
        self._entryPrice = entryPrice
        self._orderType = orderType
        self._pendingUntilTime = pendingUntilTime
        self._EntryId = None
