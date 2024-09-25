from Interfaces.IRegistryFactory import IRegistryFactory


class InvalidationFactory(IRegistryFactory):
    _registry = {}

    def returnRegistryClass(self,name):
        if name in InvalidationFactory._registry:
            return InvalidationFactory._registry[name]()
        else:
            raise ValueError(f"Unbekanntes: {name}")

    def registerClass(self,name, time_window_class):
        pass


