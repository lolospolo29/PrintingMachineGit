from Controller.SignalController import SignalControler
from Controller.TradingController import TradingController
from Models.BrokerModels.TestBroker import TestBroker
from Models.DBModels.MongoDB import DBService
from Models.Mapper.DataMapper import DataMapper
from Models.StrategyModels.TestStrategy import TestStrategy
from Monitoring.Monitoring import Monitoring
from Services.Helper.SecretsManager import SecretsManager
from Services.RiskManager import RiskManager

# Mapper
dataMapper = DataMapper()

# Broker
tstBroker = TestBroker("tstBroker")

# Strategy
tstStrategy = TestStrategy("tstStrategy")

# Monitoring

monitoring = Monitoring()

# Helper

secretsManager = SecretsManager()

secretsMongo = secretsManager.get_secret("mongodb")


# Services

mongoDB = DBService("TradingData", secretsMongo)
riskManager = RiskManager(2, 1)

# Controller

tradingController = TradingController(monitoring,mongoDB,dataMapper)

signalController = SignalControler(monitoring,tradingController)
