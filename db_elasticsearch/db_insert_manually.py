from datetime import datetime
from elasticsearch import Elasticsearch

# Connect to your Elasticsearch instance
es = Elasticsearch(["http://localhost:9200"])  # Update with your actual host

# Define the index name
index_name = "my_index"

# Define a document to save
doc = {
    "author": "John Doe",
    "text": "This is a sample document for Elasticsearch",
    "timestamp": datetime.snow(),
}

# Index the document
res = es.index(index=index_name, document=doc)

# Print response
print(res)