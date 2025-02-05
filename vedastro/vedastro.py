import requests
import json
from enum import Enum

class GeoLocation:
    def __init__(self, location_name, longitude, latitude):
        """
        Initialize a GeoLocation object.

        Args:
        location_name (str): The name of the location.
        longitude (float): The longitude of the location.
        latitude (float): The latitude of the location.
        """
        self.location_name = location_name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        """
        Return a string representation of the GeoLocation object.
        """
        return f"{self.location_name} ({self.longitude}, {self.latitude})"

class Time:
    def __init__(self, time_string, geolocation):
        """
        Initialize a Time object.

        Args:
        time_string (str): A string representing the time in the format "HH:MM DD/MM/YYYY +HH:MM".
        geolocation (GeoLocation): The geolocation associated with the time.
        """
        self.time_string = time_string
        self.geolocation = geolocation

    def __str__(self):
        """
        Return a string representation of the Time object.
        """
        return f"{self.time_string} at {self.geolocation}"

    def url_time_string(self):
        """
        Return the time string formatted as "HH:MM/DD/MM/YYYY/+HH:MM"
        """
        time_parts = self.time_string.split()
        time = time_parts[0]
        date = time_parts[1].split('/')
        offset = time_parts[2]
        return f"{time}/{date[0]}/{date[1]}/{date[2]}/{offset}"

class PlanetName(Enum):
    All = "All"
    Sun = "Sun"
    Moon = "Moon"
    Mars = "Mars"
    Mercury = "Mercury"
    Jupiter = "Jupiter"
    Venus = "Venus"
    Saturn = "Saturn"
    Rahu = "Rahu"
    Ketu = "Ketu"

class HouseName(Enum):
    House1 = "House1"
    House2 = "House2"
    House3 = "House3"
    House4 = "House4"
    House5 = "House5"
    House6 = "House6"
    House7 = "House7"
    House8 = "House8"
    House9 = "House9"
    House10 = "House10"
    House11 = "House11"
    House12 = "House12"

class ZodiacName(Enum):
    Aries = "Aries"
    Taurus = "Taurus"
    Gemini = "Gemini"
    Cancer = "Cancer"
    Leo = "Leo"
    Virgo = "Virgo"
    Libra = "Libra"
    Scorpio = "Scorpio"
    Sagittarius = "Sagittarius"
    Capricorn = "Capricorn"
    Aquarius = "Aquarius"
    Pisces = "Pisces"

class Calculate:
    api_key = None
    base_url = "https://api.vedastro.org/api/Calculate"

    @classmethod
    def SetAPIKey(cls, api_key):
        cls.api_key = api_key

    @classmethod
    def _make_request(cls, endpoint, params):
        url = f"{cls.base_url}/{endpoint}"
        params["APIKey"] = cls.api_key
        query_string = "/".join(f"{key}/{value}" for key, value in params.items())
        full_url = f"{url}/{query_string}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if "Payload" in data and data["Payload"]:
                return list(data["Payload"].values())[0]
            else:
                raise ValueError("Payload is missing or empty")
        else:
            return f"Error: API request failed with status code {response.status_code}"

    @classmethod
    def MatchReport(cls, male_birth_time, female_birth_time):
        endpoint = "MatchReport"
        params = {
            "Location": male_birth_time.geolocation.location_name,
            "Time": male_birth_time.time_string,
            "Location2": female_birth_time.geolocation.location_name,
            "Time2": female_birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetData(cls, planet_name, birth_time):
        endpoint = "AllPlanetData"
        params = {
            "PlanetName": planet_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseData(cls, house_name, birth_time):
        endpoint = "AllHouseData"
        params = {
            "HouseName": house_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllZodiacSignData(cls, zodiac_name, birth_time):
        endpoint = "AllZodiacSignData"
        params = {
            "ZodiacName": zodiac_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionNames(cls, birth_time):
        endpoint = "HoroscopePredictionNames"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseZodiacSign(cls, house_name, birth_time):
        endpoint = "HouseZodiacSign"
        params = {
            "HouseName": house_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInHouse(cls, house_name, birth_time):
        endpoint = "PlanetsInHouse"
        params = {
            "HouseName": house_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInHouseBasedOnSign(cls, house_name, birth_time):
        endpoint = "PlanetsInHouseBasedOnSign"
        params = {
            "HouseName": house_name.value,
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtRange(cls, birth_time, start_time, end_time, levels, precision_hours):
        endpoint = "DasaAtRange"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
            "Location2": start_time.geolocation.location_name,
            "Time2": start_time.url_time_string(),
            "Location3": end_time.geolocation.location_name,
            "Time3": end_time.url_time_string(),
            "Levels": levels,
            "PrecisionHours": precision_hours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunriseTime(cls, birth_time):
        endpoint = "SunriseTime"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunsetTime(cls, birth_time):
        endpoint = "SunsetTime"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PanchangaTable(cls, birth_time):
        endpoint = "PanchangaTable"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LagnaSignName(cls, birth_time):
        endpoint = "LagnaSignName"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhinnashtakavargaChart(cls, birth_time):
        endpoint = "BhinnashtakavargaChart"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GulikaLongitude(cls, birth_time):
        endpoint = "GulikaLongitude"
        params = {
            "Location": birth_time.geolocation.location_name,
            "Time": birth_time.url_time_string(),
        }
        return cls._make_request(endpoint, params)
