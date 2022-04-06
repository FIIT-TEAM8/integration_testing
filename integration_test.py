from threading import local
from pymongo import MongoClient
import requests

local_mongo_uri = 'mongodb://test:test@localhost:27017/'

my_client = MongoClient(local_mongo_uri)
  
my_database = my_client["ams"]  
my_collection = my_database["articles"]
  
# number of documents in the collection
mydoc = my_collection.find().count()
print("The number of documents in collection : ", mydoc)

ES_HOST = 'localhost'
ES_PORT = 9200
ES_USER = 'test'
ES_PASSWORD = 'test'
ELASTIC_INDEX_NAME = 'main'
ES_PROTOCOL="https"

ES_SEARCH_STRING = "{protocol}://{host}:{port}/{index}/_count".format(
    protocol=ES_PROTOCOL,
    host=ES_HOST,
    port=ES_PORT,
    index=ELASTIC_INDEX_NAME
    )

headers = {}
resp = requests.get(ES_SEARCH_STRING, 
            headers=headers, 
            json={}, 
            verify=False, 
            auth=(ES_USER, ES_PASSWORD))

print ('\nHTTP code:', resp.status_code, '-- response:', resp, '\n')
print ('dir:', dir(resp), '\n')
print ('response text:', resp.text)
    