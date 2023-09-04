import VedAstro.Library as VedAstro

from vedastro.objects.datetime_offset import DateTimeOffset


class Time:
    """
    Create a Time object with the provided date, time, time_offset, and geolocation.

    Args:
        date (str): The date. (ex - 10/05/2023)
        time (str): The time. (ex - 06:42)
        time_offset (str): The time offset. (ex - +08:00)
        geolocation (GeoLocation): The geolocation object you got by get_geolocation.

    Returns:
        Time: An instance of the VedAstro Time class representing the time.

    Raises:
        TypeError: If the input types are not as expected.
            - If date is not a string.
            - If time is not a string.
            - If time_offset is not a string.
            - If geolocation is not a GeoLocation object.
    """

    def __init__(self, date: str, time: str, time_offset: str, geolocation: VedAstro.GeoLocation):

        if not isinstance(date, str):
            raise TypeError("Date must be a string")
        if not isinstance(time, str):
            raise TypeError("Time must be a string")
        if not isinstance(time_offset, str):
            raise TypeError("Time offset must be a string")
        if not isinstance(geolocation, VedAstro.GeoLocation):
            raise TypeError("Geolocation must be a GeoLocation object")

        self.date = date
        self.time = time
        self.geolocation = geolocation
        self.time_offset = time_offset
        combined_time = time + " " + date + " " + time_offset
        self.time_object = VedAstro.Time(combined_time, geolocation)

    def get_time(self):
        return self.time_object

    def AddYears(self, years: int):

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
        # Can't call AddYears() because we need Time object
        # new_year = int(self.date.split("/")[-1])+years
        # new_date = self.date.replace(self.date.split("/")[-1], str(new_year))
        # new_time = Time(new_date, self.time, self.time_offset, self.geolocation)
        return self.time_object.AddYears(years)

    def AddHours(self, granularity_hours: float):
        """
    Adds the specified number of hours to the current DateTime object.

    Args:
        granularity_hours (float): The number of hours to add.    """
        if not isinstance(granularity_hours, float):
            try:
                granularity_hours = float(granularity_hours)
            except ValueError:
                raise TypeError("Granularity hours must be a float")
        return self.time_object.AddHours(granularity_hours)

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

    def __sub__(self, other):
        """
        Subtracts the specified Time.

        :param other:Time object:
        :return:
        """
        return self.time_object.Subtract(other)

    #
    def get_std_date_time_offset(self) -> DateTimeOffset:
        """
    Retrieves the Standard DateTimeOffset.

    Returns:
        DateTimeOffset: The Standard DateTimeOffset.
    """
        return self.time_object.GetStdDateTimeOffset()

    def get_geolocation(self):
        """
        return: geolocation object
        """""
        return self.time_object.GetGeoLocation()

    def get_lmt_date_time_offset_text(self) -> str:
        """
        return:
        """""
        return self.time_object.GetLmtDateTimeOffsetText()

    def to_xml(self):
        # Todo: test this method thoroughly
        """
        create xml object
        """""
        self.time_object.ToXml()

    def to_json(self):
        # Todo: test this method thoroughly
        """
        create json object
        """""
        self.time_object.ToJson()

    # public static Time Now(GeoLocation geoLocation)
    # public int GetStdYear() => this.GetStdDateTimeOffset().Year;
    # public int GetStdMonth() => this.GetStdDateTimeOffset().Month;
    # public int GetStdDate() => this.GetStdDateTimeOffset().Day;
    # public int GetStdHour() => this.GetStdDateTimeOffset().Hour;
    def get_std_year(self):
        """
        return std year
        """""
        return self.time_object.GetStdYear()

    def get_std_month(self):
        """
        return std month
        """""
        return self.time_object.GetStdMonth()

    def get_std_date(self):
        """
        return std date
        """""
        return self.time_object.GetStdDate()

    def get_std_hour(self):
        """
        return std hour
        """""
        return self.time_object.GetStdHour()

    @staticmethod
    def now(location: VedAstro.GeoLocation):
        """
        return: current time of the chosen geolocation
        """""
        return VedAstro.Time.Now(location)

    @staticmethod
    def date_time_format_info(self):
        """
  Retrieves the DateTimeFormatInfo object.

  Returns:
      DateTimeFormatInfo: The DateTimeFormatInfo object.
  """

        return self.time_object.GetDateTimeFormatInfo()


"""
these methods need to implement later
public dynamic FromXml<T>
public static Time FromXml
public static Time FromJson
public static List<Time> FromXml
"""
