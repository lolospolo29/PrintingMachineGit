from Models.TradingData import TradingData


class DataMapper:
    @staticmethod
    def MapToClass(data, name):
        # If _id is present, handle it as needed (e.g., ignore or use it)
        # For this example, we'll just ignore it
        if name == "tradingData":
            data = data.get("tradingData")
            return TradingData(
                    asset=data.get('asset'),
                    open=data.get('broker'),
                    close=data.get('close'),
                    high=data.get('high'),
                    low=data.get('low'),
                    time=data.get('time'),
                    timeFrame=data.get('timeFrame')
                )
