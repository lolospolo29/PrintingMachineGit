from Interfaces.RiskManagement.ITechnicalStop import ITechnicalStop


class EndOfImbalance(ITechnicalStop):
    def getExit(self,candle):
        pass

    def getExitList(self,data):
        pass
