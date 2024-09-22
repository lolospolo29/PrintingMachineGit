from Interfaces.RiskManagement.ITimeWindow import ITimeWindow


class LondonOpen(ITimeWindow):
    def getExitWindow(self):
        return (12)

    def getEntryWindow(self):
        return (2,5)

