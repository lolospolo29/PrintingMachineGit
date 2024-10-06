import datetime


from Models.TradingData import TradingData


class DataMapper:
    @staticmethod
    def MapToClass(data, name):
        # If _id is present, handle it as needed (e.g., ignore or use it)
        # For this example, we'll just ignore it

        if name == "tradingData":
            data = data.get("tradingData")

            # Handle asset
            asset_value = data.get('asset')
            asset_value = asset_value.strip("'") if asset_value else None  # Remove single quotes from asset

            timeFrame = data.get('timeFrame')
            timeFrame = timeFrame.strip("'") if asset_value else None  # Remove single quotes from asset

            # Handle time
            current_time = datetime.datetime.now().strftime("%H:%M")

            return TradingData(
                    asset=asset_value,
                    open=data.get('open'),
                    close=data.get('close'),
                    high=data.get('high'),
                    low=data.get('low'),
                    time=current_time,  # Use the formatted time
                    timeFrame=timeFrame
                    )
