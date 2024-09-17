from Interfaces.RiskManagement.ITimeWindow import ITimeWindow


class NYOpen(ITimeWindow):
    def getExitWindow(self):
        return (14)

    def getEntryWindow(self):
        return (8,11)


