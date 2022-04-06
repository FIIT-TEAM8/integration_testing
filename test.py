import os
import sys
import json
import time
from pymongo import MongoClient
from elasticsearch import Elasticsearch
from ssh_pymongo import MongoSession

local_mongo_uri = 'mongodb://mongo_db'

mongo_username = 'root'
mongo_password = 'password'
mongo_db = 'admin'
mongo_collection = 'articles'
mongo_column = 'html'
num_of_articles = 100

elastic_container_name = 'es01'
elastic_container_port = 9200
elastic_index_name = 'article_index'
elastic_index_config = 'articles_index_config.json'
elastic_field = 'text' # mongo data will be indexed in this field

wait_seconds = 60

time.sleep(wait_seconds) # wait n seconds for MongoDB and Elasticsearch containers

# connect to local MongoDB container
cluster = MongoClient(
    host=local_mongo_uri,
    serverSelectionTimeoutMS = 3000,
    username=mongo_username,
    password=mongo_password
)

print('Successfully connected to local MongoDB container.')

# insert scraped articles into mongo
# TODO


# connect to collection on remote MongoDB
#articles_collection = db[mongo_collection]
articles_collection = ""

print('Retrieving articles from remote MongoDB...')

# retrieve articles from remote MongoDB for seeding local MongoDB container and indexing in local Elasticsearch container
cursor = articles_collection.find().limit(num_of_articles)
scraped_articles = ""

print('Articles was successfully retrieved from remote MongoDB.')

# elasticsearch configuration
# this will connect to local Elasticsearch container
es = Elasticsearch(hosts=[
    {
        "host": elastic_container_name,
        "port": elastic_container_port
    }
])

print('Successfully connected to local Elasticsearch container.')

# create index if not exists
if not es.indices.exists(index=elastic_index_name):
    # firstly load index configuration
    with open(os.getcwd() + '/' + elastic_index_config) as articles_config_file:
        configuration = json.load(articles_config_file)

        # create index
        res = es.indices.create(index=elastic_index_name, settings=configuration["settings"])
        
        # make sure index was created
        if not res['acknowledged']:
            print('Index wasn\'t created')
            print(res)
            sys.exit()
        else:
            print('Index successfully created.')

local_db = cluster[mongo_db]

local_collection = local_db[mongo_collection]

print('Indexing in Elasticsearch and seeding MongoDB on your local containers...')

# iterate through each article form remote collection and perform indexing
for article in scraped_articles:
    # retrieve and convert article's id
    item_id_string = str(article['_id'])

    # article's html
    article_column_value = article[mongo_column]

    # index article's column in Elasticsearch
    res = es.index(
        index=elastic_index_name,
        doc_type='_doc',
        id=item_id_string, # document id in Elasticsearch == article id in articles collection
        document=json.dumps(
            {elastic_field: article_column_value}
        )
    )

    # insert into local MongoDB collection
    local_collection.insert_one({"_id": item_id_string, mongo_column: article_column_value})

print('Indexing finished.')


# akcia -> zapne sa scraper -> zapis do monga a elasticu -> connect to mongo / elastic (script) -> porovnat hodnoty 


    