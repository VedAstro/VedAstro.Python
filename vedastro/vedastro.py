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
    Sun = "Sun"
    Moon = "Moon"
    Mars = "Mars"
    Mercury = "Mercury"
    Jupiter = "Jupiter"
    Venus = "Venus"
    Saturn = "Saturn"
    Uranus = "Uranus"
    Neptune = "Neptune"
    Ascendant = "Ascendant"

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

    @classmethod
    def SetAPIKey(cls, api_key):
        cls.api_key = api_key
    
    @classmethod
    def MatchReport(cls, male_birth_time, female_birth_time):
        """
        Calculate the match report for two individuals.

        Args:
        male_birth_time (Time): The birth time of the male.
        female_birth_time (Time): The birth time of the female.

        Returns:
        dict: The match report.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/MatchReport/Location/{male_birth_time.geolocation.location_name}/Time/{male_birth_time.time_string}/Location/{female_birth_time.geolocation.location_name}/Time/{female_birth_time.url_time_string}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def AllPlanetData(cls, planet_name, birth_time):
        """
        Calculate the planet data for an individual.

        Args:
        planet_name (PlanetName): The name of the planet.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The planet data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/AllPlanetData/PlanetName/{planet_name.value}/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def AllHouseData(cls, house_name, birth_time):
        """
        Calculate the house data for an individual.

        Args:
        house_name (HouseName): The name of the house.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The house data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/AllHouseData/HouseName/{house_name.value}/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def HoroscopePredictionNames(cls, birth_time):
        """
        Calculate the zodiac sign data for an individual.

        Args:
        zodiac_name (ZodiacName): The name of the zodiac sign.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The zodiac sign data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/HoroscopePredictionNames/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def HouseZodiacSign(cls, house_name, birth_time):
        """
        Calculate the zodiac sign for a house.

        Args:
        house_name (HouseName): The name of the house.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The zodiac sign data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/HouseZodiacSign/HouseName/{house_name.value}/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def PlanetsInHouse(cls, house_name, birth_time):
        """
        Calculate the planets in a house.

        Args:
        house_name (HouseName): The name of the house.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The planet data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/PlanetsInHouse/HouseName/{house_name.value}/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)

    @classmethod
    def PlanetsInHouseBasedOnSign(cls, house_name, birth_time):
        """
        Calculate the planets in a house based on sign.

        Args:
        house_name (HouseName): The name of the house.
        birth_time (Time): The birth time of the individual.

        Returns:
        dict: The planet data.
        """
        # Format the API URL with the provided parameters
        url = f"https://api.vedastro.org/api/Calculate/PlanetsInHouseBasedOnSign/HouseName/{house_name.value}/Location/{birth_time.geolocation.location_name}/Time/{birth_time.url_time_string()}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Check if the payload exists and is not empty
            if "Payload" in data and data["Payload"]:
                # Return the values in the payload as a list
                return list(data["Payload"].values())[0]
            else:
                # Raise an exception if the payload is missing or empty
                raise ValueError("Payload is missing or empty")
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)
