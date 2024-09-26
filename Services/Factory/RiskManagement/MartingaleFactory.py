from Interfaces.IFactory import IFactory
from Models.RiskModels.Martingale.AntiMartingale import AntiMartingale
from Models.RiskModels.Martingale.Martingale import Martingale


class MartingaleFactory(IFactory):
    def returnClass(self,name):
        if name == "AntiMartingale":
            return AntiMartingale(name)
        if name == "Martingale":
            return Martingale(name)
