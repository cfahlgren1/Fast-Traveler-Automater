from pymongo import MongoClient, GEOSPHERE
from dotenv import load_dotenv
from datetime import datetime as dt
import os

class MongoCRUD:

    def __init__(self, db_type):
        load_dotenv()  # setup use for getting environment variables

        if db_type == "logging":
            # Connect with the portnumber and host
            self.client = MongoClient(os.getenv('MONGO_ADDRESS'))

            # Access database
            mongo_db = self.client['Logging']

            # Access collection
            self.my_collection = mongo_db['Logs']

        elif db_type == "ft_data":
            # Connect with the portnumber and host
            self.client = MongoClient(os.getenv('MONGO_ADDRESS'))

            # Access database
            mongo_db = self.client['FastTravelers']

            # Access collection
            self.my_collection = mongo_db['Fast Travelers']

        else:
            raise Exception('incorrect db specified')


    def write(self, key, action_type):
        # dictionary to be added in the database
        rec = {
            'key': key, # issue key
            'action': action_type, # action ex resolve or email
            'date_time': dt.now() # date time which emailed
        }
        self.my_collection.insert_one(rec) # write to database

    def write_ft(self, user, key, ft_type, date, description, coordinates):
        rec = {
            'user' : str(user),
            'key' : str(key),
            'type' : ft_type,
            'date' : str(date),
            'description': str(description),
            'location': {
                'type' : 'Point',
                'coordinates': coordinates
            }
        }
        self.my_collection.insert_one(rec)  # write to database

    def check_exists(self, key):
        return(self.my_collection.count_documents({'key' : key}, limit=1) != 0)

    # get all resolved document count from db
    def get_resolved(self):
        return(self.my_collection.count_documents({'action' : 'resolved'}))

    # get all emailed document count from db
    def get_emailed(self):
        return(self.my_collection.count_documents({'action':'emailed'}))

    # get all deleted document count from db
    def get_deleted(self):
        return(self.my_collection.count_documents({'action':'deleted'}))

    # get all assigned document count from db
    def get_assigned(self):
        return(self.my_collection.count_documents({'action':'deleted'}))

    # close db connection
    def close(self):
        self.client.close()




