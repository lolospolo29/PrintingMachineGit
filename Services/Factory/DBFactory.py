from Interfaces.IFactory import IFactory
from Models.DBModels.MongoDB import DBService
from Services.Helper.SecretsManager import SecretsManager


class DBFactory(IFactory):
    def __init__(self):
        self._SecretsManager = SecretsManager()

    def returnClass(self, dbType, dbName):

        if dbType == "mongodb":

            secretsMongo = self._SecretsManager.get_secret(dbType)

            return DBService(dbName, secretsMongo)
        return None
