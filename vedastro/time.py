import VedAstro.Library as libray

from vedastro.geolocation import GeoLocation


class Time:
    """
    Class representing VedAstro time.
    """

    def __init__(self, date: str, time: str, location: GeoLocation):
        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(time, str):
            raise TypeError("Time must be a string")
        if not isinstance(location, GeoLocation):
            raise TypeError("Location must be a GeoLocation")
        self.date = date
        self.time = time
        self.location = location




