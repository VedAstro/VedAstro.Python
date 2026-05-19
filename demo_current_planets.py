"""
DEMO: Current Planetary Positions
USE CASE: Get today's planetary positions for any location (transit positions)
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- How to get the current moment's planetary positions
- How to work with datetime for "now"
- How planetary transits (Gochara) work
- How to display positions in a readable format

PREREQUISITES:
- pip install vedastro

RUN:
python demo_current_planets.py

EXPECTED OUTPUT:
🪐 Current Planetary Positions for 18 May 2026, 14:23 UTC

Location: London (51.5074°N, 0.1278°W)

Planet          Sign            Nakshatra
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
☀️  Sun         Taurus          Rohini
🌙  Moon        Sagittarius     Moola
♂️  Mars        Pisces          Revathi
☿️  Mercury     Aries           Bharani
...
"""

from vedastro import *
from datetime import datetime

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Get Current Moment
# datetime.now() gives us the current time on our computer
now = datetime.now()

# Step 3: Define Location
# You can use any location - the planetary positions will be
# calculated for that location's perspective
location_name = "London"
longitude = -0.1278  # West is negative, East is positive
latitude = 51.5074   # North is positive, South is negative
location = GeoLocation(location_name, longitude, latitude)

# Step 4: Create Time Object for Current Moment
# We need to provide the timezone offset
# London is UTC+0:00 (or UTC+1:00 in summer with DST)
current_time = Time(
    hour=now.hour,
    minute=now.minute,
    day=now.day,
    month=now.month,
    year=now.year,
    offset="+00:00",  # Adjust this for your timezone
    geolocation=location
)

# Step 5: Get All 9 Vedic Planets
# In Vedic astrology, we track 9 grahas (celestial bodies):
# - 5 visible planets: Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn
# - 2 shadow planets (lunar nodes): Rahu (North Node), Ketu (South Node)
planets = [
    PlanetName.Sun,
    PlanetName.Moon,
    PlanetName.Mars,
    PlanetName.Mercury,
    PlanetName.Jupiter,
    PlanetName.Venus,
    PlanetName.Saturn,
    PlanetName.Rahu,    # North Node of Moon
    PlanetName.Ketu,    # South Node of Moon
]

# Step 6: Display Header
print(f"🪐 Current Planetary Positions for {now.strftime('%d %B %Y, %H:%M')} UTC\n")
print(f"Location: {location_name} ({latitude}°N, {abs(longitude)}°W)\n")

# Create a nice formatted table
print(f"{'Planet':<15} {'Sign':<15} {'Nakshatra':<15}")
print("━" * 50)

# Step 7: Get and Display Each Planet's Position
for planet in planets:
    # Get zodiac sign (12 signs: Aries, Taurus, Gemini, etc.)
    sign = Calculate.PlanetSignName(planet, current_time)

    # Get nakshatra (27 lunar mansions)
    nakshatra = Calculate.PlanetConstellation(planet, current_time)

    # Get emoji for each planet
    planet_emoji = {
        'Sun': '☀️',
        'Moon': '🌙',
        'Mars': '♂️',
        'Mercury': '☿️',
        'Jupiter': '♃',
        'Venus': '♀️',
        'Saturn': '♄',
        'Rahu': '☊',
        'Ketu': '☋'
    }

    emoji = planet_emoji.get(str(planet), '🪐')

    # Display in a nicely formatted row
    print(f"{emoji}  {str(planet):<12} {sign:<15} {nakshatra:<15}")

# BONUS: Check for Retrograde Planets
print("\n🔄 Retrograde Status:\n")

for planet in planets:
    # Rahu and Ketu are always retrograde by nature, so skip them
    if planet in [PlanetName.Rahu, PlanetName.Ketu]:
        continue

    # Check if planet is retrograde (moving backward from Earth's perspective)
    is_retrograde = Calculate.IsPlanetRetrograde(planet, current_time)

    if is_retrograde:
        print(f"  ⚠️  {planet} is retrograde")

# UNDERSTANDING TRANSITS (GOCHARA):
# - Transits are current planetary positions
# - They affect everyone differently based on their birth chart
# - To see how transits affect YOU specifically:
#   1. Get your birth chart
#   2. Compare current planet positions to your birth positions
#   3. See which houses the transiting planets are in relative to your chart
#
# Example: If transit Jupiter is in your 7th house, it's a good time for
# relationships and partnerships.

# NEXT STEPS:
# - Compare these positions to a birth chart: demo_transit_analysis.py
# - Get daily predictions based on transits: Calculate.EventsAtTime()
# - Check auspicious timings: Calculate.LunarDay(), Calculate.Yoga()
# - Build a daily panchanga widget: demo_daily_panchanga.py

# CUSTOMIZATION IDEAS:
# 1. Run this as a daily cron job and email yourself the positions
# 2. Create a web API endpoint that returns current positions
# 3. Add alerts when specific transits occur (e.g., "Jupiter enters Aries!")
# 4. Plot planetary positions on a chart graphic
# 5. Compare today vs yesterday to see planet movements

# BONUS: Get Exact Degrees
print("\n📐 Exact Positions (Degrees):\n")

for planet in [PlanetName.Sun, PlanetName.Moon]:  # Just show Sun & Moon for brevity
    # Get precise degree position (0-360°)
    longitude_deg = Calculate.PlanetNirayanaLongitude(planet, current_time)

    # Get degree within sign (0-30°)
    degree_in_sign = Calculate.PlanetLongitudeInSign(planet, current_time)

    emoji = '☀️' if planet == PlanetName.Sun else '🌙'
    print(f"{emoji}  {planet}:")
    print(f"   Total Longitude: {longitude_deg}°")
    print(f"   Degree in Sign: {degree_in_sign}")

# COMMON QUESTIONS:
# Q: Why are the positions different from Western astrology?
# A: Vedic uses sidereal zodiac (actual star positions), Western uses tropical
#    (fixed to seasons). There's about a 24° difference.
#
# Q: What does "retrograde" mean?
# A: From Earth's perspective, the planet appears to move backward in the sky.
#    Astrologically, it's considered a time to review, revise, and redo matters
#    related to that planet.
#
# Q: How often should I check transits?
# A: Daily for fast-moving planets (Moon, Mercury), weekly for medium (Sun, Venus,
#    Mars), monthly for slow (Jupiter, Saturn, Rahu, Ketu).
