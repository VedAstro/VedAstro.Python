# VedAstro Python Quick Start (2 Minutes)

Get your first Vedic astrology calculation running in under 2 minutes!

---

## Step 1: Install (10 seconds)

```bash
pip install vedastro
```

That's it! No C++ compilers, no ephemeris files, no configuration needed.

---

## Step 2: Run Your First Calculation (30 seconds)

Create a file called `test.py`:

```python
from vedastro import *

# Set API key (free tier)
Calculate.SetAPIKey('FreeAPIUser')

# Define birth time
birth = Time("14:30 25/10/1992 +05:30",
             GeoLocation("Mumbai", 72.8777, 19.0760))

# Get Sun sign
sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

print(f"Sun Sign: {sun_sign}")
```

Run it:
```bash
python test.py
```

**Output:**
```
Sun Sign: Libra
```

🎉 **You just made your first Vedic astrology calculation!**

---

## Step 3: Explore Examples (80 seconds)

Try the ready-to-run demo files:

```bash
# Simplest example (5 lines)
python demo_quick_start.py

# Get Sun/Moon/Ascendant
python demo_birth_chart_basics.py

# Check marriage compatibility
python demo_marriage_compatibility.py

# Today's planetary positions
python demo_current_planets.py

# Daily panchanga (Tithi, Nakshatra)
python demo_daily_panchanga.py
```

---

## What's Next?

1. **📖 Read README.md** - See all 596 calculations and features
2. **🎓 Try Tutorials** - [TUTORIALS.md](TUTORIALS.md) for step-by-step guides
3. **❓ Check FAQ** - [FAQ.md](FAQ.md) for common questions
4. **🚀 Build Something** - Your first horoscope app!
5. **💰 Upgrade** - $1/month unlimited at [vedastro.org/API.html](https://vedastro.org/API.html)

---

## Need Help?

- **Documentation**: [vedastro.org/API.html](https://vedastro.org/API.html)
- **Issues**: [GitHub Issues](https://github.com/VedAstro/VedAstro.Python/issues)
- **Telegram**: [t.me/vedastro_org](https://t.me/vedastro_org)

---

**You're ready to build! 🪐**

<p align="center">
  <a href="README.md">Full README</a> •
  <a href="TUTORIALS.md">Tutorials</a> •
  <a href="FAQ.md">FAQ</a> •
  <a href="https://vedastro.org">Website</a>
</p>
