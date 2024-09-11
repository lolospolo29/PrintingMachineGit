class TradingViewData:
    def __init__(self, ticker, broker, strategy, close, open, high, low,time,smt,tf):
        self.ticker = ticker
        self.broker = broker
        self.strategy = strategy  # Eine Liste von Strategien
        self.close = close
        self.open = open
        self.high = high
        self.low = low
        self.time = time
        self.smt = smt
        self.tf = tf

    def __repr__(self):
        return (f"TradingViewData(ticker={self.ticker}, broker={self.broker}, strategy={self.strategy}, "
                f"close={self.close}, open={self.open}, high={self.high}, low={self.low})")
