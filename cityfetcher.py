from City import City
import json
import requests


def get_some_city_objects() -> list[City]:
    cities = _fetch_some_cities()
    return [
        City(
            city["id"],
            city["uuid"],
            city["name"],
            city["latitude"],
            city["longitude"],
            city["activities_count"],
        )
        for city in cities
    ]


def _fetch_some_cities() -> list:
    result = []
    print("Fetching cities from api/v3/cities")
    for i in range(0, 1100, 100):
        req = requests.get(
            f"https://api.musement.com/api/v3/cities?offset={i}&limit=100"
        )
        result += json.loads(req.text) if req.status_code == 200 else []
    return result
