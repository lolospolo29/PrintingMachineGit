import datetime

import pytz

from Models.Asset.Asset import Asset

berlin_tz = pytz.timezone('Europe/Berlin')
current_time = datetime.datetime.now(berlin_tz)
date_60_days_ago = current_time - datetime.timedelta(days=60)
iso_date_60_days_ago = date_60_days_ago.isoformat()
iso_current_time = current_time.isoformat()


class TradingService:
    def __init__(self, Monitoring, MongoDBData, MongoDBTrades, DataMapper):
        self._Monitoring = Monitoring
        self._MongoDBData = MongoDBData
        self._MongoDBTrades = MongoDBTrades
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

        tradingData = self._DataMapper.MapToClass(jsonData, "tradingData")
        self.addDataToAsset(tradingData.asset, tradingData.timeFrame, tradingData)
        if tradingData.time.strftime("%H:%M") == "00:00":
            self.dailyDataArchive()

    def RecentDataRetriever(self):
        pass

    def dailyDataArchive(self):
        for key, asset in self.assets.items():
            timeFrames = asset.getAllTimeFrames()
            for timeFrame in timeFrames:
                assetTimeFrameData = asset.timeFrameDataStorageDict(timeFrame)
                self._MongoDBData.add(asset.name, assetTimeFrameData)
            asset.clearAllData()
            self._MongoDBData.deleteOldDocuments(asset.name, 'timeStamp', iso_date_60_days_ago)
        #  self._MongoDBData.getDataWithinDateRange(asset.name, 'timeStamp',iso_current_time, iso_date_60_days_ago)

    def findOpenTrades(self):
        query = self._DBHelper.buildQuery("Trade", "asset", "AAPL")  # Setzt den ticker-Wert in das Query

        tradeList = self._DBHelper.findDataInDBResultToList("mongodb", "Trades", "OpenTrades", query)

        tradeListCount = len(tradeList)

        if tradeListCount == 0:
            self._Monitoring.logInformation("No Trades Open")
        if not tradeListCount < 0:
            Trades = []
            self._Monitoring.logInformation("Open Trades")
            for obj in tradeList:
                Trades.append(self._DBHelper.mapDataToClass(obj, "Trade"))

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
