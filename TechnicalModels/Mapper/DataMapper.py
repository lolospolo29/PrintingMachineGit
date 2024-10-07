import datetime

from Models.Trade.Trade import Trade
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
        if name == "Trade":
            # Mappe die Daten auf das Trade-Objekt
            data = data.get("Trade")

            # Handle asset
            asset_value = data.get('asset')
            asset_value = asset_value.strip("'") if asset_value else None  # Entferne einfache Anführungszeichen

            # Handle strategyName
            strategy_name = data.get('strategyName', '')

            # Initialisiere das Trade-Objekt
            trade = Trade(asset=asset_value, strategyName=strategy_name)

            # Mappe den Status und PnL
            trade.status = data.get('status', None)
            trade.pnl = data.get('pnl', 0)

            # Verarbeite die Order-Liste, falls vorhanden
            trade.orders = data.get('orders', [])

            return trade
        else:
            raise ValueError("Unsupported mapping for: " + name)
