from Controller.SignalController import SignalControler
from Controller.TradingController import TradingController
from Models.BrokerModels.TestBroker import TestBroker
from Models.Mapper.DataMapper import DataMapper
from Models.StrategyModels.TestStrategy import TestStrategy
from Monitoring.Monitoring import Monitoring
from Services.DBService import DBService
from Services.Factory.DBFactory import DBFactory
from Services.Helper.DataHelper import DataHelper
from Services.Helper.SecretsManager import SecretsManager
from Services.RiskManager import RiskManager
from Services.TradeService import TradeService

# Mapper
dataMapper = DataMapper()

# Broker
tstBroker = TestBroker("tstBroker")

# Strategy
tstStrategy = TestStrategy("tstStrategy")

# Monitoring

monitoring = Monitoring()

# Factory

dbFactory = DBFactory()

# Helper
secretsManager = SecretsManager()

dataHelper = DataHelper()

# Services

riskManager = RiskManager(2, 1)

tradeService = TradeService()

# Controller

tradingController = TradingController(dataMapper,monitoring,dbFactory,tradeService)

signalController = SignalControler(monitoring,tradingController)
