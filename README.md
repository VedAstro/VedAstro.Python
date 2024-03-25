<h1> ✨ Vedic Astrology in Python</h1>

[![License](https://img.shields.io/github/license/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/blob/main/LICENSE)
[![GitHub Issues](https://img.shields.io/github/issues/VedAstro/VedAstro.Python)](https://github.com/VedAstro/VedAstro.Python/issues)


# 🗺️ What can this do?
Easily code complex vedic astrology math and logic.
A powerful tool for astronomical calculations and data analysis. It provides a collection of functions and classes to perform various astronomical calculations, such as celestial object positions, time conversions, coordinate transformations, and more.


# 🏎️ Quick Start
**Step 1:** Download and install .NET 7 Runtime ([How?](#net-7-download--install))

**Step 2:** Run `pip install vedastro`

**Step 3:** Do astro calculation in less than 10 lines
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
Tools.Print(allPlanetDataList)

#HOUSES
allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)
Tools.Print(allHouseDataList)

#ZODIAC SIGNS
allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)
Tools.Print(allZodiacDataList)
```

# ⚙️ How it works
Coded & compiled [in C#](https://github.com/VedAstro/VedAstro) for **maximum CPU computation efficency and speed**,
then wrapped in Python .NET Core CLR wrapper. Can be run in Linux, Windows & Mac OS.


-------------------

## .NET 7 Download & Install
<a name="net7"></a>
[Download .NET 7 for Windows](https://dotnet.microsoft.com/en-us/download/dotnet/thank-you/sdk-7.0.400-windows-x64-installer)

Download .NET 7 for Ubuntu
```
sudo apt-get update && \
sudo apt-get install -y dotnet-sdk-7.0
```

## DESIGN NOTES
- Vedastro Lib code is compiled into VedAstro.dll (Release always) and injected into this python code base
- All calls needing location data both local or production python server, will contact Live vedastro API server
- custom 3rd party API keys not supported as in C# version

## Contributing

Contributions to VedAstro Python are welcome! If you find a bug, have a feature request, or want to contribute code, please open an issue or submit a pull request. Make sure to read our [contribution guidelines](https://github.com/VedAstro/VedAstro.Python/CONTRIBUTING.md) before getting started.

## License

VedAstro Python is released under the MIT License. See [LICENSE](https://github.com/VedAstro/VedAstro.Python/LICENSE) for more information.


