from Interfaces.IRegistryFactory import IRegistryFactory


class BrokerFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in BrokerFactory._registry:
            return BrokerFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes : {name}")

    def registerClass(self,name, time_window_class):
        pass


