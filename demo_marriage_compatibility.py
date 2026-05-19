"""
DEMO: Marriage Compatibility Checker
USE CASE: Check if two people are compatible for marriage using Vedic Kuta system
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- How to compare two birth charts
- How to get 16-factor Kuta compatibility analysis
- How to interpret compatibility scores
- What each Kuta factor means

PREREQUISITES:
- pip install vedastro

RUN:
python demo_marriage_compatibility.py

EXPECTED OUTPUT:
💑 Marriage Compatibility Report

Person 1: 31 December 1996, 23:40, Tokyo
Person 2: 15 June 1997, 14:30, New York

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Overall Compatibility: 65.0/100
Status: Good match - Near perfect match, overall happiness
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

16-Factor Kuta Analysis:
✅ Graha Maitram: Good (Mental compatibility)
✅ Rajju: Good (Longevity of marriage)
✅ Nadi Kuta: Good (Health & progeny)
...
"""

from vedastro import *
import json

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Person 1's Birth Details
# Example: A person born in Tokyo, Japan
person1_time = "23:40 31/12/1996 +09:00"  # 11:40 PM JST
person1_location = GeoLocation("Tokyo", 139.83, 35.65)
person1_birth = Time(person1_time, person1_location)

# Step 3: Define Person 2's Birth Details
# Example: A person born in New York, USA
person2_time = "14:30 15/06/1997 -05:00"  # 2:30 PM EST
person2_location = GeoLocation("New York", -74.006, 40.7128)
person2_birth = Time(person2_time, person2_location)

# Step 4: Get Match Report
# This performs a comprehensive 16-factor Kuta compatibility analysis
# The report includes:
# - Overall Kuta score (out of 100)
# - Individual Kuta factors (Graha Maitram, Yoni, Nadi, etc.)
# - Detailed predictions for marriage life
# - Dosha checks (Kuja Dosha/Manglik, etc.)
print("⏳ Calculating compatibility... (this may take a few seconds)\n")

match_report = Calculate.MatchReport(person1_birth, person2_birth)

# Step 5: Display Overall Compatibility
print("💑 Marriage Compatibility Report\n")
print(f"Person 1: {person1_time}, {person1_location.Name()}")
print(f"Person 2: {person2_time}, {person2_location.Name()}\n")
print("━" * 50)

# Get overall score (Kuta score out of 36 is normalized to 100)
kuta_score = match_report['KutaScore']
print(f"Overall Compatibility: {kuta_score}/100")

# Get summary assessment
summary = match_report['Summary']['ScoreSummary']
print(f"Status: {summary}")
print("━" * 50)

# Step 6: Display Individual Kuta Factors
print("\n16-Factor Kuta Analysis:\n")

# Each prediction has a 'Nature' field: Good, Bad, or Neutral
for prediction in match_report['PredictionList']:
    name = prediction['Name']
    nature = prediction['Nature']
    info = prediction['Info']

    # Use emoji to make it easy to scan
    if nature == "Good":
        emoji = "✅"
    elif nature == "Bad":
        emoji = "❌"
    else:
        emoji = "⚠️"

    print(f"{emoji} {name}: {nature}")
    print(f"   {info}\n")

# INTERPRETING THE SCORE:
# The traditional Vedic Kuta system uses 36 points maximum:
# - 33-36 points = Excellent compatibility (91-100%)
# - 25-32 points = Good compatibility (69-89%)
# - 18-24 points = Average compatibility (50-67%)
# - Below 18 = Poor compatibility (below 50%)
#
# However, modern interpretation also considers:
# - Individual Kuta factors (some are more important than others)
# - Nadi Kuta = Most important (health & progeny)
# - Yoni Kuta = Sexual compatibility
# - Graha Maitram = Mental harmony

# IMPORTANT NOTES:
# 1. Vedic compatibility is not deterministic - it shows potential, not destiny
# 2. A "bad" score doesn't mean the marriage will fail
# 3. A "good" score doesn't guarantee success
# 4. Other factors matter: communication, values, goals, effort
# 5. Use this as one input among many, not the sole decision maker

# NEXT STEPS:
# - Save report to file: with open('match_report.json', 'w') as f: json.dump(match_report, f, indent=2)
# - Compare multiple potential matches
# - Get detailed dasa analysis: Calculate.DasaAtRange()
# - Check individual horoscopes: Calculate.HoroscopePredictions()

# BONUS: Extract specific Kuta scores
print("\n🎯 Key Compatibility Factors:\n")

# Find specific Kutas
for prediction in match_report['PredictionList']:
    name = prediction['Name']

    # Highlight the most important ones
    if name in ['Nadi Kuta', 'Graha Maitram', 'Yoni Kuta', 'Rajju']:
        score_text = prediction.get('Score', 'N/A')
        print(f"  • {name}: {prediction['Nature']} ({score_text})")

# CUSTOMIZATION IDEAS:
# 1. Create a web app that accepts two birth details and shows match report
# 2. Generate a PDF report with the compatibility analysis
# 3. Compare multiple potential matches and rank them
# 4. Add charts showing which areas are strong vs weak
# 5. Integrate with a dating app to auto-match compatible people

# COMMON QUESTIONS:
# Q: What if we don't have exact birth times?
# A: Try birth time rectification: Calculate.BirthTimeAutoAIFill()
#    Or use noon (12:00) as an approximation (less accurate)
#
# Q: What if the score is low but we love each other?
# A: Love and compatibility are different. A low score shows challenges,
#    but conscious effort can overcome them. Use the report to understand
#    potential friction points and work on them.
#
# Q: Can I get compatibility for friendship, not marriage?
# A: Yes! The same factors apply, just interpret them for friendship context.
#    Graha Maitram (mental harmony) is especially important for friendship.
