from Models.AssetModels.Data import Data


class Asset:
    def __init__(self, name, strategyName, smtPairName):
        self.name = name
        self.strategyName = strategyName
        self.smtPairName = smtPairName
        self.brokerNameList = []
        self.dataStorage = []

    def addNewTimeFrame(self, timeframe):
        self.dataStorage.append(Data(timeframe))

    def addNewBroker(self, brokerName):
        self.brokerNameList.append(brokerName)

    def addNewData(self, timeFrame):
        for data in self.dataStorage:
            if data.timeFrame == timeFrame:
                data.open.append()
