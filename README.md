<h1> ✨ Vedic Astrology in Python</h1>

[![License](https://img.shields.io/github/license/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/issues)


# 🙏 How VedAstro can help you...

- [Website](https://vedastro.org) --> easy & fast astrology data for **normal users**
- [AI Astrologer](https://vedastro.org/AstrologerChat.html) --> 🤖 World's 1st open source **Vedic AI astrologer**
- [Numerology](https://vedastro.org/Numerology.html) --> Accurate Name Numerology using **Mantra Shastra**


# 🗺️ What can this do?
Easily code complex vedic astrology math and logic.
A powerful tool for astronomical calculations and data analysis. It provides a collection of functions and classes to perform various astronomical calculations, such as celestial object positions, time conversions, coordinate transformations, and more.


# 🏎️ Quick Start

**Step 1:** Run `pip install vedastro`

**Step 2:** Do astro calculation in less than 10 lines
```python
from vedastro import * 

#PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +08:00", geolocation)

#PART 2 : CALCULATE ALL DATA
#-----------------------------------

#PLANETS
allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
print(json.dumps(allPlanetDataList, indent=4))

#HOUSES
allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)
print(json.dumps(allHouseDataList, indent=4))

#ZODIAC SIGNS
allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)
print(json.dumps(allZodiacDataList, indent=4))
```

**Step 3:** Done ✅

# 🧮 +400 Calculations
![400-plus-calculation-python](https://vedastro.org/images/400-plus-calculation-python.gif)



# ⚙️ How it works
Coded & compiled [in C#](https://github.com/VedAstro/VedAstro) for **maximum CPU computation efficency and speed**, then made available in a Python wrapper. Can be run in Linux, Windows & Mac OS.


-------------------

## Contributing

Contributions to VedAstro Python are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request. Make sure to read our [contribution guidelines](https://github.com/VedAstro/VedAstro.Python/CONTRIBUTING.md) before getting started.

## License

VedAstro Python is released under the MIT License. See [LICENSE](https://github.com/VedAstro/VedAstro.Python/LICENSE) for more information.


