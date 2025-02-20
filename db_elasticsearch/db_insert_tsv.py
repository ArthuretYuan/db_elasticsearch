# REF: https://elasticsearch-py.readthedocs.io/en/v8.17.1/

from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers
import csv

ELASTIC_USERNAME = "elastic"
ELASTIC_PASSWORD = "password"

# Connect to your Elasticsearch instance
es = Elasticsearch("https://localhost:9200",
                   ca_certs="./http_ca.crt",
                   basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD))
# Define the index name
index_name = "index_house_price"


class HousePriceES():

    def __init__(self):
        # Connect to your Elasticsearch instance
        self.es = Elasticsearch("https://localhost:9200",
                        ca_certs="./http_ca.crt",
                        basic_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD))
        # Define the index name
        self.index_name = "index_house_price" 

    def insert_data_tsv(self):
        # Open the TSV file
        f = open("test_data/house-price.tsv", "r", encoding="utf-8")
        reader = csv.reader(f, delimiter="\t")  # TSV uses '\t' as delimiter
        next(reader)  # Skip the header row

        # create a generator to read the tsv file
        def generate_docs():
            for row in reader:
                doc = {"_index": self.index_name,
                    "price": row[0],
                    "area": row[1],
                    "bedrooms": row[2],
                    "bathrooms": row[3],
                    "mainroad": row[4],
                    "guestroom": row[5],
                    "basement": row[6],
                    "hotwaterheating": row[7],
                    "airconditioning": row[8],
                    "parking": row[9],
                    "prefarea": row[10],
                    "furnishingstatus": row[11],
                    "timestamp": datetime.now()}
                yield doc

        helpers.bulk(self.es, generate_docs())

    def search_doc(self):
        res = self.es.search(
            index=self.index_name,
            query={"match": {"bedrooms": "3"}})
        print(res)


if __name__=="__main__":
    house_price_es = HousePriceES()
    house_price_es.search_doc()