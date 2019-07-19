from pymongo import MongoClient
from dotenv import load_dotenv
from datetime import datetime as dt
import os

class MongoCRUD:

    def __init__(self):
        load_dotenv()  # setup use for getting environment variables

        # Connect with the portnumber and host
        self.client = MongoClient(os.getenv('MONGO_ADDRESS'))

        # Access database
        mongo_db = self.client['Logging']

        # Access collection
        self.my_collection = mongo_db['Logs']

    def write(self, key, action_type):
        # dictionary to be added in the database
        rec = {
            'key': key, # issue key
            'action': action_type, # action ex resolve or email
            'date_time': dt.now() # date time which emailed
        }
        self.my_collection.insert_one(rec) # write to database

    def read(self):
        pass

    # close db connection
    def close(self):
        self.client.close()




