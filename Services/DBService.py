class DBHelper:
    def __init__(self,DBFactory,Monitoring,DataMapper):
        self._DBFactory = DBFactory
        self._Monitoring = Monitoring
        self._DataMapper = DataMapper

    def mapDataToClass(self,data,name):
        return self._DataMapper.MapToClass(data, name)

    def addDataToDB(self, dbType, dbName, tableName, data):
        db = self._DBFactory.returnClass(dbType, dbName)
        db.add(tableName, data)
        self._Monitoring.logInformation((tableName, ": DB added New Data"))

    def deleteDataFromData(self, dbType, dbName, tableName, query):
        db = self._DBFactory.returnClass(dbType, dbName)
        db.deleteByQuery(tableName, query)
        self._Monitoring.logInformation((tableName, ": DB Deleted Data"))

    @staticmethod
    def buildQuery(className, attribute, value):
        return {f"{className}.{attribute}": value}

    def findDataInDBResultToList(self, dbType, dbName, tableName, query):
        db = self._DBFactory.returnClass(dbType, dbName)
        return db.find(tableName, query)
