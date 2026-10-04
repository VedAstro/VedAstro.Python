"""
DEMO: Numerology Calculator (Chaldean System)
USE CASE: Birth number, destiny number and name-number predictions
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- Which numerology values the API exposes
- How the Chaldean name number is calculated
- How to compare several spellings of a name

PREREQUISITES:
- pip install vedastro

RUN:
python demo_numerology_calculator.py

EXPECTED OUTPUT (values depend on the input):
  Birth number   : 7
  Destiny number : 2
  John Doe -> number 34 (root 7, ruling planet Ketu)
"""

import json
import re

from vedastro import *

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Person Details
person_name = "John Doe"
birth_time = "14:30 25/10/1992 +05:30"
birth_location = GeoLocation("Mumbai", 72.8777, 19.0760)

birth = Time(birth_time, birth_location)

print(f"Numerology for {person_name}")
print("-" * 50)

# Step 3: Numbers From The Birth Date
# BirthNumber and DestinyNumber come from the birth date alone.
birth_number = Calculate.BirthNumber(birth)
destiny_number = Calculate.DestinyNumber(birth)

print(f"Birth number   : {birth_number}")
print(f"Destiny number : {destiny_number}")

# Step 4: Name Number (Chaldean System)
# The name number comes from the letters of the name; the API also reports
# the ruling planet and an interpretation.
print("-" * 50)
print("Name number (Chaldean system)")

prediction = Calculate.NameNumberPrediction(person_name)

print(f"Name           : {person_name}")
print(f"Number         : {prediction['Number']}")
print(f"Root number    : {prediction['RootNumber']}")
print(f"Ruling planet  : {prediction['Planet']}")

# 'Prediction' is HTML formatted, so strip the tags for plain terminal text.
plain_interpretation = re.sub(r"<[^>]+>", "", str(prediction['Prediction']))
print(f"Interpretation : {plain_interpretation[:400]}")

# Step 5: Compare Name Spellings
# A small spelling change shifts the name number, which is the usual way to
# compare a legal name against a nickname or a business name.
print("-" * 50)
print("Comparing name spellings")

# NOTE: the free tier allows 5 calls per minute and each entry below costs one
# call (the two birth numbers above already used two). Keep this list short, or
# sleep ~13 seconds between entries, or use a premium key from vedastro.org/API.html
names_to_test = [
    "John Doe",   # legal name
    "Jon Doe",    # spelling variation
]

comparison = {}
for candidate in names_to_test:
    result = Calculate.NameNumberPrediction(candidate)
    comparison[candidate] = {
        "number": result["Number"],
        "root_number": result["RootNumber"],
        "planet": result["Planet"],
    }
    print(f"  {candidate:<16} number {result['Number']:<4} "
          f"root {result['RootNumber']:<4} ruling planet {result['Planet']}")

# Step 6: Save The Report
report = {
    "name": person_name,
    "birth_number": birth_number,
    "destiny_number": destiny_number,
    "name_number": {
        "number": prediction["Number"],
        "root_number": prediction["RootNumber"],
        "planet": prediction["Planet"],
    },
    "name_comparison": comparison,
}

with open('numerology_report.json', 'w') as handle:
    json.dump(report, handle, indent=2)

print("-" * 50)
print("Full report saved to: numerology_report.json")

# NEXT STEPS
# 1. Try different spellings of the same name and compare the numbers
# 2. Calculate for family members, or for business / brand names
# 3. Combine with the birth chart, for example:
#    Calculate.PlanetRasiD1Sign(PlanetName.Sun, birth)['Name']
