class SignalControler:
    def __init__(self, Monitoring,TradingController):
        self._Monitoring = Monitoring
        self._TradingController = TradingController

    def orderSignal(self, jsonData):

        if "TradingData" in jsonData:
            self._TradingController.handleTradingViewSignal(jsonData)
