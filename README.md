# db_elasticsearch
This repo includes the scripts of basic operations of elasticsearch.
REF: https://www.vps-mart.com/blog/how-to-set-up-an-elasticsearch-cluster-using-docker

# Install Elasticsearch
1. create a 'data' folder under cwd
2. docker-compose -f docker-compose-elasticsearch.yaml up
3. Go to the other terminal (not sure needed or not)
4. docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-reset-password -u elastic (reset password if needed)
5. docker exec -it es01 /usr/share/elasticsearch/bin/elasticsearch-create-enrollment-token -s kibana (obtain the enrollment token for Kibana)
e.g., eyJ2ZXIiOiI4LjMuMSIsImFkciI6WyIxNzIuMjEuMC4yOjkyMDAiXSwiZmdyIjoiNzE5NzRiNmU5NTlhNDRlNGY1YzM1MzQyMTZkNzBmNWI0YzA4ZTcyMGQ1MmYyMDU5YmZmMmU5OTNmNmNiZDUzNCIsImtleSI6IlNLVTJHWlVCNkJac1VZdnA0Z0lsOjQtU1ExSTEzU195Z25vMGFkUEc3UHcifQ==
6. docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt . (copy the SSL certificate locally)
7. curl --cacert http_ca.crt -u elastic:<your_password> https://localhost:9200 (verify installation)

# Install Kibana

1. docker-compose -f docker-compose-kibana.yaml up
2. Go to the link displayed in the terminal (e.g., http://0.0.0.0:5601/?code=092927)
3. Enter the enrollment token generated previously
4. docker exec -it kib01 /usr/share/kibana/bin/kibana-verification-code (get verification code if needed)
5. login with username and password (default username is 'elastic')
