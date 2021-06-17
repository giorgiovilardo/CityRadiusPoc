from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, Float
from geoalchemy2 import Geography

import cityfetcher
from conf import conf


def setup_db():
    db = create_engine(conf.connection_string, echo=True)
    connection = db.connect()

    metadata = MetaData()

    city_table = Table(
        "city",
        metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String),
        Column("uuid", String),
        Column("musement_id", String),
        Column("lat", Float),
        Column("long", Float),
        Column("activity_count", Integer),
        Column("location_geog", Geography("POINT")),
    )
    city_table.create(db)

    cities = cityfetcher.get_some_city_objects()

    for city in cities:
        insertor = city_table.insert().values(
            name=city.name,
            uuid=city.uuid,
            musement_id=city.musement_id,
            lat=city.latitude,
            long=city.longitude,
            activity_count=city.activities,
            location_geog=f"POINT({city.longitude} {city.latitude})",
        )
        connection.execute(insertor)


if __name__ == "__main__":
    setup_db()
