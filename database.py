from pymongo import MongoClient
import dotenv
import os
dotenv.load_dotenv()

MONGO_URL = os.getenv('db_url')
DB_NAME = os.getenv('DB_NAME')

def get_mongodb():
    client = MongoClient(MONGO_URL)
    db = client[DB_NAME]
    return db
