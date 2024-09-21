class TradingController:
    def __init__(self, DataMapper, Monitoring, DBFactory,TradeService):
        self._DataMapper = DataMapper
        self._Monitoring = Monitoring
        self._DBFactory = DBFactory
        self._TradeService = TradeService

    def handleTradingViewSignal(self, jsonData):
        tradingViewData = self._DataMapper.MapToClass(jsonData, "TradingViewData")

        self.addDataToDB("mongodb", "TradingData", tradingViewData.ticker, tradingViewData.to_dict())

        query = {"ticker": "a"}  # Setzt den ticker-Wert in das Query

        OpenTradelist = self.findDataInDBResultToList("mongodb","Trade","OpenTrades",query)

        if len(OpenTradelist) == 0:
            self._Monitoring.logInformation(tradingViewData.ticker," : No Trades Open")

    def addDataToDB(self, dbType, dbName, tableName, data):
        db = self._DBFactory.returnClass(dbType, dbName)
        self._Monitoring.logInformation((tableName, ": DB added New Data"))
        db.add(tableName, data)

    def findDataInDBResultToList(self, dbType, dbName, tableName, query):
        db = self._DBFactory.returnClass(dbType, dbName)
        return db.find(tableName, query)

    def handleExit(self):
        return None

    def handleEntry(self):
        return None

    def resetDB(self):
        return None
