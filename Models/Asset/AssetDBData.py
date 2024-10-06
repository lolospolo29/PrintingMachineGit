class AssetDBData:
    def __init__(self, open, high, low, close, time, timeStamp, timeFrame):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.time = time
        self.timeStamp = timeStamp
        self.timeFrame = timeFrame

    def to_dict(self):
        return {
            'open': self.open,
            'high': self.high,
            'low': self.low,
            'close': self.close,
            'time': self.time,
            'timeStamp': self.timeStamp,
            'timeFrame': self.timeFrame
        }
