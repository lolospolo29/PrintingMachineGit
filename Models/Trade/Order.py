class Order:
    def __init__(self,tradeEntry,tradeExit):
        self._tradeEntry = tradeEntry
        self._tradeExit = tradeExit
        self._status = "pending"
        self._timeEntry = None
        self._timeExit = None
        self._brokerTradeId = None
