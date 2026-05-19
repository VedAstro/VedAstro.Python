"""
DEMO: Transit Analysis (Gochar)
USE CASE: Compare current planetary positions to birth chart for predictions
DIFFICULTY: Intermediate

WHAT YOU'LL LEARN:
- What transits (Gochar) are and why they matter
- How to calculate current transits relative to birth chart
- How to interpret transit effects
- Which transits are most important
- How to predict timing of events

PREREQUISITES:
- pip install vedastro

RUN:
python demo_transit_analysis.py

EXPECTED OUTPUT:
🌟 Transit Analysis for 25 October 1992
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Current Transits vs Birth Chart:

Transit Sun in Taurus → Transiting 5th house (Romance, creativity)
Transit Moon in Sagittarius → Transiting 12th house (Spirituality, expenses)
...
"""

from vedastro import *
from datetime import datetime

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

print("🌟 Transit Analysis (Gochar)\n")
print("━" * 60)

# Step 2: Define Birth Chart
birth_time = "14:30 25/10/1992 +05:30"
birth_location = GeoLocation("Mumbai", 72.8777, 19.0760)
birth = Time(birth_time, birth_location)

# Step 3: Get Current Moment
now = datetime.now()
current_time = Time(
    hour=now.hour,
    minute=now.minute,
    day=now.day,
    month=now.month,
    year=now.year,
    offset="+05:30",  # IST timezone
    geolocation=birth_location  # Use same location as birth for comparison
)

# UNDERSTANDING TRANSITS
print("📚 What Are Transits (Gochar)?\n")

print("""
DEFINITION:
Transits are the current positions of planets in the sky compared
to your birth chart positions.

ANALOGY:
- Birth chart = Your home's layout (permanent)
- Transits = Visitors moving through your home (temporary)

WHY THEY MATTER:
1. Timing of events - When will something happen?
2. Current influences - What energies are active now?
3. Opportunities - When to start new ventures?
4. Challenges - When to be cautious?

TRANSIT SPEED (How long each planet stays in a sign):
- Moon: 2.5 days (fastest - daily changes)
- Sun: 30 days (monthly changes)
- Mercury: 3 weeks to 2 months
- Venus: 4 weeks to 5 months
- Mars: 6 weeks to 7 months
- Jupiter: 1 year (major yearly influence)
- Saturn: 2.5 years (major long-term influence)
- Rahu/Ketu: 1.5 years (karmic cycles)

MOST IMPORTANT TRANSITS:
1. Saturn (Shani) - Tests, delays, discipline
2. Jupiter (Guru) - Growth, expansion, wisdom
3. Rahu/Ketu - Karmic events, sudden changes
4. Mars (Mangal) - Energy, conflicts, action
5. Sun/Moon - Daily/monthly rhythms
""")

# Step 4: Compare Birth vs Transit Positions
print("\n━" * 60)
print(f"Transit Analysis for {now.strftime('%d %B %Y')}")
print("━" * 60)

# Get birth chart ascendant
birth_ascendant = Calculate.HouseSignName(HouseName.House1, birth)
print(f"\n📊 Birth Chart Ascendant: {birth_ascendant}")
print(f"📍 Location: {birth_location.Name()}\n")

# All 9 planets
planets = [
    PlanetName.Sun,
    PlanetName.Moon,
    PlanetName.Mars,
    PlanetName.Mercury,
    PlanetName.Jupiter,
    PlanetName.Venus,
    PlanetName.Saturn,
    PlanetName.Rahu,
    PlanetName.Ketu,
]

print("🪐 Current Transits vs Birth Chart:\n")
print(f"{'Planet':<10} {'Birth Sign':<12} {'Transit Sign':<12} {'House':<8} {'Interpretation'}")
print("─" * 90)

for planet in planets:
    # Get birth position
    birth_sign = Calculate.PlanetSignName(planet, birth)

    # Get current transit position
    transit_sign = Calculate.PlanetSignName(planet, current_time)

    # Get which house the planet is transiting relative to birth chart
    # Note: This requires calculating which house the current sign falls in
    # For now, we'll just show the signs
    transit_house = Calculate.PlanetHouseName(planet, current_time)

    # Determine if retrograde
    try:
        is_retrograde = Calculate.IsPlanetRetrograde(planet, current_time)
        retro_mark = " (R)" if is_retrograde else ""
    except:
        retro_mark = ""

    # Simple interpretation based on house
    house_num = int(transit_house.replace("House", ""))
    house_meanings = {
        1: "Self, body, personality",
        2: "Wealth, family, speech",
        3: "Siblings, courage, communication",
        4: "Home, mother, happiness",
        5: "Romance, children, creativity",
        6: "Enemies, health, service",
        7: "Marriage, partnerships",
        8: "Transformation, obstacles",
        9: "Luck, dharma, father",
        10: "Career, status, reputation",
        11: "Gains, friends, wishes",
        12: "Losses, spirituality, expenses"
    }

    interpretation = house_meanings.get(house_num, "")

    print(f"{str(planet):<10} {birth_sign:<12} {transit_sign:<12}{retro_mark} {transit_house:<8} {interpretation}")

# Step 5: Major Transit Analysis
print("\n━" * 60)
print("⭐ Major Transits (Most Important)")
print("━" * 60)

# Focus on slow-moving planets (Jupiter, Saturn, Rahu, Ketu)
major_planets = [
    ("Jupiter", PlanetName.Jupiter, "Growth, wisdom, expansion"),
    ("Saturn", PlanetName.Saturn, "Tests, discipline, delay"),
    ("Rahu", PlanetName.Rahu, "Desires, obsession, sudden events"),
    ("Ketu", PlanetName.Ketu, "Detachment, spirituality, loss"),
]

print("\nThese transits last longest and have the deepest impact:\n")

for name, planet, meaning in major_planets:
    birth_sign = Calculate.PlanetSignName(planet, birth)
    transit_sign = Calculate.PlanetSignName(planet, current_time)
    transit_house = Calculate.PlanetHouseName(planet, current_time)

    print(f"🪐 {name}")
    print(f"   Birth: {birth_sign}")
    print(f"   Transit: {transit_sign} in {transit_house}")
    print(f"   Meaning: {meaning}")

    # Special transit checks
    if name == "Saturn":
        # Sade Sati check (Saturn in 12th, 1st, or 2nd from Moon)
        birth_moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth)
        print(f"   Note: Check if in Sade Sati relative to Moon ({birth_moon_sign})")

    if name == "Jupiter":
        # Jupiter return (back to birth sign)
        if birth_sign == transit_sign:
            print(f"   🌟 Jupiter Return! Major 12-year cycle completion")

    print()

# Step 6: Analyze Specific Transits
print("━" * 60)
print("🔍 Detailed Transit Interpretations")
print("━" * 60)

# Get Jupiter transit house
jupiter_house = Calculate.PlanetHouseName(PlanetName.Jupiter, current_time)
jupiter_house_num = int(jupiter_house.replace("House", ""))

print(f"\n💫 Jupiter Transit (Current Growth Area):\n")
print(f"   Transiting {jupiter_house}")

jupiter_interpretations = {
    1: "Focus on self-improvement, new beginnings, personal growth",
    2: "Financial gains, family expansion, value accumulation",
    3: "Communication skills, sibling relationships, courage",
    4: "Home purchase, mother's wellbeing, inner peace",
    5: "Romance, children, creative projects, education",
    6: "Health improvements, defeating enemies, service work",
    7: "Marriage, partnerships, business collaborations",
    8: "Research, occult studies, inheritance, transformation",
    9: "Higher education, spiritual growth, foreign travel, father",
    10: "Career advancement, recognition, status elevation",
    11: "Wish fulfillment, income increase, new friendships",
    12: "Spiritual practices, foreign settlement, charitable work"
}

print(f"   {jupiter_interpretations.get(jupiter_house_num, 'General expansion')}\n")

# Get Saturn transit house
saturn_house = Calculate.PlanetHouseName(PlanetName.Saturn, current_time)
saturn_house_num = int(saturn_house.replace("House", ""))

print(f"⚖️  Saturn Transit (Current Challenge Area):\n")
print(f"   Transiting {saturn_house}")

saturn_interpretations = {
    1: "Focus on health, discipline, self-control, may feel restricted",
    2: "Financial constraints, family responsibilities, speech issues",
    3: "Sibling challenges, communication blocks, courage tests",
    4: "Home issues, mother's health, emotional challenges",
    5: "Delays in romance, children's issues, creative blocks",
    6: "Health problems, enemy issues, service challenges (but Saturn strong here!)",
    7: "Marriage tests, partnership delays, relationship maturity",
    8: "Major life changes, obstacles, but also transformation",
    9: "Faith tests, father issues, dharma challenges",
    10: "Career pressure, hard work, but potential for lasting success",
    11: "Delayed gains, friend issues, but building solid networks",
    12: "Expenses, isolation, but spiritual growth, foreign opportunities"
}

print(f"   {saturn_interpretations.get(saturn_house_num, 'General challenges')}\n")

# Step 7: Transit Aspects (Which planets are aspecting birth planets)
print("━" * 60)
print("👁️  Transit Aspects (Drishti)")
print("━" * 60)

print("""
Aspects are when transiting planets "look at" or influence positions
in your birth chart.

IMPORTANT ASPECTS:
- Jupiter aspects: 5th, 7th, 9th from its position (benefic)
- Saturn aspects: 3rd, 7th, 10th from its position (malefic)
- Mars aspects: 4th, 7th, 8th from its position (malefic)
- Rahu/Ketu always aspect each other (opposite signs)

Example: If transit Saturn is in Aries, it aspects:
- 3rd from Aries = Gemini
- 7th from Aries = Libra
- 10th from Aries = Capricorn

Use these to check which birth chart planets are being influenced.
""")

# Step 8: Dasha + Transit Combination
print("\n━" * 60)
print("⏰ Timing Events: Dasha + Transit Combination")
print("━" * 60)

print("""
IMPORTANT PRINCIPLE:
Events happen when Dasha period + Transit align.

Example:
- Running Jupiter Mahadasa + Jupiter transit to 10th house
  = Strong career advancement opportunity

- Running Saturn Mahadasa + Saturn transit to 7th house
  = Delay in marriage, or marriage with responsibility

HOW TO USE:
1. Check current Mahadasa: Calculate.CurrentDasa()
2. Check current transits (as above)
3. Where they align, events manifest
4. Where they conflict, challenges arise

Next Step: Use demo_vimshottari_dasa.py to get your current dasha
""")

# PRACTICAL APPLICATIONS
print("\n━" * 60)
print("💡 Practical Applications")
print("━" * 60)

print("""
1. DAILY PLANNING
   - Check Moon transit (changes every 2.5 days)
   - Favorable Moon transits = good for that house matters
   - Example: Moon in 10th = good day for career moves

2. MONTHLY PLANNING
   - Check Sun transit (changes monthly)
   - Start projects when Sun transits favorable houses
   - Example: Sun in 11th = good month for networking

3. YEARLY PLANNING
   - Check Jupiter transit (changes yearly)
   - Major growth in the house Jupiter transits
   - Example: Jupiter in 4th = year to buy property

4. LONG-TERM PLANNING
   - Check Saturn transit (changes every 2.5 years)
   - Be patient in areas Saturn transits
   - Example: Saturn in 7th = delay marriage or work harder

5. MUHURTHA (TIMING)
   - Avoid major decisions when malefics transit 8th house
   - Start ventures when benefics transit 1st, 5th, 9th, 11th
   - Check retrograde planets (weaker or internalized energy)
""")

# NEXT STEPS
print("\n━" * 60)
print("Next Steps")
print("━" * 60)

print("""
1. Calculate your current Dasha: demo_vimshottari_dasa.py
2. Combine Dasha + Transit for accurate timing
3. Track slow planets (Saturn, Jupiter, Rahu, Ketu)
4. Use Ashtakvarga for transit strength: Calculate.SarvaAshtakvarga()
5. Check daily Moon transits for day-to-day planning
6. Study Vedha (obstructing transits) for advanced analysis
7. Learn about transit yogas (combinations) for specific events

Advanced: Calculate.EventsAtTime() - Get transit predictions directly!
""")

# BONUS: Quick Transit Checker Function
print("\n━" * 60)
print("🔧 Bonus: Quick Transit Checker Function")
print("━" * 60)

def check_favorable_transits(birth_chart_time, current_time_obj):
    """Quick check if current transits are favorable"""

    # Get Jupiter and Saturn transits
    jupiter_house = Calculate.PlanetHouseName(PlanetName.Jupiter, current_time_obj)
    saturn_house = Calculate.PlanetHouseName(PlanetName.Saturn, current_time_obj)

    jupiter_num = int(jupiter_house.replace("House", ""))
    saturn_num = int(saturn_house.replace("House", ""))

    # Favorable houses: 1, 5, 9, 11 (trines and gains)
    favorable_houses = [1, 5, 9, 11]

    # Challenging houses: 6, 8, 12
    challenging_houses = [6, 8, 12]

    score = 0

    if jupiter_num in favorable_houses:
        score += 2
        print(f"✅ Jupiter in {jupiter_house} (favorable)")
    elif jupiter_num in challenging_houses:
        score -= 1
        print(f"⚠️  Jupiter in {jupiter_house} (challenging)")

    if saturn_num in favorable_houses:
        score += 1
        print(f"✅ Saturn in {saturn_house} (favorable - rare!)")
    elif saturn_num in challenging_houses:
        score -= 2
        print(f"⚠️  Saturn in {saturn_house} (challenging)")

    print(f"\nOverall Transit Score: {score}")
    if score > 0:
        print("🌟 Favorable period overall - good time for action")
    elif score < 0:
        print("🛡️  Challenging period - focus on patience and perseverance")
    else:
        print("⚖️  Neutral period - mixed results")

print("\nChecking current transits:\n")
check_favorable_transits(birth, current_time)

print("\n✨ Transit analysis complete!")
print("\n💡 Pro Tip: Run this script daily/weekly to track changing transits")
print("   and time your important decisions accordingly!")
