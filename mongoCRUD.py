from pymongo import MongoClient
from bson.objectid import ObjectId
from collections.abc import Mapping
import pprint

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        self.client = MongoClient('mongodb://%s:%s@localhost:40964/?authMechanism=DEFAULT&authSource=AAC' % (username, password))
        self.database = self.client['AAC']

    def create(self, data): # Check for null
        if data is not None:

            if isinstance(data, Mapping): # Ensure data is dictionary
                result = self.database.animals.insert(data)
                print("Insertion successful")
            else:
                raise Exception("Please enter data as a valid dictionary")
        else:
            print("Nothing to save, because data parameter is empty")

    def read(self, query):
        if query is not None:
            if isinstance(query, Mapping): # Ensure data is dictionary
                if self.database.animals.find(query).count() > 0:
                    try:
                        results = self.database.animals.find(query) # Find key/value
                        for document in results:
                            print(document)
                            print()
                        return results
                    except Exception as e:
                        print(e) # Print error message if one occurs
                else:
                    print("No documents found")
            else:
                print("Invalid input: ")
                print("Please enter read paramaters as a valid Python dictionary")
        else:
            print("Invalid input: ")
            print("Read paramaters cannot be null")


    def update(self, query, data):
        if query is not None and data is not None:

            if isinstance(query, Mapping) and isinstance(data, Mapping): # Ensure both inputs are valid dictionaries

                if self.database.animals.find(query).count() > 0: # Ensure document(s) exist before trying to update
                    try:
                        result = self.database.animals.update_many(query, {"$set": data}, upsert=False)
                            print(result.raw_result)
                    except Exception as e:
                        print(e) # Print error message if error occurs
                else:
                    print("No documents affected: ")
                    print("Specified document does not exist")

            else:
                print("Invalid input: ")
                print("Please enter update paramaters as valid Python dictionaries")

        else:
            print("Invalid input: ")
            print("Update paramaters cannot be null")

    def delete(self, query):
        if query is not None: # Ensure not null
            if isinstance(query, Mapping): # Ensure valid dictionary
                if self.database.animals.find(query).count() > 0: # Ensure document(s) exist before trying to update
                    try:
                        result = self.database.animals.delete_many(query)
                            print(result.raw_result)
                    except Exception as e:
                        print(e) # Print error message if error occurs
                else:
                    print("No documents affected: ")
                    print("Specified document does not exist")
            else:
                print("Invalid input: ")
                print("Please enter delete paramaters as a valid Python Dictionary")
        else:
            print("Invalid input: ")
            print("Delete paramaters cannot be null")
