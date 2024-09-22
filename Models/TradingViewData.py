class TradingViewData:
    def __init__(self, ticker, broker, strategy, close, open, high, low, time, smt, tf):
        self.ticker = ticker
        self.broker = broker
        self.strategy = strategy
        self.close = close
        self.open = open
        self.high = high
        self.low = low
        self.time = time
        self.smt = smt
        self.tf = tf

    def to_dict(self):
        return {
            "TradingData": {
                "ticker": self.ticker,
                "broker": self.broker,
                "close": self.close,
                "open": self.open,
                "high": self.high,
                "low": self.low,
                "tf": self.tf,
                "smt": self.smt,
                "strategy": self.strategy,
                "time": self.time,
            }
        }
