from Interfaces.IRegistryFactory import IRegistryFactory


class TakeProfitFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in TakeProfitFactory._registry:
            return TakeProfitFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes : {name}")

    def registerClass(self,name, time_window_class):
        pass


