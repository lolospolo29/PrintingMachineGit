class TradingController:
    def __init__(self, Monitoring, MongoDB, DataMapper):
        self._Monitoring = Monitoring
        self._MongoDB = MongoDB
        self._DataMapper = DataMapper

    def handleTradingViewSignal(self, jsonData):

        tradingViewData = self._DBHelper.mapDataToClass(jsonData, "TradingData")

        self._DBHelper.addDataToDB("mongodb", "TradingData", tradingViewData.ticker, tradingViewData.to_dict())

        query = self._DBHelper.buildQuery("Trade", "asset", "AAPL")  # Setzt den ticker-Wert in das Query

        TradeList = self._DBHelper.findDataInDBResultToList("mongodb", "Trades", "OpenTrades", query)

        if self.isTradeListEmpty(TradeList):
            self._Monitoring.logInformation((tradingViewData.ticker, " : No Trades Open"))
        if not self.isTradeListEmpty(TradeList):
            Trades = []
            self._Monitoring.logInformation((tradingViewData.ticker, len(TradeList)))
            for obj in TradeList:
                Trades.append(self._DBHelper.mapDataToClass(obj, "Trade"))
            self.handleTrades(Trades)

    @staticmethod
    def isTradeListEmpty(OpenTradeList):
        if len(OpenTradeList) == 0:
            return True
        if len(OpenTradeList) > 0:
            return False

    def handleTrades(self, Trades):
        Trades = self.removeClosedTrades(Trades)

        for trade in Trades:
            strategy = self._StrategyFactory.returnClass(trade.strategy)

    def removeClosedTrades(self, Trades):
        OpenTrades = []
        for trade in Trades:
            if trade.status == "Open":
                OpenTrades.append(trade)
            if trade.status == "Closed":
                query = self._DBHelper.buildQuery("Trade", "id", trade.id)
                self._DBHelper.deleteDataFromData("mongodb", "Trades", "OpenTrades", query)

        return OpenTrades

    def handleExit(self):
        return None

    def handleEntry(self):
        return None
