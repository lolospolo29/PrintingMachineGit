import json
from datetime import datetime

from Models.TradingViewData import TradingViewData


class DataMapper:
    @staticmethod
    def MapToClass(data, name):
        # If _id is present, handle it as needed (e.g., ignore or use it)
        # For this example, we'll just ignore it
        if name == "TradingViewData":
            data = data.get("tradingViewData")
            return TradingViewData(
                    ticker=data.get('ticker'),
                    broker=data.get('broker'),
                    strategy=data.get('strategy', []),  # Default to empty list if not present
                    close=data.get('close'),
                    open=data.get('open'),
                    high=data.get('high'),
                    low=data.get('low'),
                    time=data.get('time'),
                    smt=data.get('smt'),
                    tf=data.get('tf')
                )
