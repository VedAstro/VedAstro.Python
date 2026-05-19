"""
DEMO: Daily Panchanga Calculator
USE CASE: Get today's Tithi, Nakshatra, Yoga, and Karana for any location
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- What is Panchanga (5 limbs of time)
- How to get Tithi (lunar day)
- How to get Nakshatra (lunar mansion)
- How to get Yoga (Sun-Moon angle combination)
- How to get Karana (half of Tithi)
- Why Panchanga matters in Vedic astrology

PREREQUISITES:
- pip install vedastro

RUN:
python demo_daily_panchanga.py

EXPECTED OUTPUT:
📅 Daily Panchanga for 18 May 2026
📍 Location: Mumbai, India

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌙 Tithi (Lunar Day):      Shukla Dwadashi
⭐ Nakshatra (Lunar Mansion): Pushya
🔗 Yoga:                    Ganda
⚡ Karana:                  Vishti
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Use for: Muhurtha (auspicious timing), daily guidance, spiritual practices
"""

from vedastro import *
from datetime import datetime

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Get Current Date and Time
now = datetime.now()

# Step 3: Define Location
# Panchanga is location-specific because it's based on local sunrise
location_name = "Mumbai"
longitude = 72.8777
latitude = 19.0760
location = GeoLocation(location_name, longitude, latitude)

# Step 4: Create Time Object for Today
# Use current moment for most accurate panchanga
today = Time(
    hour=now.hour,
    minute=now.minute,
    day=now.day,
    month=now.month,
    year=now.year,
    offset="+05:30",  # IST = UTC+5:30 (adjust for your timezone)
    geolocation=location
)

# Step 5: Calculate the 5 Limbs of Panchanga
# Panchanga = Pancha (five) + Anga (limbs)

# 1. TITHI - Lunar Day (1-30, divided into Shukla Paksha & Krishna Paksha)
#    Measures Moon's angle from Sun (0° to 360° in 30 steps)
#    Important for: Festivals, fasting, ceremonies
tithi = Calculate.LunarDay(today)

# 2. NAKSHATRA - Lunar Mansion (1 of 27 constellations)
#    The constellation where Moon is currently placed
#    Important for: Naming ceremonies, compatibility, spiritual practices
nakshatra = Calculate.MoonConstellation(today)

# 3. YOGA - Sun-Moon Angle Combination (1 of 27 yogas)
#    Sum of Sun and Moon longitudes divided into 27 parts
#    Important for: Daily predictions, auspiciousness
yoga = Calculate.Yoga(today)

# 4. KARANA - Half of Tithi (1 of 11 karanas, repeated twice per Tithi)
#    Important for: Timing of actions, muhurtha
karana = Calculate.Karana(today)

# 5. VARA - Day of Week (derived from datetime, not calculated separately)
#    Each day ruled by a planet: Sun=Sunday, Moon=Monday, etc.
vara = now.strftime('%A')  # e.g., "Monday"

# Step 6: Display Panchanga
print(f"📅 Daily Panchanga for {now.strftime('%d %B %Y')}")
print(f"📍 Location: {location_name}, India\n")
print("━" * 50)

# Display the 5 elements
print(f"🌙 Tithi (Lunar Day):         {tithi}")
print(f"⭐ Nakshatra (Lunar Mansion):  {nakshatra}")
print(f"🔗 Yoga:                       {yoga}")
print(f"⚡ Karana:                     {karana}")
print(f"📆 Vara (Weekday):             {vara}")

print("━" * 50)

# WHAT IS PANCHANGA USED FOR?
print("\n💡 Uses of Panchanga:\n")
print("✅ Muhurtha (auspicious timing) - Choose best time for important events")
print("✅ Festival calculation - Many festivals tied to specific Tithis")
print("✅ Fasting - Ekadashi (11th Tithi) is a fasting day")
print("✅ Spiritual practices - Certain nakshatras favor specific practices")
print("✅ Daily guidance - Avoid inauspicious combinations")

# AUSPICIOUSNESS GUIDE
print("\n🎯 Quick Auspiciousness Guide:\n")

# Good Tithis for starting ventures
good_tithis = ["Pratipada", "Tritiya", "Panchami", "Saptami", "Dashami", "Ekadashi", "Trayodashi"]
print("🌟 Auspicious Tithis: " + ", ".join(good_tithis))

# Good Nakshatras
good_nakshatras = ["Ashwini", "Rohini", "Mrigashira", "Pushya", "Hasta", "Anuradha", "Shravana", "Uttara"]
print("⭐ Auspicious Nakshatras: " + ", ".join(good_nakshatras))

# Check if today is auspicious
if tithi.split()[1] in good_tithis:  # Split to handle "Shukla Pratipada" format
    print(f"\n✨ Today's Tithi ({tithi}) is generally auspicious!")

if nakshatra in good_nakshatras:
    print(f"✨ Today's Nakshatra ({nakshatra}) is favorable!")

# NEXT STEPS:
# - Build a panchanga calendar for the whole month
# - Add sunrise/sunset times: Calculate.SunriseTime(), Calculate.SunsetTime()
# - Get Rahu Kaal (inauspicious time): Calculate.RahuKaal()
# - Find best muhurtha: demo_muhurtha_finder.py
# - Create a daily panchanga email/SMS service

# BONUS: Additional Panchanga Elements
print("\n📊 Additional Timing Elements:\n")

# Paksha (Lunar Fortnight) - Derived from Tithi
if "Shukla" in tithi:
    paksha = "Shukla Paksha (Waxing Moon - Bright Fortnight)"
elif "Krishna" in tithi:
    paksha = "Krishna Paksha (Waning Moon - Dark Fortnight)"
else:
    paksha = "New Moon (Amavasya) or Full Moon (Purnima)"

print(f"🌓 Paksha: {paksha}")

# Moon Phase - Approximate from Tithi
tithi_parts = tithi.split()
if len(tithi_parts) > 1:
    tithi_name = tithi_parts[1]
    tithi_to_phase = {
        "Pratipada": "🌑 New Moon",
        "Dwitiya": "🌒 Waxing Crescent",
        "Tritiya": "🌒 Waxing Crescent",
        "Chaturthi": "🌓 Waxing Crescent",
        "Panchami": "🌓 First Quarter",
        "Shashthi": "🌔 Waxing Gibbous",
        "Saptami": "🌔 Waxing Gibbous",
        "Ashtami": "🌔 Waxing Gibbous",
        "Navami": "🌕 Nearly Full",
        "Dashami": "🌕 Nearly Full",
        "Ekadashi": "🌕 Nearly Full",
        "Dwadashi": "🌕 Full Moon",
        "Trayodashi": "🌖 Waning Gibbous",
        "Chaturdashi": "🌖 Waning Gibbous",
    }
    moon_phase = tithi_to_phase.get(tithi_name, "🌙 Moon")
    print(f"🌙 Moon Phase: {moon_phase}")

# UNDERSTANDING EACH ELEMENT:
print("\n📚 Panchanga Elements Explained:\n")

print("1️⃣ TITHI (Lunar Day)")
print("   - 30 tithis per lunar month (15 Shukla + 15 Krishna)")
print("   - Shukla Paksha = Waxing moon (after New Moon)")
print("   - Krishna Paksha = Waning moon (after Full Moon)")
print("   - Important tithis: Amavasya (New Moon), Purnima (Full Moon), Ekadashi (11th)")

print("\n2️⃣ NAKSHATRA (Lunar Mansion)")
print("   - 27 nakshatras, each 13°20' of zodiac")
print("   - Moon spends ~1 day in each nakshatra")
print("   - Used for: Naming, marriage matching, muhurtha")

print("\n3️⃣ YOGA")
print("   - 27 yogas based on Sun + Moon longitude")
print("   - Some yogas are auspicious, some inauspicious")
print("   - Important for: Daily activities, travel, starting ventures")

print("\n4️⃣ KARANA")
print("   - 11 karanas, each is half of a tithi (~6 hours)")
print("   - 4 fixed karanas + 7 movable karanas (repeated)")
print("   - Used for: Precise timing of activities")

print("\n5️⃣ VARA (Weekday)")
print("   - Sun=Sunday, Moon=Monday, Mars=Tuesday, Mercury=Wednesday")
print("   - Jupiter=Thursday, Venus=Friday, Saturn=Saturday")
print("   - Each day has different qualities and ruling planets")

# CUSTOMIZATION IDEAS:
# 1. Create a website widget showing today's panchanga
# 2. Build a mobile app with push notifications
# 3. Generate monthly panchanga calendar PDF
# 4. Add regional language support (Hindi, Tamil, Telugu, etc.)
# 5. Integrate with Google Calendar for festival reminders

# COMMON QUESTIONS:
# Q: Why does panchanga vary by location?
# A: Because it's based on local sunrise, which varies by longitude/latitude
#
# Q: What if I'm in a Western country?
# A: Panchanga still works! Just use your local coordinates and timezone
#
# Q: Which Tithi system is correct?
# A: There are 2 systems - Amanta (month ends on New Moon) and Purnimanta
#    (month ends on Full Moon). This library uses the standard system.
#
# Q: Can I get panchanga for a specific time/place?
# A: Yes! Just change the `today` Time object to any date/time/location
