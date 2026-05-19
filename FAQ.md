# VedAstro Python Library - FAQ

Answers to the most common questions from beginners.

---

## Installation & Setup

### Q: How do I install VedAstro?

**A:** Simply run:
```bash
pip install vedastro
```

No additional dependencies, no configuration files, no setup needed!

---

### Q: Do I need to download ephemeris files?

**A:** No! All calculations run on our cloud servers. You don't need to download any data files, ephemeris data, or timezone databases. Just install the pip package and start coding.

---

### Q: Which Python versions are supported?

**A:** Python 3.9+ (3.9, 3.10, 3.11, 3.12, 3.13)

Check your version:
```bash
python --version
```

---

### Q: Can I use this offline?

**A:** No, VedAstro requires an internet connection because calculations are performed on our cloud servers. This design ensures you always get the latest algorithms and updates without needing to reinstall the library.

---

## API Keys & Pricing

### Q: Do I need an API key?

**A:** For the **free tier**, you can either:
- Use no key at all (defaults to free tier)
- Use `Calculate.SetAPIKey('FreeAPIUser')`

For the **premium tier** ($1/month unlimited), get your key from [vedastro.org/API.html](https://vedastro.org/API.html).

---

### Q: What's the difference between free and premium?

**A:**

| Feature | Free | Premium |
|---------|------|---------|
| **All 596 calculations** | ✅ | ✅ |
| **All 47 ayanamsa** | ✅ | ✅ |
| **Commercial use** | ✅ | ✅ |
| **Swiss Ephemeris** | ✅ | ✅ |
| **Rate limit** | 5 req/min | Unlimited |
| **Cost** | $0/month | $1/month |

**Bottom line:** All features are the same. Only difference is rate limits.

---

### Q: How do I upgrade to premium?

**A:**
1. Go to [vedastro.org/API.html](https://vedastro.org/API.html)
2. Choose plan ($1/month or ₹758/year for India)
3. Pay via card, UPI, Google Pay, or PayPal
4. Get API key from [vedastro.org/Account.html](https://vedastro.org/Account.html)
5. Use it: `Calculate.SetAPIKey('your-key-here')`

---

### Q: What happens if I exceed the rate limit (free tier)?

**A:** You'll get a rate limit error. Solutions:
1. Add delays: `time.sleep(12)` between requests (12 sec = 5 req/min)
2. Upgrade to premium: $1/month for unlimited requests

---

### Q: Can I use this commercially?

**A:** **Yes!** Both free and premium tiers allow commercial use:
- ✅ Build and sell apps
- ✅ Offer paid services
- ✅ Use in SaaS products
- ✅ Integrate in commercial websites

MIT license = no attribution required (but appreciated!).

---

### Q: Is there a discount for students or nonprofits?

**A:** Contact us at contact@vedastro.org with proof of student/nonprofit status. We offer discounts on a case-by-case basis.

---

## Time & Location Format

### Q: I keep getting time format errors. What's wrong?

**A:** Use the exact format: `"HH:MM DD/MM/YYYY +TZ:TZ"`

✅ **Correct:**
```python
Time("14:30 25/10/1992 +05:30", location)  # 2:30 PM IST
Time("09:00 01/01/2000 -05:00", location)  # 9 AM EST
Time("23:45 15/08/1985 +09:00", location)  # 11:45 PM JST
```

❌ **Wrong:**
```python
Time("2:30 PM 25/10/1992 +05:30", location)  # No AM/PM format
Time("14:30 1992-10-25 +05:30", location)    # Wrong date order
Time("14:30 25/10/1992", location)           # Missing timezone
Time("14:30 25-10-1992 +05:30", location)    # Hyphens not allowed
```

**Key rules:**
- Use 24-hour format (14:30, not 2:30 PM)
- Date order: DD/MM/YYYY (not MM/DD/YYYY or YYYY-MM-DD)
- Always include timezone offset (+05:30, -08:00, etc.)

---

### Q: How do I know my timezone offset?

**A:** Common timezone offsets:

| Location | Offset | Example |
|----------|--------|---------|
| India | `+05:30` | IST |
| UK | `+00:00` | GMT (or `+01:00` in summer) |
| USA East Coast | `-05:00` | EST (or `-04:00` in summer) |
| USA West Coast | `-08:00` | PST (or `-07:00` in summer) |
| Japan | `+09:00` | JST |
| Australia (Sydney) | `+10:00` | AEST (or `+11:00` in summer) |
| China | `+08:00` | CST |

Search online for "[your city] timezone offset from UTC" if not listed above.

---

### Q: What about daylight saving time (DST)?

**A:** You must adjust the offset manually:
- **Standard time**: Use standard offset (e.g., EST = `-05:00`)
- **Daylight time**: Add 1 hour (e.g., EDT = `-04:00`)

Check if the birth date was during DST for your location.

---

### Q: How do I enter coordinates (latitude/longitude)?

**A:**
- **Latitude**: -90 to +90 (North = positive, South = negative)
- **Longitude**: -180 to +180 (East = positive, West = negative)

Examples:
```python
# Mumbai, India (North, East)
GeoLocation("Mumbai", 72.8777, 19.0760)

# New York, USA (North, West)
GeoLocation("NYC", -74.006, 40.7128)

# Sydney, Australia (South, East)
GeoLocation("Sydney", 151.2093, -33.8688)
```

Find coordinates: Search "[city name] coordinates" on Google.

---

## Ayanamsa (Zodiac System)

### Q: Which ayanamsa should I use?

**A:** Quick guide:

| Your Context | Recommended Ayanamsa |
|--------------|----------------------|
| Indian astrology | `Ayanamsa.Lahiri` (govt standard) |
| Unsure / General | `Ayanamsa.Raman` (API default) |
| KP system | `Ayanamsa.Krishnamurti` |
| Western sidereal | `Ayanamsa.Fagan_Bradley` |

How to set:
```python
Calculate.SetAyanamsa(Ayanamsa.Lahiri)
```

---

### Q: What's the difference between ayanamsas?

**A:** Ayanamsa is the offset between tropical (Western) and sidereal (Vedic) zodiacs. Different systems calculate this offset slightly differently, resulting in 0-3° variations.

This mainly affects planets near sign boundaries (0°-3° or 27°-30°).

---

### Q: How many ayanamsa systems does VedAstro support?

**A:** **47 systems** - the most comprehensive library available:
- Lahiri, Raman, Krishnamurti, Fagan-Bradley, Yukteswar
- ...and 42 more!

See full list: [vedastro.org/API.html](https://vedastro.org/API.html)

---

### Q: Why is my Sun sign different in Vedic vs Western?

**A:**
- **Vedic** uses sidereal zodiac (actual star positions)
- **Western** uses tropical zodiac (fixed to seasons/equinoxes)

The difference is about 24°, which shifts most signs back by one (e.g., Libra in Vedic = Scorpio in Western).

Both are valid systems for different purposes.

---

## Understanding Results

### Q: What's the difference between longitude and degree?

**A:**
- **Niravana Longitude** = 0-360° continuous (e.g., 217.45°)
- **Degree in Sign** = 0-30° within current sign (e.g., 7° 27' Scorpio)

Examples:
```python
# Continuous longitude
longitude = Calculate.PlanetNirayanaLongitude(PlanetName.Sun, birth)
# Output: 217.45

# Degree within sign
degree = Calculate.PlanetLongitudeInSign(PlanetName.Sun, birth)
# Output: "7° 27' 15\""
```

---

### Q: How do I interpret match compatibility scores?

**A:** Kuta score ranges:

| Score | Compatibility | Recommendation |
|-------|---------------|----------------|
| 33-36 | Excellent | Highly compatible |
| 25-32 | Good | Compatible, proceed confidently |
| 18-24 | Average | Requires careful consideration |
| Below 18 | Poor | Not recommended |

Also check individual Kutas, especially:
- **Nadi** (8 pts) - Health & progeny (most important!)
- **Graha Maitram** (5 pts) - Mental compatibility
- **Yoni** (4 pts) - Sexual compatibility

---

### Q: What does "retrograde" mean?

**A:** From Earth's perspective, the planet appears to move backward in the sky. Astrologically:
- Time to review, revise, redo
- Matters related to that planet may face delays
- Inner reflection favored over outward action

Check retrograde status:
```python
is_retro = Calculate.IsPlanetRetrograde(PlanetName.Mercury, birth)
```

---

## Errors & Troubleshooting

### Q: I get "Failed to establish connection" error

**A:** Possible causes:

1. **No internet** - VedAstro requires internet connection
2. **Firewall blocking** - Check if port 443 (HTTPS) is blocked
3. **API server down** - Check status at [status.vedastro.org](https://status.vedastro.org)

Try:
```python
import requests
response = requests.get("https://api.vedastro.org")
print(response.status_code)  # Should be 200
```

---

### Q: I get "Invalid API key" error

**A:** Solutions:
1. **Use free tier**: `Calculate.SetAPIKey('FreeAPIUser')`
2. **Check spelling**: Copy-paste key from [vedastro.org/Account.html](https://vedastro.org/Account.html)
3. **Verify subscription**: Check if premium subscription is active

---

### Q: API returns empty result or None

**A:** Check:
1. **Time format** - Must be `"HH:MM DD/MM/YYYY +TZ:TZ"`
2. **Coordinates** - Lat: -90 to 90, Long: -180 to 180
3. **API key** - Valid and not expired
4. **Internet** - Connection is stable

Add error handling:
```python
try:
    result = Calculate.PlanetSignName(PlanetName.Sun, birth)
    if result:
        print(result)
    else:
        print("Empty result - check input parameters")
except Exception as e:
    print(f"Error: {e}")
```

---

### Q: How do I report a bug?

**A:**
1. Check if it's a known issue: [GitHub Issues](https://github.com/VedAstro/VedAstro.Python/issues)
2. If not, open a new issue with:
   - Clear description
   - Code to reproduce the bug
   - Expected vs actual behavior
   - Python version and VedAstro version

---

## Features & Calculations

### Q: How many calculations are available?

**A:** **596+ methods** across 10 categories:
- Planets (120 methods)
- Houses (85 methods)
- Zodiac (42 methods)
- Matching (15 methods)
- Events (180 methods)
- Dasa (8 methods)
- Divisional Charts (60 methods)
- Ashtakvarga (45 methods)
- AI Features (8 methods)
- Numerology (10 methods)

Full list: [vedastro.org/API.html](https://vedastro.org/API.html)

---

### Q: Can I get divisional charts (D9, D10, etc.)?

**A:** Yes! All D1-D60 charts available:

```python
# D9 (Navamsa)
d9_signs = Calculate.AllHouseNavamshaSigns(birth)

# D10 (Dashamsa)
d10_signs = Calculate.AllHouseDashamsaSigns(birth)

# D12 (Dwadashamsa)
d12_signs = Calculate.AllHouseDwadashamsaSigns(birth)
```

---

### Q: Can I calculate Ashtakvarga?

**A:** Yes! Both SAV (Sarva Ashtakvarga) and BAV (Bhinna Ashtakvarga):

```python
# All planets' ashtakvarga
ashtakvarga = Calculate.AllPlanetAshtakvarga(birth)

# Sarva Ashtakvarga (combined)
sav = Calculate.SarvaAshtakvarga(birth)
```

---

### Q: Does VedAstro support Jaimini system?

**A:** Partial support. We have:
- Char Karakas
- Jaimini aspects
- Some Jaimini dasas

Full Jaimini support is on our roadmap.

---

### Q: Can I get Vimshottari Dasa periods?

**A:** Yes!

```python
birth = Time("14:30 25/10/1992 +05:30", GeoLocation("Mumbai", 72.8777, 19.0760))
start = Time("00:00 01/01/2020 +05:30", GeoLocation("Mumbai", 72.8777, 19.0760))
end = Time("23:59 31/12/2030 +05:30", GeoLocation("Mumbai", 72.8777, 19.0760))

# Get Mahadasa, Bhukti, Antaram (3 levels)
dasa = Calculate.DasaAtRange(birth, start, end, levels=3, precision_hours=100)
```

---

## Advanced Usage

### Q: How do I batch process multiple charts?

**A:** See [`demo_batch_processing.py`](demo_batch_processing.py):

```python
# Process multiple birth charts efficiently
charts = [
    {"name": "Person 1", "time": "14:30 25/10/1992 +05:30", "location": GeoLocation("Mumbai", 72.8777, 19.0760)},
    {"name": "Person 2", "time": "09:00 01/01/1990 -05:00", "location": GeoLocation("NYC", -74.006, 40.7128)},
    # ...
]

for chart in charts:
    birth = Time(chart["time"], chart["location"])
    sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
    print(f"{chart['name']}: {sun_sign}")
    time.sleep(12)  # Rate limiting for free tier
```

---

### Q: Can I use this with Flask/Django?

**A:** Yes! VedAstro works with any Python web framework:

```python
from flask import Flask, request, jsonify
from vedastro import *

app = Flask(__name__)
Calculate.SetAPIKey('your-key-here')

@app.route('/horoscope', methods=['POST'])
def get_horoscope():
    data = request.json
    birth = Time(data['birth_time'], GeoLocation(data['location'], data['long'], data['lat']))
    sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
    return jsonify({"sun_sign": sun_sign})

app.run()
```

---

### Q: How do I cache results to reduce API calls?

**A:** Use Python's caching:

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def get_sun_sign(birth_time_str, location_name, long, lat):
    birth = Time(birth_time_str, GeoLocation(location_name, long, lat))
    return Calculate.PlanetSignName(PlanetName.Sun, birth)

# First call - makes API request
result1 = get_sun_sign("14:30 25/10/1992 +05:30", "Mumbai", 72.8777, 19.0760)

# Second call with same params - returns cached result
result2 = get_sun_sign("14:30 25/10/1992 +05:30", "Mumbai", 72.8777, 19.0760)
```

---

## Support & Community

### Q: Where can I get help?

**A:**
- **Documentation**: [vedastro.org/API.html](https://vedastro.org/API.html)
- **GitHub Issues**: [github.com/VedAstro/VedAstro.Python/issues](https://github.com/VedAstro/VedAstro.Python/issues)
- **Telegram**: [t.me/vedastro_org](https://t.me/vedastro_org)
- **Email**: contact@vedastro.org

---

### Q: How do I request a new feature?

**A:**
1. Check if it exists: [vedastro.org/API.html](https://vedastro.org/API.html)
2. Open GitHub issue: [github.com/VedAstro/VedAstro.Python/issues](https://github.com/VedAstro/VedAstro.Python/issues)
3. Email us: contact@vedastro.org

We prioritize features based on user demand!

---

### Q: Can I contribute to VedAstro?

**A:** Yes! VedAstro is open source (MIT license):
- **Report bugs**: GitHub Issues
- **Improve docs**: Submit pull requests
- **Add examples**: Share your demo scripts
- **Spread the word**: Tell other developers!

> **Note:** `vedastro/calculate.py` is auto-generated. Don't edit it directly.

---

### Q: Is VedAstro maintained actively?

**A:** Yes!
- Regular updates and bug fixes
- New features added based on user requests
- 99.9% uptime SLA
- Active community support

Check [GitHub commits](https://github.com/VedAstro/VedAstro) for recent activity.

---

## Comparisons

### Q: How does VedAstro compare to other astrology libraries?

**A:**

| Feature | VedAstro | Astro-API | AstrologyAPI | Swiss Ephemeris (direct) |
|---------|----------|-----------|--------------|--------------------------|
| **Price** | $1/month | $50/month | $100/month | Free (but complex setup) |
| **Setup** | Zero | Medium | Medium | Very complex |
| **Calculations** | 596+ | ~100 | ~150 | Unlimited (but requires coding) |
| **Ayanamsa** | 47 | 3-5 | 5-10 | 47+ (need to implement) |
| **Cloud-powered** | ✅ | ✅ | ✅ | ❌ (local only) |
| **Beginners** | Very easy | Medium | Medium | Very hard |

---

### Q: Why is VedAstro so cheap?

**A:** We're a non-profit focused on accessibility:
- No investors or shareholders
- User-funded model
- Minimal overhead costs
- Mission: Make Vedic astrology accessible to all developers

---

## Still Have Questions?

- 📖 Check [README.md](README.md) for full documentation
- 🚀 Read [QUICKSTART.md](QUICKSTART.md) for quick setup
- 🎓 See [TUTORIALS.md](TUTORIALS.md) for step-by-step guides
- 💬 Join [Telegram](https://t.me/vedastro_org) for community support
- 📧 Email contact@vedastro.org for direct help

---

<p align="center">
  <strong>Happy coding! 🪐</strong><br>
  <a href="README.md">README</a> •
  <a href="QUICKSTART.md">Quick Start</a> •
  <a href="TUTORIALS.md">Tutorials</a> •
  <a href="https://vedastro.org">Website</a>
</p>
