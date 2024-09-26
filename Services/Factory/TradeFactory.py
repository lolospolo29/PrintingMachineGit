from Interfaces.IFactory import IFactory
from Models.Trade.Order import Order
from Models.Trade.Trade import Trade
from Models.Trade.TradeEntry import TradeEntry
from Models.Trade.TradeExit import TradeExit


class TradeFactory(IFactory):
    def returnClass(self, name):
        if name == "Trade":
            # Trade()
            pass
        if name == "Order":
            # return Order()
            pass
        if name == "TradeEntry":
            # return TradeEntry()
            pass
        if name == "TradeExit":
            # return TradeExit()
            pass
