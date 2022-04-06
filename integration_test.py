from pymongo import MongoClient
import requests

local_mongo_uri = 'mongodb://localhost:27017/ams'
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

param = (('v', ''),) # '-v' is for --verbose

resp = requests.get('http://localhost:9200/_cat/indices', params=param)
print ('\nHTTP code:', resp.status_code, '-- response:', resp, '\n')
print ('dir:', dir(resp), '\n')
print ('response text:', resp.text)
    