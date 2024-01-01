from pymongo import MongoClient
from datetime import datetime, timedelta
from pymongo.server_api import ServerApi
from decouple import config

url = config("MONGO_URL")

client = MongoClient(
    url,
    server_api=ServerApi("1"),
    connectTimeoutMS=30000,
    socketTimeoutMS=None,
    connect=False,
    maxPoolsize=1,
)

db = client["the_scribe"]
collection = db["codes"]


    