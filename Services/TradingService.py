from Models.AssetModels.Asset import Asset


class TradingService:
    def __init__(self, Monitoring, MongoDB, DataMapper):
        self._Monitoring = Monitoring
        self._MongoDB = MongoDB
        self._DataMapper = DataMapper
        self.assets = {}
        self.openTrades = {}

    def createAsset(self, name, strategyName, smtPairName):
        """
        Create a new asset and add it to the controller's asset list.
        """
        asset = Asset(name, strategyName, smtPairName)
        self.assets[name] = asset
        print(f"Asset '{name}' created and added to the controller.")
        return asset

    def addBrokerToAsset(self, asset_name, broker):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addBroker(broker)

    def addTimeframeToAsset(self, asset_name, timeframe):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addNewTimeFrame(timeframe)

    def addDataToAsset(self, asset_name, timeframe, tradingData):
        """
        Add a new timeframe to a specific asset.
        """
        if asset_name in self.assets:
            self.assets[asset_name].addNewData(timeframe, tradingData.open, tradingData.high, tradingData.low,
                                               tradingData.close, tradingData.time)

    def handleTradingViewSignal(self, jsonData):

        tradingData = self._DataMapper.mapDataToClass(jsonData, "TradingData")
        self.addDataToAsset(tradingData.asset, tradingData.timeFrame, tradingData)

    def findOpenTrades(self):
        query = self._DBHelper.buildQuery("Trade", "asset", "AAPL")  # Setzt den ticker-Wert in das Query

        tradeList = self._DBHelper.findDataInDBResultToList("mongodb", "Trades", "OpenTrades", query)

        tradeListCount = len(tradeList)

        if tradeListCount == 0:
            self._Monitoring.logInformation("No Trades Open")
        if not self.isTradeListEmpty(tradeList):
            Trades = []
            self._Monitoring.logInformation("Open Trades")
            for obj in tradeList:
                Trades.append(self._DBHelper.mapDataToClass(obj, "Trade"))

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
