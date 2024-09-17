from Interfaces.RiskManagement.ITimeWindow import ITimeWindow


class LondOpen(ITimeWindow):
    def getExitWindow(self):
        return (12)

    def getEntryWindow(self):
        return (2,5)

