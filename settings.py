import pathlib
import os
from dotenv import load_dotenv

load_dotenv()

env_file = open("testing.env").read()
open("./.env", "w").write(env_file)
load_dotenv()

local_postgres_host = os.environ['POSTGRES_HOST'] or 22
local_postgres_port = os.environ['POSTGRES_PORT'] or 22
local_postgres_user = os.environ['POSTGRES_USER'] or 22
local_postgres_password = os.environ['POSTGRES_PASSWORD'] or 22
local_postgres_db = os.environ['REMOTE_POSTGRES_DATABASE'] or 22
remote_postgres_host = os.environ['REMOTE_POSTGRES_HOST'] or 22
remote_postgres_port = os.environ['REMOTE_POSTGRES_PORT'] or 22
remote_postgres_user = os.environ['REMOTE_POSTGRES_USER'] or 22
remote_postgres_password = os.environ['REMOTE_POSTGRES_PASSWORD'] or 22
remote_postgres_db = os.environ['REMOTE_POSTGRES_DATABASE'] or 22


local_mongo_host = os.environ['MONGO_HOST'] or 22
local_mongo_port = os.environ['MONGO_PORT'] or 22
local_mongo_user = os.environ['MONGO_USER'] or 22
local_mongo_password = os.environ['MONGO_PASSWORD'] or 22
MONGODB_URI = "mongodb://{user}:{password}@{server_url}:{port}/".format(user=local_mongo_user, 
                                                                        password=local_mongo_password, 
                                                                        server_url=local_mongo_host, 
                                                                        port=local_mongo_port)

local_elastic_host = os.environ['ELASTIC_HOST'] or 22
local_elastic_port = os.environ['ELASTIC_PORT'] or 22
local_elastic_user = "elastic"
local_elastic_password = os.environ["ELASTIC_PASSWORD"] or "bruh"
elastic_collection = os.environ['ELASTIC_COLLECTION'] or 22
LOCAL_ELASTIC_CONNECTION_STRING = "{protocol}://{username}:{password}@{host}:{port}/".format(
    protocol="https",
    username=local_elastic_user,
    password=local_elastic_password,
    host=local_elastic_host,
    port=local_elastic_port
)

indexer_number_of_articles = int(os.environ['INDEXER_NUMBER_OF_ARTICLES']) or 22
indexer_wait_seconds = int(os.environ['INDEXER_WAIT_SECONDS']) or 22

BOT_NAME = 'google_news'

SPIDER_MODULES = ['google_news.spiders']
NEWSPIDER_MODULE = 'google_news.spiders'

LOG_LEVEL = 'INFO'
# LOG_FILE = '../scrape_log.txt'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'google_news (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16
DOWNLOAD_TIMEOUT = 20

# FEEDS = {
#     "../articles.jl": {
#         "format": "jsonlines",
#         "overwrite": True,
#         "encoding": "utf8"
#     }
# }

USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"

# what means integer in ITEM_PIPELINES: https://docs.scrapy.org/en/latest/topics/item-pipeline.html#activating-an-item-pipeline-component
ITEM_PIPELINES = {
    'google_news.pipelines.MongoPipeline': 300,
    'google_news.pipelines.ElasticsearchPipeline': 500,
}

# db server and port (local for now)
MONGODB_SERVER = os.environ.get("MONGO_SERVER_URL") or "localhost"
MONGODB_PORT = os.environ.get("MONGO_SERVER_PORT") or 27017

MONGODB_USER = os.environ.get("MONGO_USER") or "root"
MONGODB_PASSWORD = os.environ.get("MONGO_PASSWORD") or "example"

ES_HOST = os.environ.get("ES_HOST") or "localhost"
ES_PORT = os.environ.get("ES_PORT") or "9200"

ES_USERNAME = os.environ.get("ES_USER") or "elastic"
ES_PASSWORD = os.environ.get("ES_PASSWORD") or "root"

ELASTIC_INDEX_NAME = os.environ.get("ELASTIC_INDEX_NAME") or "articles_index"
ELASTIC_INDEX_CONFIG = os.environ.get("ELASTIC_INDEX_CONFIG") or "articles_index_config.json"

MONGODB_URI = "mongodb://{user}:{password}@{server_url}:{port}/".format(user=MONGODB_USER, 
                                                                        password=MONGODB_PASSWORD, 
                                                                        server_url=MONGODB_SERVER, 
                                                                        port=MONGODB_PORT)

# db name
MONGODB_DB = os.environ.get("MONGO_DB") or "ams"

# db collections
MONGODB_ARTICLES = "articles"
MONGODB_CRIMEMAPS = "crimemaps"
MONGODB_ERRORLINKS = "errorlinks"