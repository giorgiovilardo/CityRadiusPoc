class City:
    def __init__(
        self,
        id: int,
        uuid: str,
        name: str,
        latitude: float,
        longitude: float,
        activities: int,
    ):
        self.musement_id = id
        self.uuid = uuid
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.activities = activities
