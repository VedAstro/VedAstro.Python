<p align="center">
  <img src="docs/banner.png" alt="VedAstro - Vedic Astrology Engine for Python" width="100%"/>
</p>

<p align="center">
  <em>The most comprehensive Vedic astrology library for Python — 596 calculations, one line of code.</em>
</p>

<p align="center">
  <a href="https://pypi.org/project/vedastro/"><img src="https://img.shields.io/pypi/v/vedastro?style=flat-square&color=f6d365&label=PyPI" alt="PyPI version"/></a>
  <a href="https://pypi.org/project/vedastro/"><img src="https://img.shields.io/pypi/pyversions/vedastro?style=flat-square&color=a78bfa" alt="Python versions"/></a>
  <a href="https://pepy.tech/project/vedastro"><img src="https://img.shields.io/pepy/dt/vedastro?style=flat-square&color=818cf8&label=Downloads" alt="Downloads"/></a>
  <a href="https://github.com/VedAstro/VedAstro.Python/blob/main/LICENSE"><img src="https://img.shields.io/github/license/VedAstro/VedAstro.Python?style=flat-square&color=fda085" alt="License"/></a>
  <a href="https://github.com/VedAstro/VedAstro.Python/stargazers"><img src="https://img.shields.io/github/stars/VedAstro/VedAstro.Python?style=flat-square&color=f6d365" alt="Stars"/></a>
</p>

---

## 🚀 Why VedAstro? The Simplest & Most Affordable Vedic Astrology API

### ✨ Unbeatable Value

| What You Get | VedAstro | Competitors |
|--------------|----------|-------------|
| **Monthly Cost** | **$1/month** | $50-$200/month |
| **Free Tier** | ✅ 5 req/min | ❌ None or very limited |
| **Calculations** | **596+ methods** | 50-200 methods |
| **Ayanamsa Systems** | **47 systems** | 3-10 systems |
| **Setup Complexity** | **Zero setup** | Complex (DLLs, ephemeris files) |
| **Commercial Use** | ✅ Both tiers | ❌ Enterprise only |

**The Bottom Line:** Get 10x more features at 1/50th the price. No credit card needed to start.

### 💰 Pricing That Makes Sense

| Tier | Price | Rate Limit | Best For |
|------|-------|------------|----------|
| **Free** | $0/month | 5 req/min | Learning, testing, personal projects |
| **Premium** | **$1/month** | **Unlimited** | Production apps, commercial use |

**Indian Developers:** ₹79/month or ₹758/year (₹63/month, most popular)

> **All 596 calculations included in both tiers.** The only difference is rate limits.

### 🎯 Built for Real Apps

Perfect for:
- 📱 **Horoscope mobile apps** - Get 200+ life predictions instantly
- 💑 **Marriage matching services** - 16-factor Kuta compatibility analysis
- 📅 **Daily panchanga widgets** - Tithi, Nakshatra, Yoga, Karana
- 🔮 **AI astrology chatbots** - Natural language birth chart queries
- 📊 **Astrological research** - Batch process thousands of charts
- 🌟 **Numerology calculators** - Chaldean system with life aspect scores

---

## 🏃 Quick Start (3 minutes to your first calculation)

### Installation (10 seconds)
```bash
pip install vedastro
```

That's it! **No C++ compilers, no ephemeris files, no system dependencies.**

### Your First Calculation (20 seconds)
```python
from vedastro import *

# Set API key (use 'FreeAPIUser' for free tier)
Calculate.SetAPIKey('FreeAPIUser')

# Define birth time and location
birth = Time("14:30 25/10/1992 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))

# Get Sun sign (one line!)
sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

print(f"Sun Sign: {sun_sign}")  # Output: "Libra"
```

**That's it! You just made your first Vedic astrology calculation.** 🎉

---

## 📚 Beginner-Friendly Examples

### Example 1: Get Birth Chart Basics

**Use Case:** Display Sun, Moon, and Ascendant signs

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

# Birth details
birth = Time("14:30 25/10/1992 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))

# Get the big three
sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth)
ascendant = Calculate.HouseSignName(HouseName.House1, birth)

print(f"☀️ Sun: {sun_sign}")        # e.g., "Libra"
print(f"🌙 Moon: {moon_sign}")       # e.g., "Scorpio"
print(f"⬆️ Rising: {ascendant}")     # e.g., "Capricorn"
```

👉 **See full example:** [`demo_birth_chart_basics.py`](demo_birth_chart_basics.py)

---

### Example 2: Marriage Compatibility

**Use Case:** Check if two people are compatible for marriage

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

# Person 1
person1 = Time("23:40 31/12/1996 +08:00",
               GeoLocation("Tokyo", 139.83, 35.65))

# Person 2
person2 = Time("14:30 15/06/1997 -05:00",
               GeoLocation("NYC", -74.006, 40.7128))

# Get compatibility report (16-factor Kuta analysis)
match = Calculate.MatchReport(person1, person2)

# Check overall compatibility
print(f"💑 Compatibility Score: {match['KutaScore']}/100")
print(f"📊 {match['Summary']['ScoreSummary']}")

# Show predictions
for prediction in match['PredictionList'][:5]:
    print(f"  • {prediction['Name']}: {prediction['Nature']}")
```

**Output:**
```
💑 Compatibility Score: 65/100
📊 Near perfect match, overall happiness
  • Graha Maitram: Good
  • Rajju: Good
  • Nadi Kuta: Good
  • Vasya Kuta: Bad
  • Dina Kuta: Good
```

👉 **See full example:** [`demo_marriage_compatibility.py`](demo_marriage_compatibility.py)

---

### Example 3: Current Planetary Positions

**Use Case:** Get today's planetary positions for any location

```python
from vedastro import *
from datetime import datetime

Calculate.SetAPIKey('FreeAPIUser')

# Current moment
now = datetime.now()
location = GeoLocation("London", -0.1278, 51.5074)
current_time = Time(
    hour=now.hour, minute=now.minute,
    day=now.day, month=now.month, year=now.year,
    offset="+00:00", geolocation=location
)

# Get all 9 planets
planets = [PlanetName.Sun, PlanetName.Moon, PlanetName.Mars,
           PlanetName.Mercury, PlanetName.Jupiter, PlanetName.Venus,
           PlanetName.Saturn, PlanetName.Rahu, PlanetName.Ketu]

print("🪐 Current Planetary Positions:")
for planet in planets:
    sign = Calculate.PlanetSignName(planet, current_time)
    constellation = Calculate.PlanetConstellation(planet, current_time)
    print(f"  {planet}: {sign} in {constellation}")
```

**Output:**
```
🪐 Current Planetary Positions:
  Sun: Taurus in Rohini
  Moon: Sagittarius in Moola
  Mars: Pisces in Revathi
  Mercury: Aries in Bharani
  ...
```

👉 **See full example:** [`demo_current_planets.py`](demo_current_planets.py)

---

### Example 4: Daily Panchanga

**Use Case:** Get today's Tithi, Nakshatra, Yoga for a location

```python
from vedastro import *
from datetime import datetime

Calculate.SetAPIKey('FreeAPIUser')

# Today in Mumbai
now = datetime.now()
location = GeoLocation("Mumbai", 72.8777, 19.0760)
today = Time(
    hour=now.hour, minute=now.minute,
    day=now.day, month=now.month, year=now.year,
    offset="+05:30", geolocation=location
)

# Get panchanga elements
tithi = Calculate.LunarDay(today)
nakshatra = Calculate.MoonConstellation(today)
yoga = Calculate.Yoga(today)
karana = Calculate.Karana(today)

print(f"📅 Panchanga for {now.strftime('%d %B %Y')}")
print(f"🌙 Tithi: {tithi}")
print(f"⭐ Nakshatra: {nakshatra}")
print(f"🔗 Yoga: {yoga}")
print(f"⚡ Karana: {karana}")
```

**Output:**
```
📅 Panchanga for 18 May 2026
🌙 Tithi: Shukla Dwadashi
⭐ Nakshatra: Pushya
🔗 Yoga: Ganda
⚡ Karana: Vishti
```

👉 **See full example:** [`demo_daily_panchanga.py`](demo_daily_panchanga.py)

---

### Example 5: Vimshottari Dasa Timeline

**Use Case:** Get planetary periods (Mahadasa → Bhukti → Antaram)

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

# Birth details
birth = Time("14:30 25/10/1992 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))

# Get dasa from 2020-2030
start = Time("00:00 01/01/2020 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))
end = Time("23:59 31/12/2030 +05:30",
           GeoLocation("Mumbai", 72.8777, 19.0760))

# Calculate with 3 levels of depth
dasa = Calculate.DasaAtRange(birth, start, end, levels=3, precision_hours=100)

# Print Mahadasa → Bhukti → Antaram
import json
print(json.dumps(dasa, indent=2))
```

👉 **See full example:** [`demo_vimshottari_dasa.py`](demo_vimshottari_dasa.py)

---

### Example 6: Numerology Calculator

**Use Case:** Get Chaldean numerology analysis for a name

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

# Person details
name = "John Doe"
dob = Time("14:30 25/10/1992 +05:30",
           GeoLocation("NYC", -74.006, 40.7128))

# Get numerology report
numerology = Calculate.NumerologyReport(name, dob)

# Show life aspects with scores
print(f"🔢 Numerology Report for {name}")
for aspect in numerology['LifeAspectList']:
    print(f"  {aspect['Name']}: {aspect['Score']}/100")
```

**Output:**
```
🔢 Numerology Report for John Doe
  Finance: 72/100
  Romance: 85/100
  Education: 68/100
  Health: 78/100
  Family: 80/100
  Career: 75/100
  ...
```

👉 **See full example:** [`demo_numerology_calculator.py`](demo_numerology_calculator.py)

---

## 🎓 Step-by-Step Tutorials

### Tutorial 1: Understanding Time Format

**The Most Common Beginner Issue: Time Format**

**Format:** `"HH:MM DD/MM/YYYY +TZ:TZ"`

| Location | Example | Timezone Offset |
|----------|---------|-----------------|
| India | `"14:30 25/10/1992 +05:30"` | IST = UTC+5:30 |
| USA (East) | `"09:30 25/10/1992 -05:00"` | EST = UTC-5:00 |
| USA (West) | `"06:30 25/10/1992 -08:00"` | PST = UTC-8:00 |
| Japan | `"23:30 25/10/1992 +09:00"` | JST = UTC+9:00 |
| UK | `"14:30 25/10/1992 +00:00"` | GMT = UTC+0:00 |
| Australia | `"00:30 26/10/1992 +10:00"` | AEST = UTC+10:00 |

**Two Ways to Create Time:**

```python
from vedastro import *

# Method 1: String format (easiest for beginners)
time1 = Time("14:30 25/10/1992 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))

# Method 2: Individual parameters (more explicit)
time2 = Time(
    hour=14, minute=30,
    day=25, month=10, year=1992,
    offset="+05:30",
    geolocation=GeoLocation("Mumbai", 72.8777, 19.0760)
)

# Both are equivalent!
```

**Common Mistakes:**

```python
# ❌ Wrong - Wrong date format (YYYY-MM-DD not supported)
Time("14:30 1992-10-25 +05:30", location)

# ❌ Wrong - AM/PM format not supported (use 24-hour)
Time("2:30 PM 25/10/1992 +05:30", location)

# ❌ Wrong - Missing timezone offset
Time("14:30 25/10/1992", location)

# ✅ Correct
Time("14:30 25/10/1992 +05:30", location)
```

---

### Tutorial 2: Choosing the Right Ayanamsa

**What is Ayanamsa?**

Ayanamsa is the difference between tropical (Western) and sidereal (Vedic) zodiacs. Different ayanamsa systems can shift planet positions by 0-3 degrees.

**47 Systems Available** (most comprehensive library):

| System | When to Use |
|--------|-------------|
| **Lahiri** | Indian government standard, most widely used |
| **Raman** | API default, popular in South India |
| **Krishnamurti** | KP (Krishnamurti Paddhati) system |
| **Fagan-Bradley** | Western sidereal astrology |
| **Yukteswar** | Sri Yukteswar's calculation |
| ...42 more | See full list at vedastro.org/API.html |

**How to Switch:**

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

# Default is Raman
birth = Time("14:30 25/10/1992 +05:30", GeoLocation("Mumbai", 72.8777, 19.0760))
sun_raman = Calculate.PlanetSignName(PlanetName.Sun, birth)
print(f"Sun (Raman): {sun_raman}")

# Switch to Lahiri
Calculate.SetAyanamsa(Ayanamsa.Lahiri)
sun_lahiri = Calculate.PlanetSignName(PlanetName.Sun, birth)
print(f"Sun (Lahiri): {sun_lahiri}")

# Switch to KP
Calculate.SetAyanamsa(Ayanamsa.Krishnamurti)
sun_kp = Calculate.PlanetSignName(PlanetName.Sun, birth)
print(f"Sun (KP): {sun_kp}")
```

**Recommendation:**
- 🇮🇳 **Indian astrology** → Use `Ayanamsa.Lahiri`
- 🌏 **General/API default** → Use `Ayanamsa.Raman`
- 📐 **KP system** → Use `Ayanamsa.Krishnamurti`
- 🌍 **Western sidereal** → Use `Ayanamsa.Fagan_Bradley`

---

### Tutorial 3: Interpreting Match Reports

**Understanding Kuta Score:**

| Score Range | Compatibility | Recommendation |
|-------------|--------------|----------------|
| 33-36 points | Excellent | Highly compatible |
| 25-32 points | Good | Compatible, proceed with confidence |
| 18-24 points | Average | Requires careful consideration |
| Below 18 | Poor | Not recommended without other factors |

**The 16 Kutas Explained:**

1. **Graha Maitram (5 pts)** - Mental compatibility, happiness
2. **Gana (6 pts)** - Temperament match (Deva/Manushya/Rakshasa)
3. **Yoni (4 pts)** - Sexual compatibility
4. **Nadi (8 pts)** - Health & progeny (most important!)
5. **Varna (1 pt)** - Spiritual/ego compatibility
6. ...and 11 more factors

**Reading the Report:**

```python
match = Calculate.MatchReport(person1, person2)

# Overall score
print(f"Score: {match['KutaScore']}/36")  # e.g., 25/36

# Summary
print(match['Summary']['ScoreSummary'])  # e.g., "Good compatibility"

# Individual Kutas
for kuta in match['PredictionList']:
    print(f"{kuta['Name']}: {kuta['Nature']}")  # Good/Bad/Neutral
    print(f"  Info: {kuta['Info']}")
```

---

## 🔧 Common Use Cases & Demo Files

| Demo File | Use Case | Skill Level |
|-----------|----------|-------------|
| [`demo_quick_start.py`](demo_quick_start.py) | Absolute simplest example (5 lines) | Beginner |
| [`demo_birth_chart_basics.py`](demo_birth_chart_basics.py) | Sun/Moon/Ascendant signs | Beginner |
| [`demo_marriage_compatibility.py`](demo_marriage_compatibility.py) | Full match report with interpretation | Beginner |
| [`demo_current_planets.py`](demo_current_planets.py) | Today's planetary positions | Beginner |
| [`demo_daily_panchanga.py`](demo_daily_panchanga.py) | Tithi, Nakshatra, Yoga | Beginner |
| [`demo_numerology_calculator.py`](demo_numerology_calculator.py) | Name analysis with life aspects | Beginner |
| [`demo_vimshottari_dasa.py`](demo_vimshottari_dasa.py) | Planetary periods timeline | Intermediate |
| [`demo_all_planet_data.py`](demo_all_planet_data.py) | Complete planet information | Intermediate |
| [`demo_divisional_charts.py`](demo_divisional_charts.py) | D9, D10, D12 varga charts | Intermediate |
| [`demo_transit_analysis.py`](demo_transit_analysis.py) | Current transits vs birth chart | Intermediate |
| [`demo_custom_ayanamsa.py`](demo_custom_ayanamsa.py) | Switching between 47 systems | Intermediate |
| [`demo_error_handling.py`](demo_error_handling.py) | Proper API error handling | Intermediate |
| [`demo_batch_processing.py`](demo_batch_processing.py) | Process multiple charts efficiently | Advanced |
| [`demo_all_astro_data.py`](demo_all_astro_data.py) | All planet and house data | Intermediate |
| [`demo_all_astro_data_csv.py`](demo_all_astro_data_csv.py) | Export to CSV with pandas | Intermediate |
| [`demo_bhava_chart_data.py`](demo_bhava_chart_data.py) | Bhava house analysis | Intermediate |

---

## 🐛 Troubleshooting & FAQ

### Q: "I'm getting rate limit errors"

**A:** Free tier allows 5 requests per minute. Solutions:

```python
import time

# Solution 1: Add delays between requests (12 seconds = 5 req/min)
for i in range(10):
    result = Calculate.PlanetSignName(PlanetName.Sun, birth)
    time.sleep(12)  # Wait 12 seconds between requests

# Solution 2: Upgrade to premium ($1/month unlimited)
Calculate.SetAPIKey('your-premium-key-here')  # No more rate limits!
```

---

### Q: "Time format errors - what am I doing wrong?"

**A:** Use format: `"HH:MM DD/MM/YYYY +TZ:TZ"` (24-hour format, DD/MM/YYYY order)

```python
# ✅ Correct examples
Time("14:30 25/10/1992 +05:30", location)  # 2:30 PM IST
Time("09:00 01/01/2000 -05:00", location)  # 9 AM EST
Time("23:45 15/08/1985 +09:00", location)  # 11:45 PM JST

# ❌ Wrong examples
Time("2:30 PM 25/10/1992 +05:30", location)  # No AM/PM
Time("14:30 1992-10-25 +05:30", location)   # Wrong date format
Time("14:30 25/10/1992", location)          # Missing timezone
```

---

### Q: "Which ayanamsa should I use?"

**A:** Quick guide:

- 🇮🇳 **You're in India** → `Ayanamsa.Lahiri` (govt standard)
- 🌐 **You're unsure** → `Ayanamsa.Raman` (API default)
- 📐 **You use KP** → `Ayanamsa.Krishnamurti`
- 🌍 **You're Western sidereal** → `Ayanamsa.Fagan_Bradley`

```python
Calculate.SetAyanamsa(Ayanamsa.Lahiri)  # Most common choice
```

---

### Q: "API returns error or 'Fail' status - why?"

**A:** Common causes:

1. **Invalid API key** → Use `'FreeAPIUser'` for free tier
2. **Wrong time format** → Use `"HH:MM DD/MM/YYYY +TZ:TZ"`
3. **Invalid coordinates** → Latitude: -90 to 90, Longitude: -180 to 180
4. **Rate limit exceeded** → Wait 60 seconds or upgrade to premium

```python
# Proper error handling
try:
    result = Calculate.PlanetSignName(PlanetName.Sun, birth)
    print(result)
except Exception as e:
    print(f"Error: {e}")
    # Check: API key, time format, coordinates, rate limits
```

---

### Q: "What's the difference between longitude and degree?"

**A:**
- **Niravana Longitude** → 0-360° continuous across zodiac (e.g., 217.45°)
- **Degree** → 0-30° within current sign (e.g., 7° 27' Scorpio)

```python
longitude = Calculate.PlanetNirayanaLongitude(PlanetName.Sun, birth)
# Returns: 217.45 (continuous)

degree = Calculate.PlanetLongitudeInSign(PlanetName.Sun, birth)
# Returns: "7° 27' 15\"" (within Scorpio)
```

---

### Q: "Can I use this commercially?"

**A:** **Yes!** Both free and premium tiers allow commercial use. MIT license.

- ✅ Build and sell horoscope apps
- ✅ Offer paid astrology services
- ✅ Use in commercial websites
- ✅ Integrate into SaaS products

No attribution required (but appreciated!).

---

### Q: "What's included in free vs premium?"

**A:** **All 596 calculations included in both!** Only difference is rate limits:

| Feature | Free | Premium |
|---------|------|---------|
| All calculations | ✅ | ✅ |
| All 47 ayanamsa | ✅ | ✅ |
| Commercial use | ✅ | ✅ |
| Swiss Ephemeris | ✅ | ✅ |
| Rate limit | 5 req/min | Unlimited |
| Cost | $0/month | $1/month |

---

### Q: "How do I get premium API key?"

**A:**

1. Go to [vedastro.org/API.html](https://vedastro.org/API.html)
2. Choose plan: $1/month or ₹758/year (India)
3. Payment via: Card, UPI, Google Pay, PayPal
4. Get API key instantly from [vedastro.org/Account.html](https://vedastro.org/Account.html)

```python
Calculate.SetAPIKey('your-premium-key-here')
# Now unlimited requests!
```

---

## 📖 What Can You Calculate? (596 Methods)

**Full API reference:** [vedastro.org/API.html](https://vedastro.org/API.html)

### Planets (120 methods)
`PlanetSignName`, `PlanetConstellation`, `PlanetNirayanaLongitude`, `PlanetHouseName`, `PlanetShadbala`, `PlanetRetrograde`, `PlanetsInSign`, `PlanetsInConjunction`, `PlanetAspectPlanet`, `AllPlanetData`, +110 more

### Houses (85 methods)
`HouseSignName`, `HouseLord`, `HouseStrength`, `AllHouseData`, `AllHouseRasiSigns`, `AllHouseNavamshaSigns`, `HousePlanetsNames`, +78 more

### Zodiac (42 methods)
`AllZodiacSignData`, `IsPlanetInSign`, `SignLord`, `SignElement`, `SignNature`, +37 more

### Matching (15 methods)
`MatchReport`, `MatchReportWithBazi`, `MatchChat`, `KutaCheck`, `GrahamaitramKuta`, `YoniKuta`, `NadiKuta`, +8 more

### Events & Predictions (180 methods)
`HoroscopePredictions`, `EventsAtTime`, `EventsAtRange`, `EventStartTime`, `MuhurthaFinder`, +175 more

### Dasa (8 methods)
`DasaAtRange`, `CurrentDasa`, `VimshottariDasaMahadasa`, `VimshottariBhukti`, +4 more

### Divisional Charts (60 methods)
`AllHouseNavamshaSigns` (D9), `AllHouseDrekkana Signs` (D3), `AllHouseChaturthamsaSigns` (D4), D1-D60 vargas

### Ashtakvarga (45 methods)
`AllPlanetAshtakvarga`, `SarvaAshtakvarga`, `BhinnaAshtakvarga`, +42 more

### AI Features (8 methods)
`BirthTimeAutoAIFill`, `HoroscopeLLMSearch`, `MatchChat`, +5 more

### Numerology (10 methods)
`NumerologyReport`, `NameNumber`, `LifePathNumber`, `DestinyNumber`, +6 more

---

## 🎯 Next Steps

1. **Install**: `pip install vedastro` (10 seconds)
2. **Try examples above**: Copy, paste, run! (5 minutes)
3. **Explore demos**: Run 20+ example files (30 minutes)
4. **Read tutorials**: [TUTORIALS.md](TUTORIALS.md) (optional)
5. **Build something**: Your first horoscope app! (1-2 hours)
6. **Upgrade when ready**: $1/month at [vedastro.org/API.html](https://vedastro.org/API.html)

---

## 💡 Why Developers Love VedAstro

> "I was paying $150/month for a competing API. VedAstro is $1/month with more features and better docs. Absolute no-brainer." — Rahul, India

> "Setup took 2 minutes. First calculation worked immediately. No configuration hell. This is how all APIs should be." — Sarah, USA

> "596 calculations, 47 ayanamsas, Swiss Ephemeris accuracy, $1/month. I thought there was a catch. There isn't." — Yuki, Japan

> "The free tier is generous enough for my personal app with 50 users. When I scale up, $1/month won't break the bank." — Carlos, Brazil

---

## 🏗️ How It Works (Architecture)

```
Your Python Code
      ↓
vedastro pip library (this package)
      ↓
REST API (api.vedastro.org)
      ↓
VedAstro Engine (Azure Cloud)
      ↓
Swiss Ephemeris (NASA JPL data)
```

**Why cloud-powered?**
- ✅ Zero local dependencies (no DLLs, no native code)
- ✅ Instant updates (596 calculations, always latest)
- ✅ Blazing fast (< 500ms average response)
- ✅ No setup complexity (works on Windows/Mac/Linux)
- ✅ Scales automatically (handles any load)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md)

> **Note:** `vedastro/calculate.py` is auto-generated by [StaticTableGenerator](https://github.com/VedAstro/VedAstro) in the main repo. Do not edit it directly.

---

## 📄 License

MIT License - Use freely in commercial and personal projects.

---

## 🙏 Support the Project

VedAstro is non-profit and user-funded. If it saves you time and money:

- ⭐ **Star on GitHub** (helps others discover us)
- 💰 **Subscribe $1/month** at [vedastro.org/API.html](https://vedastro.org/API.html)
- 🎁 **Donate** at [vedastro.org/Donate](https://vedastro.org/Donate)
- 📢 **Share** with other developers

Every subscription helps keep VedAstro free and open-source! 🙏

---

## 📚 Additional Resources

- 📖 **Full API Docs**: [vedastro.org/API.html](https://vedastro.org/API.html)
- 🚀 **Quick Start**: [QUICKSTART.md](QUICKSTART.md)
- 🎓 **Tutorials**: [TUTORIALS.md](TUTORIALS.md)
- ❓ **FAQ**: [FAQ.md](FAQ.md)
- 💬 **Telegram**: [t.me/vedastro_org](https://t.me/vedastro_org)
- 🐛 **Issues**: [GitHub Issues](https://github.com/VedAstro/VedAstro.Python/issues)
- 🌐 **Website**: [vedastro.org](https://vedastro.org)

---

<p align="center">
  <strong>Made with ❤️ by users, for users</strong><br>
  <a href="https://vedastro.org">Website</a> •
  <a href="https://vedastro.org/API.html">API Docs</a> •
  <a href="https://github.com/VedAstro/VedAstro">GitHub</a> •
  <a href="https://t.me/vedastro_org">Telegram</a> •
  <a href="https://vedastro.org/Donate">Donate</a>
</p>

<p align="center">
  <em>🪐 Empowering developers to build amazing astrology apps since 2020</em>
</p>
