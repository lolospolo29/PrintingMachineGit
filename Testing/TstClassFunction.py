from bson import ObjectId

from Model.TradingViewData import TradingViewData
from Services.DBService import DBService
from Services.Helper.DataHelper import DataHelper
from Services.Helper.SecretsManager import SecretsManager
import json


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

db.add('Data', json_data)

receivedData = db.find('Data')

for obj in receivedData:
    print(obj)
    # data = conv.convert_objectid_to_str(obj)
    # json_string = json.dumps(data)
    # tradingview = conv.ConvertJsonToClass(json_string)
    #implement mapper

# Function to convert ObjectId to string
