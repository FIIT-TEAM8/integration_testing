from pymongo import MongoClient
  
Client = MongoClient()
myclient = MongoClient('localhost', 27017)
  
my_database = myclient["ams"]  
my_collection = my_database["articles"] 
  
# number of documents in the collection
mydoc = my_collection.find().count()
print("The number of documents in collection : ", mydoc) 
    