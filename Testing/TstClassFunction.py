from Model.TradingViewData import TradingViewData
from Services.DBService import DBService
from Services.Helper.DataConverter import DataConverter


class NestedClass:
    def __init__(self, description):
        self.description = description


# Add a nested object
trading_data = TradingViewData("AAPL", "Broker1", [NestedClass("Strategy1")], 150.5, 149.0, 151.0, 148.5)

conv = DataConverter()

json_data = conv.ConvertClassToDict(trading_data)

# trading_data = {
#     "name": "John Doe",
#     "email": "johndoe@example.com",
#     "age": 30
# }
print(json_data)

db = DBService("TradingViewData")

db.add('Data',json_data)

print(json_data)
