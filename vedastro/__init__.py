# VedAstro Python Library - REST API Mode
# https://vedastro.org

import sys

# Plain ASCII on purpose: a banner with box-drawing characters or emoji raises
# UnicodeEncodeError on Windows consoles that use a legacy code page (cp1252).
if sys.stdout is not None:  # pythonw.exe and some embedded hosts have no stdout
    print("VedAstro : Easy To Use Advanced Astrology Engine")

from .update_check import check_for_update
check_for_update("vedastro")

__all__ = [
    'Calculate', 'GeoLocation', 'Time', 'PlanetName', 'HouseName', 'ZodiacName',
    'ChartType', 'DayOfWeek', 'ConstellationName', 'Avasta', 'Ayanamsa',
    'Karana', 'LunarDayGroup', 'LunarMonth', 'Tools',
]

# Core API interface
from .calculate import Calculate

# Data classes and enums
from .vedastro import (
    GeoLocation, Time, PlanetName, HouseName, ZodiacName,
    ChartType, DayOfWeek, ConstellationName, Avasta, Ayanamsa,
    Karana, LunarDayGroup, LunarMonth,
)


class Tools:
    """Simple utility class replacing the old C# Tools class."""

    @staticmethod
    def Print(data):
        """Pretty print any data returned from the API."""
        if isinstance(data, dict):
            import json
            print(json.dumps(data, indent=2, default=str))
        elif isinstance(data, list):
            for item in data:
                print(item)
        else:
            print(data)

    @staticmethod
    def AnyToJSON(name, data):
        """Convert API result data to JSON string."""
        import json
        return json.dumps(data, indent=2, default=str)
