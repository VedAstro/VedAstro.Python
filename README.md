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

## Why VedAstro?

| | |
|---|---|
| **596+ Calculations** | Planet positions, house data, divisional charts (D1–D60), yogas, dasas, and more |
| **47 Ayanamsa Systems** | Lahiri, Raman, Krishnamurti, Fagan-Bradley (Western), and 43 others |
| **Match Compatibility** | Full Kuta-based compatibility reports between two horoscopes |
| **Zero Setup** | Cloud-powered engine — just `pip install` and start calculating |
| **AI Features** | Birth time auto-fill, horoscope search by natural language |

---

## Installation

```bash
pip install vedastro
```

---

## Quick Start

### Planet Positions

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')  # get your key at vedastro.org/API.html

geo = GeoLocation("Tokyo, Japan", 139.83, 35.65)
birth_time = Time(hour=23, minute=40, day=31, month=12, year=2010, offset="+08:00", geolocation=geo)

result = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
Tools.Print(result)
```

### Match Compatibility

```python
from vedastro import *

Calculate.SetAPIKey('FreeAPIUser')

romeo = Time("23:40 31/12/1996 +08:00", GeoLocation("Tokyo, Japan", 139.83, 35.65))
juliet = Time("14:30 15/06/1997 -05:00", GeoLocation("New York, USA", -74.006, 40.7128))

match = Calculate.MatchReport(romeo, juliet)
Tools.Print(match)
```

### Vimshottari Dasa

```python
from vedastro import *
import json

Calculate.SetAPIKey('FreeAPIUser')

geo = GeoLocation("Tokyo, Japan", 139.83, 35.65)
birth_time = Time("23:40 31/12/2010 +08:00", geo)
start = Time("00:00 01/01/2020 +08:00", geo)
end = Time("23:59 31/12/2025 +08:00", geo)

dasa = Calculate.DasaAtRange(birth_time, start, end, levels=3, precision_hours=100)
print(json.dumps(dasa, indent=4))
```

---

## What Can You Calculate?

| Category | Examples | Description |
|:---------|:---------|:------------|
| **Planets** | `AllPlanetData`, `PlanetNirayanaLongitude`, `PlanetsInConjunction` | Positions, strengths, aspects, conjunctions |
| **Houses** | `AllHouseData`, `HouseSignName`, `AllHouseRasiSigns` | Bhava charts, house lords, sign placements |
| **Zodiac** | `AllZodiacSignData`, `IsPlanetInSign` | Sign-based calculations |
| **Matching** | `MatchReport`, `MatchReportWithBazi`, `MatchChat` | Kuta compatibility, AI chat analysis |
| **Events** | `EventsAtTime`, `EventsAtRange`, `EventStartTime` | Muhurtha, event predictions |
| **Dasa** | `DasaAtRange` | Vimshottari dasa periods with configurable depth |
| **AI** | `BirthTimeAutoAIFill`, `HoroscopeLLMSearch` | Machine learning birth time, natural language search |
| **Divisional** | `AllHouseNavamshaSigns`, `AllHouseDrekkanaSigns`, etc. | D1 through D60 charts |

Full API reference: [vedastro.org/API.html](https://vedastro.org/API.html)

---

## Custom Ayanamsa

By default, calculations use the **Raman** ayanamsa. Switch to any of the 47 supported systems:

```python
# Vedic — Lahiri
Calculate.SetAyanamsa(Ayanamsa.Lahiri)

# Western astrology — Fagan-Bradley
Calculate.SetAyanamsa(Ayanamsa.Fagan_Bradley)

# KP System — Krishnamurti
Calculate.SetAyanamsa(Ayanamsa.Krishnamurti)
```

---

## API Key

| Tier | Speed | How |
|:-----|:------|:----|
| **Free** | Rate limited | No key needed, or use `'FreeAPIUser'` |
| **Subscriber** | Unlimited | Get key at [vedastro.org/API.html](https://vedastro.org/API.html) |

```python
Calculate.SetAPIKey('your-key-here')
```

---

## How It Works

```
Your Python Code  →  vedastro pip library  →  REST API  →  VedAstro Engine (cloud)
```

All calculations run server-side on the VedAstro engine. No local dependencies beyond Python and `requests`. No DLLs, no native binaries, no setup.

---

## Examples

| Demo File | What It Shows |
|:----------|:-------------|
| [`demo_all_astro_data.py`](demo_all_astro_data.py) | All planet and house data for a birth chart |
| [`demo_all_astro_data_json_output.py`](demo_all_astro_data_json_output.py) | Same as above, with JSON output |
| [`demo_all_astro_data_csv.py`](demo_all_astro_data_csv.py) | Export astro data to CSV with pandas |
| [`demo_all_planet_data.py`](demo_all_planet_data.py) | Detailed planet positions with degree parsing |
| [`demo_bhava_chart_data.py`](demo_bhava_chart_data.py) | Bhava chart house signs and planet placements |
| [`demo_code_from_api_builder.py`](demo_code_from_api_builder.py) | Code generated from the API Builder tool |
| [`demo_custom_ayanamsa.py`](demo_custom_ayanamsa.py) | Using a custom ayanamsa system |
| [`demo_horoscope_prediction_names.py`](demo_horoscope_prediction_names.py) | Horoscope prediction event names |
| [`demo_match_checker.py`](demo_match_checker.py) | Match compatibility report between two charts |
| [`demo_vimshottari_dasa.py`](demo_vimshottari_dasa.py) | Vimshottari dasa periods for a time range |

---

## Contributing

Contributions welcome! Please open an issue or submit a pull request.

> **Note:** `vedastro/calculate.py` is auto-generated by the [StaticTableGenerator](https://github.com/VedAstro/VedAstro) in the main repo. Do not edit it directly.

## License

Released under the [MIT License](LICENSE).

---

<p align="center">
  <em>Made & Funded by Users — <a href="https://vedastro.org/Donate">Support VedAstro</a></em>
</p>
