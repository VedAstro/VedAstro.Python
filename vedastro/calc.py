from VedAstro.Library import GeoLocation, Time


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


def set_birthtime(date: str, time: str, time_offset: str, geolocation: GeoLocation) -> Time:
    """
    Create a Time object with the provided date, time, time_offset, and geolocation.

    Args:
        date (str): The date of the birthtime. (ex - 10/05/2023)
        time (str): The time of the birthtime. (ex - 06:42)
        time_offset (str): The time offset of the birthtime. (ex - +08:00)
        geolocation (GeoLocation): The geolocation of the birthtime.

    Returns:
        Time: An instance of the Time class representing the birthtime.

    Raises:
        TypeError: If the input types are not as expected.
            - If date is not a string.
            - If time is not a string.
            - If time_offset is not a string.
            - If geolocation is not a GeoLocation object.
    """
    if not isinstance(date, str):
        raise TypeError("Date must be a string")
    if not isinstance(time, str):
        raise TypeError("Time must be a string")
    if not isinstance(time_offset, str):
        raise TypeError("Time offset must be a string")
    if not isinstance(geolocation, GeoLocation):
        raise TypeError("Geolocation must be a GeoLocation object")
    combined_time = time + " " + date + " " + time_offset
    birthtime = Time(combined_time, geolocation)
    return birthtime
