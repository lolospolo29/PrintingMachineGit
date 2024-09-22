from Models.Mapper.DataMapper import DataMapper
from Models.TradingViewData import TradingViewData
from Monitoring.Monitoring import Monitoring
from Models.DBModels.MongoDB import DBService
from Services.Helper.SecretsManager import SecretsManager


class NestedClass:
    def __init__(self, description):
        self.description = description


# Add a nested object
trading_data = TradingViewData("BTC", "Broker1", "a", 150.5, 149.0, 151.0, 148.5, 13, "no", 4)

json_data = trading_data.to_dict()

secretsM = SecretsManager()

secretsMongo = secretsM.get_secret("mongodb")

monitoring = Monitoring()

db = DBService("TradingData", secretsMongo)

# db.add("Data", json_data)

receivedData = db.find("BTCUSDT.P", query=None)

mapper = DataMapper()

for obj in receivedData:
    mappedClass = mapper.MapToClass(obj, "TradingViewData")


# print(mappedClass.ticker)

# data = conv.convert_objectid_to_str(obj)
# json_string = json.dumps(data)
# tradingview = conv.ConvertJsonToClass(json_string)
# implement mapperr
def buildQuery(className, attribute, value):
    return {f"{className}.{attribute}": value}


query = buildQuery("OpenTrades", "asset", "AAPL")

db = DBService("Trade", secretsMongo)

receivedData = db.find("OpenTrades", query)

print(len(receivedData))
# Function to convert ObjectId to string
