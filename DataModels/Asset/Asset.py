from Models.AssetModels.AssetData import AssetData


class Asset:
    def __init__(self, name, strategyName, smtPairName):
        self.name = name
        self.strategyName = strategyName
        self.smtPairName = smtPairName
        self.brokerNameList = []
        self.dataStorage = []

    def addNewTimeFrame(self, timeframe):
        self.dataStorage.append(AssetData(timeframe))

    def addNewBroker(self, brokerName):
        self.brokerNameList.append(brokerName)

    def addNewData(self, timeFrame, open,high,low,close,time):
        for assetData in self.dataStorage:
            if assetData.timeFrame == timeFrame:
                assetData.addData(open, high, low, close, time)
                break

    def getHistoricalData(self, timeframe, numberOfDataPoints):
        """
        Fetch the last 'number_of_data_points' for the given timeframe.
        This is useful for retrieving historical data for analysis.
        """
        for assetData in self.dataStorage:
            if assetData.timeFrame == timeframe:
                # Ensure we don't request more data than we have
                available_data_points = min(len(assetData.open), numberOfDataPoints)

                historical_data = {
                    'open': list(assetData.open)[-available_data_points:],
                    'high': list(assetData.high)[-available_data_points:],
                    'low': list(assetData.low)[-available_data_points:],
                    'close': list(assetData.close)[-available_data_points:],
                    'time': list(assetData.time)[-available_data_points:]
                }
                return historical_data
