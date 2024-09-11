from Models.Mapper.DataMapper import DataMapper
from Models.TradingViewData import TradingViewData
from Services.DBService import DBService
from Services.Helper.DataHelper import DataHelper
from Services.Helper.SecretsManager import SecretsManager


class NestedClass:
    def __init__(self, description):
        self.description = description


# Add a nested object
trading_data = TradingViewData("AAPL", "Broker1", [NestedClass("Strategy1")], 150.5, 149.0, 151.0, 148.5)

conv = DataHelper()

json_data = conv.ConvertClassToDict(trading_data)

# trading_data = {
#     "name": "John Doe",
#     "email": "johndoe@example.com",
#     "age": 30
# }
secretsM = SecretsManager()

secretsMongo = secretsM.get_secret("mongodb")

db = DBService("TradingViewData", secretsMongo)

db.add("Data", json_data)

receivedData = db.find("Data")

mapper = DataMapper()

for obj in receivedData:
    mappedClass = mapper.MapToClass(obj,"TradingViewData")
    print(obj)
    print(mappedClass)

    # data = conv.convert_objectid_to_str(obj)
    # json_string = json.dumps(data)
    # tradingview = conv.ConvertJsonToClass(json_string)
    #implement mapperr

# Function to convert ObjectId to string
