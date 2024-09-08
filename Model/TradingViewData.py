class TradingViewData:
    def __init__(self, ticker, broker, strategy, close, open_price, high, low):
        self.ticker = ticker
        self.broker = broker
        self.strategy = strategy  # Eine Liste von Strategien
        self.close = close
        self.open = open_price
        self.high = high
        self.low = low

    def __repr__(self):
        return (f"TradingViewData(ticker={self.ticker}, broker={self.broker}, strategy={self.strategy}, "
                f"close={self.close}, open={self.open}, high={self.high}, low={self.low})")

# Erstellen des TradingViewData-Objekts
# data = jsonModel
# trading_view_data = TradingViewData(
#     ticker=data['ticker'],
#     broker=data['Broker'],
#     strategy=data['strategie'],  # Die Strategie bleibt eine Liste
#     close=data['close'],
#     open_price=data['open'],
#     high=data['high'],
#     low=data['low']
# )

# Ausgabe
# print(trading_view_data)
