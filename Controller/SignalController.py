class SignalControler:
    def __init__(self, Monitoring,TradingController):
        self._Monitoring = Monitoring
        self._TradingController = TradingController

    def orderSignal(self, jsonData):

        if "tradingViewData" in jsonData:
            self._Monitoring.logInformation("TradingView Data received")
            self._TradingController.handleTradingViewSignal(jsonData)
