"""
DEMO: Quick Start - Your First Vedic Astrology Calculation
USE CASE: Learn the absolute basics in 5 lines of code
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- How to install and import the library
- How to set your API key (free or premium)
- How to define birth time and location
- How to make your first calculation
- How simple VedAstro really is!

PREREQUISITES:
- pip install vedastro

RUN:
python demo_quick_start.py

EXPECTED OUTPUT:
Sun Sign: Libra
"""

# Import everything from VedAstro
# This gives you access to Calculate, Time, GeoLocation, PlanetName, etc.
from vedastro import *

# Step 1: Set API Key
# For free tier: use 'FreeAPIUser' (5 requests per minute)
# For premium tier: get your key from vedastro.org/API.html ($1/month unlimited)
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Birth Time and Location
# Format: "HH:MM DD/MM/YYYY +TZ:TZ"
# HH:MM = Hour:Minute (24-hour format, e.g., 14:30 = 2:30 PM)
# DD/MM/YYYY = Day/Month/Year
# +TZ:TZ = Timezone offset (e.g., +05:30 for India, -05:00 for USA East)
birth_time = Time("14:30 25/10/1992 +05:30",
                  GeoLocation("Mumbai", 72.8777, 19.0760))

# Step 3: Make Your First Calculation
# This gets the zodiac sign where the Sun was at birth
sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth_time)

# Step 4: Display the Result
print(f"Sun Sign: {sun_sign}")

# That's it! You just made your first Vedic astrology calculation! 🎉

# NEXT STEPS:
# - Try changing the birth time to your own birth date
# - Try Calculate.PlanetSignName(PlanetName.Moon, birth_time) for Moon sign
# - Explore more examples: demo_birth_chart_basics.py
# - Read the full README.md for 596+ calculation methods
# - Check the FAQ: FAQ.md for common questions

# COMMON VARIATIONS:
# Get Moon sign:
# moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth_time)

# Get Ascendant (Rising sign):
# ascendant = Calculate.HouseSignName(HouseName.House1, birth_time)

# Get current position of Mars:
# mars_sign = Calculate.PlanetSignName(PlanetName.Mars, birth_time)
