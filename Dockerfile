# Start from the official Elasticsearch image
FROM docker.elastic.co/elasticsearch/elasticsearch:8.3.1

# # Install OpenJDK 11
# RUN apt-get update && apt-get install -y openjdk-11-jdk

# # Set JAVA_HOME environment variable
# ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-arm64