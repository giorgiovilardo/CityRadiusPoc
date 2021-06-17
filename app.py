from sqlalchemy import create_engine
from conf import conf


def main():
    db = gimme_a_db()

    while True:
        activity_count, distance, lat, lon = get_user_input()

        q = f"""
SELECT name, activity_count, ST_Distance(location_geog, ref_geom) AS distance
FROM city
CROSS JOIN (SELECT ST_MakePoint({lon}, {lat})::geography AS ref_geom) AS r
WHERE ST_DWithin(location_geog, ref_geom, {int(distance)*1000})
AND activity_count >= {activity_count}
ORDER BY ST_Distance(location_geog, ref_geom);
"""

        with db.connect() as connection:
            result = connection.execute(q)

        for city_name, activities, distance in result:
            print(
                f"{city_name} has {activities} activities and is distant {distance//1000} km"
            )


def get_user_input():
    print("### use ctrl+c to exit ###")
    print("### some test coordinates: ###")
    print("### Milan: 45.46, 9.18 ###")
    print("### Paris: 48.86, 2.34 ###")
    print("### Beijing: 39.91, 116.38 ###")
    lat = input(
        "Insert latitude in float 2 digits format (eg -12.34, range: -90 to 90)> "
    )
    lon = input(
        "Insert longitude in float 2 digits format (eg -12.34, range: -180 to 180)> "
    )
    km = input("Insert radius in km, integer plz> ")
    ac = input("Insert minimum number of activities for the included nearest cities> ")
    return ac, km, lat, lon


def gimme_a_db():
    engine = create_engine(conf.connection_string)
    return engine


if __name__ == "__main__":
    main()
