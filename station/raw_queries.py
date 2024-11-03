GET_STATION_BY_NAME = (
    "MATCH (s:Station {{name: '{name}'}})-[r]->(other) RETURN s, r, other"
)
