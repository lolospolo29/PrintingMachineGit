import datetime
from collections import deque

import pytz as pytz

utc_minus_4 = pytz.timezone('Etc/GMT+4')


class AssetData:
    def __init__(self, timeFrame):
        self.open = deque(maxlen=90)
        self.high = deque(maxlen=90)
        self.low = deque(maxlen=90)
        self.close = deque(maxlen=90)
        self.time = deque(maxlen=90)
        self.timesStamp = datetime.datetime.now(utc_minus_4).strftime('%d %B')
        self.timeFrame = timeFrame

    def addData(self, openPrice, highPrice, lowPrice, closePrice, time):
        """
        Add new OHLC data to the deque.
        """
        self.open.append(openPrice)
        self.high.append(highPrice)
        self.low.append(lowPrice)
        self.close.append(closePrice)
        self.time.append(time)
