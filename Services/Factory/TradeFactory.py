from Interfaces.IFactory import IFactory


class TradeFactory(IFactory):
    def returnClass(self,name):
        if name == "TestStrategy":
            pass
