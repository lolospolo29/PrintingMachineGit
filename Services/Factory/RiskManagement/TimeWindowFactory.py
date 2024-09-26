from Interfaces.IFactory import IFactory
from Models.RiskModels.TimeModels.London import LondonOpen
from Models.RiskModels.TimeModels.NYOpen import NYOpen


class TimeWindowFactory(IFactory):
    def returnClass(self, name):
        if name == "LondonOpen":
            return LondonOpen(name)
        if name == "NYOpen":
            return NYOpen(name)
