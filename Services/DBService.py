from pymongo import MongoClient
from bson.objectid import ObjectId


class DBService:
    def __init__(self, db_name, uri):
        """
        Initialize the DbService with a MongoDB URI and database name.
        """
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def add(self, collection_name, data):
        # """
        # Add a new document to a collection.
        # param collection_name: The name of the collection.
        # param data: A dictionary representing the document to insert.
        # :return: The inserted document's ID.
        # """
        collection = self.db[collection_name]
        result = collection.insert_one(data)
        return str(result.inserted_id)

    def get(self, collection_name, document_id):
        """
        Retrieve a document by its ID.
        param collection_name: The name of the collection.
        param document_id: The document's unique ID (as a string).
        return: The document, or None if not found.
        """
        collection = self.db[collection_name]
        return collection.find_one({"_id": ObjectId(document_id)})

    def update(self, collection_name, document_id, updates):
        # """
        # Update an existing document in a collection.
        # param collection_name: The name of the collection.
        # param document_id: The document's unique ID (as a string).
        # param updates: A dictionary with the fields to update.
        # return: True if the update was successful, False otherwise.
        # """
        collection = self.db[collection_name]
        result = collection.update_one({"_id": ObjectId(document_id)}, {"$set": updates})
        return result.modified_count > 0

    def delete(self, collection_name, document_id):
        """
        Delete a document by its ID.
        param collection_name: The name of the collection.
        param document_id: The document's unique ID (as a string).
        return: True if the deletion was successful, False otherwise.
        """
        collection = self.db[collection_name]
        result = collection.delete_one({"_id": ObjectId(document_id)})
        return result.deleted_count > 0

    def find(self, collection_name, query=None):
        """
        Find documents in a collection based on a query.
        param collection_name: The name of the collection.
        param query: A dictionary representing the query (optional).
        return: A list of matching documents.
        """
        if query is None:
            query = {}
        collection = self.db[collection_name]
        return list(collection.find(query))

    def execute_raw_query(self, collection_name, query):
        """
        Execute a raw MongoDB query.
        param collection_name: The name of the collection.
        param query: A MongoDB query.
        return: The result of the query.
        """
        collection = self.db[collection_name]
        return list(collection.find(query))

    def close(self):
        """
        Close the MongoDB connection.
        """
        self.client.close()
