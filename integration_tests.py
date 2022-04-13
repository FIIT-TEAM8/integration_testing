from pymongo import MongoClient
import requests

MONGO_URI_LOCAL = 'mongodb://test:test@localhost:27017/'
MONGODB_DB = "ams"
MONGODB_COLLECTION = "articles"

ES_PROTOCOL = "https"
ES_HOST = "localhost"
ES_PORT = 9200
ES_INDEX_NAME = "articles_index"
ES_USER = "elastic"
ES_PASSWORD = "test"

my_client = MongoClient(MONGO_URI_LOCAL)
my_database = my_client[MONGODB_DB]  
my_collection = my_database[MONGODB_COLLECTION]


# test if number of documents in MongoDB is the same as number of documents indexed in Elasticsearch
def test_articles_equal():

    # number of documents in MongoDB collection
    mongodb_count = my_collection.find().count()
    print("Number of documents in MongoDB collection: ", mongodb_count)

    ES_SEARCH_STRING = "{protocol}://{host}:{port}/{index}/_count".format(
        protocol=ES_PROTOCOL,
        host=ES_HOST,
        port=ES_PORT,
        index=ES_INDEX_NAME
        )

    resp = requests.get(ES_SEARCH_STRING, 
                verify=False, 
                auth=(ES_USER, ES_PASSWORD))
    
    if resp:
        # number of documents in Elasticsearch index from response
        elastic_count = int(resp.text.split(",")[0].split(":")[1])

        print ('HTTP code:', resp.status_code)
        print ('Number of documents in Elasticsearch:', elastic_count)

        if elastic_count == mongodb_count:
            return 0

    return 1

# builds elasticsearch query with or without filters
def build_query(query, keywords, regions, page_num, size):
    
    # default body of query withou any filters
    body = {
        # pagination
        "from": page_num * size - size,
        "size": size,
        "query": {
            "bool": {
                "must": [
                    # match main query in article itself
                    {
                        "match": {
                            "html": {
                                "query": query,
                                "operator": "and"
                            }
                        }
                    },
                ]
            }
        }
    }

    # add crime keywords filter
    if keywords:
        keywords_filter = {
            "terms": {
                "keywords.keyword": keywords
            }
        }
        body["query"]["bool"]["must"].append(keywords_filter)
        
    # add regions filter
    if regions:
        regions_filter = {
            "terms": {
                "region": regions
            }
        }
        body["query"]["bool"]["must"].append(regions_filter)

    return body


def get_ids(results):
    ids = []

    for res in results["hits"]["hits"]:
        ids.append(res["_id"])

    return ids

# test if stored document in MongoDB has the filters that were given in request
def test_filters_mongodb():
    query = "donald"
    keywords = []
    regions = []
    page_num = 1
    size = 10
    body = build_query(query, keywords, regions, page_num, size)

    ES_SEARCH_STRING = "{protocol}://{host}:{port}/{index}/_search".format(
        protocol=ES_PROTOCOL,
        host=ES_HOST,
        port=ES_PORT,
        index=ES_INDEX_NAME
        )
    
    build_query(query, keywords, regions, page_num, size)
    headers = {}
    response = requests.get(ES_SEARCH_STRING, 
        headers=headers, 
        json=body, 
        verify=False, 
        auth=(ES_USER, ES_PASSWORD))
    response = response.json()

    #article_ids = get_ids(response)
    #print(article_ids)
    
    return 0

check1 = test_articles_equal()
# check2 = test_filters_mongodb()

# if check1 == 0 and check2 == 0:
#     print("SUCCESS")
#     exit(0)

# exit(1)