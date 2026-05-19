"""
DEMO: Birth Chart Basics - The Big Three
USE CASE: Get Sun, Moon, and Ascendant signs for any birth chart
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- How to get Sun sign (your core identity)
- How to get Moon sign (your emotional nature)
- How to get Ascendant/Rising sign (your outer personality)
- How these three form the foundation of a birth chart

PREREQUISITES:
- pip install vedastro

RUN:
python demo_birth_chart_basics.py

EXPECTED OUTPUT:
🌟 Birth Chart Basics for 25 October 1992, 14:30 IST, Mumbai

☀️  Sun Sign: Libra
    (Your core identity, ego, and life purpose)

🌙  Moon Sign: Scorpio
    (Your emotions, instincts, and inner world)

⬆️  Ascendant (Rising): Capricorn
    (Your outer personality and how others see you)

These three signs form the foundation of your birth chart!
"""

from vedastro import *

# Step 1: Set API Key
# Free tier: 'FreeAPIUser' (5 requests/minute)
# Premium: Get key from vedastro.org/API.html ($1/month unlimited)
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Birth Details
# IMPORTANT: Use the correct format "HH:MM DD/MM/YYYY +TZ:TZ"
birth_time_str = "14:30 25/10/1992 +05:30"  # 2:30 PM IST on 25 Oct 1992
location_name = "Mumbai"
longitude = 72.8777  # East is positive, West is negative
latitude = 19.0760   # North is positive, South is negative

# Create location object
location = GeoLocation(location_name, longitude, latitude)

# Create time object
birth_time = Time(birth_time_str, location)

# Step 3: Calculate The Big Three
# The Sun Sign - Your core identity, ego, conscious self
sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth_time)

# The Moon Sign - Your emotions, instincts, subconscious
moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth_time)

# The Ascendant (Rising Sign) - Your outer personality, how others see you
# In Vedic astrology, House 1 = Ascendant
ascendant = Calculate.HouseSignName(HouseName.House1, birth_time)

# Step 4: Display Results
print(f"🌟 Birth Chart Basics for {birth_time_str} {location_name}\n")

print(f"☀️  Sun Sign: {sun_sign}")
print(f"    (Your core identity, ego, and life purpose)\n")

print(f"🌙  Moon Sign: {moon_sign}")
print(f"    (Your emotions, instincts, and inner world)\n")

print(f"⬆️  Ascendant (Rising): {ascendant}")
print(f"    (Your outer personality and how others see you)\n")

print("These three signs form the foundation of your birth chart!")

# NEXT STEPS:
# - Try changing birth_time_str to your own birth date and time
# - Get more planet positions: demo_all_planet_data.py
# - Get full horoscope predictions: Calculate.HoroscopePredictions(birth_time)
# - Learn about Nakshatras: Calculate.MoonConstellation(birth_time)

# BONUS: Get constellation (Nakshatra) for Moon
moon_nakshatra = Calculate.MoonConstellation(birth_time)
print(f"\n🌟 Bonus: Moon Nakshatra: {moon_nakshatra}")
print(f"   (The lunar mansion where your Moon is placed)")

# EXPLANATION OF THE BIG THREE:
# 1. Sun Sign - What motivates you, your ego, your life's purpose
#    Example: Libra = seeks balance, harmony, relationships
#
# 2. Moon Sign - Your emotional world, how you feel and react
#    Example: Scorpio = intense emotions, deep feelings, transformative
#
# 3. Ascendant - How you appear to others, your mask, physical body
#    Example: Capricorn = serious demeanor, disciplined appearance, mature look

# COMMON QUESTIONS:
# Q: Why is my Sun sign different in Vedic vs Western astrology?
# A: Vedic uses sidereal zodiac (actual star positions), Western uses tropical
#    (fixed to seasons). Difference is about 24 degrees, shifting most signs back one.
#
# Q: Which one is "correct"?
# A: Both systems are valid. Vedic is astronomical (actual stars), Western is
#    seasonal (equinox-based). Choose based on which resonates with you.
#
# Q: Can I change the ayanamsa (zodiac calculation method)?
# A: Yes! Use Calculate.SetAyanamsa(Ayanamsa.Lahiri) before calculations
#    See demo_custom_ayanamsa.py for details
