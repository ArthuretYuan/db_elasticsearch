# REF: https://elasticsearch-py.readthedocs.io/en/v8.17.1/

from datetime import datetime
from elasticsearch import Elasticsearch

ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "password"

# Connect to your Elasticsearch instance
es = Elasticsearch("https://localhost:9200",
                   ca_certs="./http_ca.crt",
                   basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD))

# Define the index name
index_name = "test_index"

# Define a document to save
doc = {
    "author": "John Doe",
    "text": "This is another sample document for Elasticsearch",
    "timestamp": datetime.now(),
}

# Index the document
res = es.index(index=index_name, 
               #id="001", # specify _id, otherwise assign automatically
               document=doc)
print(res)

# get documents by _id
res = es.get(index="test_index", id="OutnHpUBH6TyJ5tFb4E2")
print(res)