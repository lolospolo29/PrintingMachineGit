from Interfaces.IRegistryFactory import IRegistryFactory


class StrategicFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in StrategicFactory._registry:
            return StrategicFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes: {name}")

    def registerClass(self,name, time_window_class):
        pass


