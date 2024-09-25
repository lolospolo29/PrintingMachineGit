from Interfaces.IRegistryFactory import IRegistryFactory


class TechnicalEntryFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in TechnicalEntryFactory._registry:
            return TechnicalEntryFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes : {name}")

    def registerClass(self,name, time_window_class):
        pass


