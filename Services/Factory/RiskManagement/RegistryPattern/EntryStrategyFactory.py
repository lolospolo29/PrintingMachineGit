from Interfaces.IRegistryFactory import IRegistryFactory


class EntryStrategyFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in EntryStrategyFactory._registry:
            return EntryStrategyFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes: {name}")

    def registerClass(self,name, time_window_class):
        pass


