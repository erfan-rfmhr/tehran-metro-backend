from fastapi import status
from fastapi.exceptions import HTTPException
from neo4j import AsyncSession

from config.db import get_session
from station.rest.v1.schemas.base import Property, Relation, Station


class StationManager:
    _db = get_session()

    @staticmethod
    async def _do_cypher(session: AsyncSession, cypher, **kwargs):
        result = await session.run(cypher.format(**kwargs))
        graph = await result.graph()
        return graph.nodes, graph.relationships

    @classmethod
    async def get_station_by_name(cls, en_name: str) -> Station:
        from station.raw_queries import GET_STATION_BY_NAME

        nodes, relationships = await cls._db.execute_read(
            cls._do_cypher, GET_STATION_BY_NAME, name=en_name
        )
        if len(nodes) == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Station {en_name} not found.",
            )
        station_property = list(nodes)[0]._properties
        property_schema = Property(**station_property)
        relations_schema = [
            Relation(**{k: v for k, v in relation._end_node.items()})
            for relation in relationships
        ]
        station_schema = Station(property=property_schema, relations=relations_schema)
        return station_schema
