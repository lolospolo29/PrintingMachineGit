from Controller.SignalController import SignalControler
from Controller.TradingController import TradingController
from Models.BrokerModels.TestBroker import TestBroker
from Models.Mapper.DataMapper import DataMapper
from Models.StrategyModels.TestStrategy import TestStrategy
from Monitoring.Monitoring import Monitoring
from Services.Factory.DBFactory import DBFactory
from Services.Factory.StrategyFactory import StrategyFactory
from Services.DBService import DBHelper
from Services.Helper.DataHelper import DataHelper
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

# Factory

dbFactory = DBFactory()

strategyFactory = StrategyFactory()

# Helper
secretsManager = SecretsManager()

dataHelper = DataHelper()

dbHelper = DBHelper(dbFactory,monitoring,dataMapper)

# Services

riskManager = RiskManager(2, 1)

# Controller

tradingController = TradingController(monitoring,dbHelper,strategyFactory)

signalController = SignalControler(monitoring,tradingController)
