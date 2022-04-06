from pymongo import MongoClient

local_mongo_uri = 'mongodb://mongodb0.example.com:27017'
mongo_username = 'test'
mongo_password = 'test'

# connect to local MongoDB container
my_client = MongoClient(
    host = local_mongo_uri,
    serverSelectionTimeoutMS = 3000,
    username = mongo_username,
    password = mongo_password
)
  
my_database = my_client["ams"]  
my_collection = my_database["articles"]
  
# number of documents in the collection
mydoc = my_collection.find().count()
print("The number of documents in collection : ", mydoc) 
    