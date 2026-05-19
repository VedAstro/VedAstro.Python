"""
DEMO: Divisional Charts (Varga Charts)
USE CASE: Get D9 (Navamsa), D10 (Dashamsa), D12 (Dwadashamsa) chart data
DIFFICULTY: Intermediate

WHAT YOU'LL LEARN:
- What divisional charts are and why they matter
- How to calculate D9 (marriage/spouse), D10 (career), D12 (parents)
- How to interpret divisional chart placements
- When to use which divisional chart

PREREQUISITES:
- pip install vedastro
- Basic understanding of houses and signs

RUN:
python demo_divisional_charts.py

EXPECTED OUTPUT:
📊 Divisional Charts Analysis
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

D1 (Rasi) - Main Birth Chart
House 1: Capricorn (Ascendant)
House 2: Aquarius
...

D9 (Navamsa) - Marriage & Spouse
House 1: Aries (Navamsa Ascendant)
...
"""

from vedastro import *

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Birth Details
birth_time = "14:30 25/10/1992 +05:30"
location = GeoLocation("Mumbai", 72.8777, 19.0760)
birth = Time(birth_time, location)

# Step 3: Understanding Divisional Charts
print("📊 Divisional Charts (Vargas) - Explained\n")
print("━" * 60)

print("""
WHAT ARE DIVISIONAL CHARTS?

In Vedic astrology, divisional charts (Vargas) are created by dividing
each zodiac sign into smaller sections, revealing deeper insights into
specific life areas.

Think of it like zooming in on a photograph:
- D1 (Rasi) = The full picture (main birth chart)
- D9, D10, D12, etc. = Zoomed-in views of specific life areas

WHY THEY MATTER:

While D1 shows the overall life picture, divisional charts show:
- Hidden strengths and weaknesses in specific areas
- Karmic patterns and past life influences
- Timing of events with greater precision
- Confirmation of D1 predictions

MOST IMPORTANT DIVISIONAL CHARTS:

D1  (Rasi)        - Main chart, overall life
D2  (Hora)        - Wealth and prosperity
D3  (Drekkana)    - Siblings, courage, communication
D4  (Chaturtamsa) - Property, vehicles, home
D7  (Saptamsa)    - Children and creativity
D9  (Navamsa)     - Marriage, spouse, dharma (MOST IMPORTANT!)
D10 (Dashamsa)    - Career, profession, status
D12 (Dwadashamsa) - Parents, ancestors
D16 (Shodasamsa)  - Comforts, luxuries, vehicles
D20 (Vimsamsa)    - Spirituality, worship
D24 (Chaturvimsamsa) - Education, learning
D30 (Trimsamsa)   - Misfortunes, obstacles
D40 (Khavedamsa)  - Auspicious/inauspicious effects
D45 (Akshavedamsa) - Character, morals
D60 (Shashtyamsa) - Past life karma (MOST DETAILED!)

VedAstro supports all D1-D60 charts!
""")

print("\n━" * 60)
print("D1 - Main Birth Chart (Rasi)")
print("━" * 60)

# Get D1 (main chart) house signs
d1_houses = Calculate.AllHouseRasiSigns(birth)

print("\nHouse Signs in D1:")
for house_num in range(1, 13):
    house_name = f"House{house_num}"
    sign = d1_houses.get(house_name, "Unknown")

    # Special note for ascendant
    if house_num == 1:
        print(f"House {house_num:2}: {sign:<15} ← Ascendant (Lagna)")
    else:
        print(f"House {house_num:2}: {sign:<15}")

# Step 4: D9 - Navamsa Chart (Marriage & Spouse)
print("\n━" * 60)
print("D9 - Navamsa Chart (Marriage & Spouse)")
print("━" * 60)

print("""
PURPOSE: Shows marriage quality, spouse nature, and dharma (life purpose)

IMPORTANCE:
- Called the "Fruit of the Tree" (D1 is the tree, D9 is the fruit)
- If a planet is weak in D1 but strong in D9, it gives results later in life
- Used extensively for marriage compatibility
- Shows spiritual evolution and dharma

HOW IT'S CALCULATED:
Each zodiac sign (30°) is divided into 9 parts (3°20' each)
Example: If Sun is at 15° Libra in D1, it moves to a specific sign in D9
""")

d9_houses = Calculate.AllHouseNavamshaSigns(birth)

print("\nHouse Signs in D9 (Navamsa):")
for house_num in range(1, 13):
    house_name = f"House{house_num}"
    d1_sign = d1_houses.get(house_name, "Unknown")
    d9_sign = d9_houses.get(house_name, "Unknown")

    # Compare with D1
    if d1_sign == d9_sign:
        note = "← Same as D1 (Vargottama - Very Strong!)"
    else:
        note = f"(D1: {d1_sign})"

    if house_num == 1:
        print(f"House {house_num:2}: {d9_sign:<15} ← Navamsa Ascendant {note}")
    else:
        print(f"House {house_num:2}: {d9_sign:<15} {note}")

# Step 5: D10 - Dashamsa Chart (Career & Profession)
print("\n━" * 60)
print("D10 - Dashamsa Chart (Career & Profession)")
print("━" * 60)

print("""
PURPOSE: Shows career, profession, status, and achievements

IMPORTANCE:
- Reveals true career potential and professional success
- Shows authority, power, and social status
- Indicates best career path and timing of promotions
- Used to judge fame and recognition

HOW TO INTERPRET:
- Strong 10th house in D10 = Career success
- Benefics in D10 10th = Positive reputation
- Malefics in D10 10th = Challenges but also determination
- Planets in D10 show career-related traits
""")

d10_houses = Calculate.AllHouseDashamsaSigns(birth)

print("\nHouse Signs in D10 (Dashamsa):")
for house_num in range(1, 13):
    house_name = f"House{house_num}"
    d1_sign = d1_houses.get(house_name, "Unknown")
    d10_sign = d10_houses.get(house_name, "Unknown")

    if house_num == 1:
        print(f"House {house_num:2}: {d10_sign:<15} ← Dashamsa Ascendant")
    elif house_num == 10:
        print(f"House {house_num:2}: {d10_sign:<15} ← Career House (Important!)")
    else:
        print(f"House {house_num:2}: {d10_sign:<15}")

# Step 6: D12 - Dwadashamsa Chart (Parents & Ancestors)
print("\n━" * 60)
print("D12 - Dwadashamsa Chart (Parents & Ancestors)")
print("━" * 60)

print("""
PURPOSE: Shows relationship with parents and ancestral karma

IMPORTANCE:
- Reveals parental influence on your life
- Shows ancestral blessings or curses
- Indicates relationship quality with mother (4th) and father (9th)
- Used for ancestral remedies (Pitru Dosha, etc.)

HOW TO INTERPRET:
- 4th house in D12 = Mother's influence
- 9th house in D12 = Father's influence
- Benefics = Good parental support
- Malefics = Challenges but lessons learned
""")

d12_houses = Calculate.AllHouseDwadashamsaSigns(birth)

print("\nHouse Signs in D12 (Dwadashamsa):")
for house_num in range(1, 13):
    house_name = f"House{house_num}"
    d12_sign = d12_houses.get(house_name, "Unknown")

    if house_num == 1:
        print(f"House {house_num:2}: {d12_sign:<15} ← Dwadashamsa Ascendant")
    elif house_num == 4:
        print(f"House {house_num:2}: {d12_sign:<15} ← Mother")
    elif house_num == 9:
        print(f"House {house_num:2}: {d12_sign:<15} ← Father")
    else:
        print(f"House {house_num:2}: {d12_sign:<15}")

# Step 7: Vargottama Analysis (Same sign in D1 and D9)
print("\n━" * 60)
print("🌟 Vargottama Analysis (Strongest Positions)")
print("━" * 60)

print("""
VARGOTTAMA = When a planet/house is in the same sign in both D1 and D9

This is considered VERY AUSPICIOUS because:
- The planet/house has consistent strength across charts
- Results are more reliable and predictable
- Effects manifest both in material (D1) and spiritual (D9) realms
- Indicates strong karma and destiny in that area
""")

print("\nVargottama Houses (Same sign in D1 and D9):")
vargottama_count = 0

for house_num in range(1, 13):
    house_name = f"House{house_num}"
    d1_sign = d1_houses.get(house_name, "Unknown")
    d9_sign = d9_houses.get(house_name, "Unknown")

    if d1_sign == d9_sign and d1_sign != "Unknown":
        vargottama_count += 1
        print(f"  ✨ House {house_num}: {d1_sign} (Vargottama - Very Strong!)")

if vargottama_count == 0:
    print("  No Vargottama houses found")
else:
    print(f"\n  Total Vargottama Houses: {vargottama_count}/12")

# ADVANCED: Check planet positions in divisional charts
print("\n━" * 60)
print("🪐 Planet Positions Across Charts (Example: Sun)")
print("━" * 60)

print("""
To truly understand a planet's strength, check its position across
multiple divisional charts. A planet strong in multiple charts
gives consistent results.
""")

sun_d1 = Calculate.PlanetSignName(PlanetName.Sun, birth)
sun_d9 = Calculate.PlanetNavamsaSign(PlanetName.Sun, birth)
sun_d10 = Calculate.PlanetDashamsaSign(PlanetName.Sun, birth)

print(f"\nSun's Position:")
print(f"  D1 (Main):    {sun_d1}")
print(f"  D9 (Navamsa): {sun_d9}")
print(f"  D10 (Dashamsa): {sun_d10}")

if sun_d1 == sun_d9:
    print(f"\n  ⭐ Sun is Vargottama (in {sun_d1} in both D1 and D9)!")
    print(f"     This makes Sun very powerful for you.")

# NEXT STEPS
print("\n━" * 60)
print("Next Steps")
print("━" * 60)

print("""
1. Get planet positions in each divisional chart
2. Check planet strengths (Shadbala) in different charts
3. Analyze specific charts for specific questions:
   - Marriage issues? → Check D9
   - Career problems? → Check D10
   - Children? → Check D7
   - Property? → Check D4

4. Learn Varga Vimshopaka (divisional chart strength scoring)
5. Study how planets change signs across divisions
""")

# CUSTOMIZATION IDEAS
print("\n💡 Customization Ideas:\n")
print("1. Create a divisional chart comparison tool")
print("2. Build a Vargottama planet finder")
print("3. Make a career analysis using D10 + D24 (education)")
print("4. Create marriage compatibility checker using D9")
print("5. Build parent relationship analyzer using D12")

# COMMON QUESTIONS
print("\n❓ Common Questions:\n")

print("Q: Which divisional charts are most important?")
print("A: D1 (main), D9 (marriage/dharma), D10 (career), D3 (siblings),")
print("   D7 (children), D12 (parents), D60 (past life karma)\n")

print("Q: Can I use only D1 for predictions?")
print("A: D1 shows potential, but divisional charts show REALIZATION.")
print("   Use both for accurate predictions.\n")

print("Q: What if a planet is strong in D1 but weak in D9?")
print("A: It will give good results in the first half of life but")
print("   decline later. The reverse is also true.\n")

print("Q: How many divisional charts should I check?")
print("A: For beginners: D1, D9, D10")
print("   For intermediate: Add D3, D7, D12")
print("   For advanced: Study all D1-D60 based on specific questions\n")

print("✨ Divisional charts analysis complete!")
print("\nTo get all D1-D60 charts, use:")
print("  Calculate.AllHouse[ChartName]Signs(birth)")
print("  Example: Calculate.AllHouseSaptamsaSigns(birth)  # D7")
print("  Example: AllHouseShodasamsaSigns(birth)  # D16")
