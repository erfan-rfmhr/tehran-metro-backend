FROM docker.arvancloud.ir/neo4j

# copy the neo4j.conf file to the container
COPY neo4j/neo4j.conf /var/lib/neo4j/conf/neo4j.conf

# copy the plugins to the container
# COPY config/neo4j/plugins /var/lib/neo4j/plugins

# copy data to the container
COPY neo4j/import/ /var/lib/neo4j/import

CMD ["neo4j", "start"]
