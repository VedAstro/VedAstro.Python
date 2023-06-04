from VedAstro.Library import GeoLocation


def set_geolocation(location: str, longtitude: float, latitude: float):
    """
    Create a GeoLocation object with the provided location, longitude, and latitude.

    Args:
        location (str): The name or description of the location.
        longitude (float): The longitude coordinate of the location.
        latitude (float): The latitude coordinate of the location.

    Returns:
        GeoLocation: An instance of the GeoLocation class representing the geolocation.

    Raises:
        TypeError: If the input types are not as expected.
            - If location is not a string.
            - If longitude is not a float.
            - If latitude is not a float.
    """
    if not isinstance(location, str):
        raise TypeError("Location must be a string")
    if not isinstance(longtitude, float):
        try:
            longtitude = float(longtitude)
        except ValueError:
            raise TypeError("Longtitude must be a float or convertible to a float")
    if not isinstance(latitude, float):
        try:
            latitude = float(latitude)
        except ValueError:
            raise TypeError("Latitude must be a float or convertible to a float")
    geoLocation = GeoLocation(location, longtitude, latitude)
    return geoLocation
