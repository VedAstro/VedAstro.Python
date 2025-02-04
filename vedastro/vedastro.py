import requests
import json

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
        url = f"https://api.vedastro.org/api/Calculate/MatchReport/Location/{male_birth_time.geolocation.location_name}/Time/{male_birth_time.time_string}/Location/{female_birth_time.geolocation.location_name}/Time/{female_birth_time.time_string}/APIKey/{cls.api_key}"

        # Make the API request
        response = requests.get(url)

        # Check if the response was successful
        if response.status_code == 200:
            # Parse the JSON response
            data = json.loads(response.text)

            # Return the parsed payload
            return data["Payload"]
        else:
            # Return an error message if the response was not successful
            return "Error: API request failed with status code {}".format(response.status_code)
