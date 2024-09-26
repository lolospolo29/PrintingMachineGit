from Interfaces.IFactory import IFactory
from Models.RiskModels.Ratio.FixedRatio import FixedRatio
from Models.RiskModels.Ratio.VariableRatio import VariableRatio


class RatioFactory(IFactory):
    def returnClass(self,name):
        if name == "FixedRatio":
            return FixedRatio(name)
        if name == "Ratio":
            return VariableRatio(name)
