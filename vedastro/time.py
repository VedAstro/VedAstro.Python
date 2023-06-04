import VedAstro.Library as libray

from vedastro.datetime_offset import DateTimeOffset
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
        self.time_object = libray.Time(date, time, location)

    def add_years(self, years: int):
        """
    Adds the specified number of years to the current DateTime object.

    Args:
        years (int): The number of years to add.

    Returns:
        DateTime: The DateTime object after adding the specified number of years.

    Raises:
        TypeError: If years is not an integer.
    """
        if not isinstance(years, int):
            raise TypeError("Years must be an integer")
        return self.time_object.AddYears(years)

    def subtract_hours(self, granularity_hours: float):
        """
    Subtracts the specified number of hours from the current DateTime object.

    Args:
        granularity_hours (float): The number of hours to subtract.

    Returns:
        DateTime: The DateTime object after subtracting the specified number of hours.

    Raises:
        TypeError: If granularity_hours is not a float.
    """
        if not isinstance(granularity_hours, float):
            raise TypeError("Granularity hours must be a float")
        return self.time_object.SubtractHours(granularity_hours)

    def get_lmt_date_time_offset(self) -> DateTimeOffset:
        """
    Retrieves the Local Mean Time (LMT) DateTimeOffset.

    Returns:
        DateTimeOffset: The Local Mean Time DateTimeOffset.
    """
        return self.time_object.GetLmtDateTimeOffset()

    def get_std_date_time_offset_text(self) -> str:
        """
    Retrieves the Standard DateTimeOffset as a string.

    Returns:
        str: The Standard DateTimeOffset as a string.
    """
        return self.time_object.GetStdDateTimeOffsetText()

    def get_std_date_time_offset(self) -> DateTimeOffset:
        """
    Retrieves the Standard DateTimeOffset.

    Returns:
        DateTimeOffset: The Standard DateTimeOffset.
    """
        return self.time_object.GetStdDateTimeOffset()
    @staticmethod
    def date_time_format_info(self):
        """
  Retrieves the DateTimeFormatInfo object.

  Returns:
      DateTimeFormatInfo: The DateTimeFormatInfo object.
  """

        return self.time_object.GetDateTimeFormatInfo()
