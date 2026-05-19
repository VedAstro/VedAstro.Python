"""
DEMO: Numerology Calculator (Chaldean System)
USE CASE: Get numerology analysis for a name with life aspect scores
DIFFICULTY: Beginner

WHAT YOU'LL LEARN:
- How to calculate numerology for names
- How the Chaldean numerology system works
- How to interpret life aspect scores
- Which life areas numerology can predict

PREREQUISITES:
- pip install vedastro

RUN:
python demo_numerology_calculator.py

EXPECTED OUTPUT:
🔢 Numerology Report for John Doe
Born: 25 October 1992

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Life Aspect Scores (0-100)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💰 Finance:        72/100
💑 Romance:        85/100
📚 Education:      68/100
...
"""

from vedastro import *
import json

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

# Step 2: Define Person Details
# Numerology requires name and birth date
person_name = "John Doe"
birth_time = "14:30 25/10/1992 +05:30"
birth_location = GeoLocation("Mumbai", 72.8777, 19.0760)

# Create time object
birth = Time(birth_time, birth_location)

# Step 3: Calculate Numerology Report
# The Chaldean system is used (ancient Babylonian numerology)
# It analyzes the vibrations of your name and birth date
print("⏳ Calculating numerology... (this may take a few seconds)\n")

numerology_report = Calculate.NumerologyReport(person_name, birth)

# Step 4: Display Header
print(f"🔢 Numerology Report for {person_name}")
print(f"Born: {birth.GetStdDateTimeOffsetText()}\n")
print("━" * 50)
print("Life Aspect Scores (0-100)")
print("━" * 50)

# Step 5: Display Life Aspect Scores
# Numerology predicts various life areas based on name vibrations
# Higher scores = more favorable outcomes in that area

# Store scores for summary
scores = {}

for aspect in numerology_report['LifeAspectList']:
    name = aspect['Name']
    score = aspect['Score']
    description = aspect['Description']

    # Store for later
    scores[name] = score

    # Choose emoji based on life aspect
    emoji_map = {
        'Finance': '💰',
        'Romance': '💑',
        'Education': '📚',
        'Health': '🏥',
        'Family': '👨‍👩‍👧‍👦',
        'Growth': '📈',
        'Career': '💼',
        'Reputation': '⭐',
        'Spirituality': '🕉️',
        'Luck': '🍀'
    }

    emoji = emoji_map.get(name, '📊')

    # Color-code the score
    if score >= 80:
        rating = "Excellent"
    elif score >= 60:
        rating = "Good"
    elif score >= 40:
        rating = "Average"
    else:
        rating = "Needs attention"

    print(f"{emoji} {name:<15} {score}/100  ({rating})")

# Step 6: Display Strengths and Weaknesses
print("\n━" * 50)
print("Analysis Summary")
print("━" * 50)

# Find top 3 strengths (highest scores)
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
strengths = sorted_scores[:3]
weaknesses = sorted_scores[-3:]

print("\n✨ Top Strengths:")
for aspect, score in strengths:
    print(f"  • {aspect}: {score}/100")

print("\n⚠️  Areas to Focus On:")
for aspect, score in weaknesses:
    print(f"  • {aspect}: {score}/100")

# Step 7: Calculate Name Numbers (Core Numbers)
# These are the fundamental numerology numbers
print("\n━" * 50)
print("Core Numbers (from name)")
print("━" * 50)

# Get individual number breakdowns
name_details = numerology_report.get('NameDetails', {})

if name_details:
    print(f"\n📝 Name: {person_name}")

    # Destiny Number (from full name)
    if 'DestinyNumber' in name_details:
        destiny = name_details['DestinyNumber']
        print(f"  Destiny Number: {destiny}")
        print(f"  (Your life purpose and potential)")

    # Soul Urge Number (from vowels)
    if 'SoulUrgeNumber' in name_details:
        soul_urge = name_details['SoulUrgeNumber']
        print(f"  Soul Urge Number: {soul_urge}")
        print(f"  (Your inner desires and motivations)")

    # Personality Number (from consonants)
    if 'PersonalityNumber' in name_details:
        personality = name_details['PersonalityNumber']
        print(f"  Personality Number: {personality}")
        print(f"  (How others perceive you)")

# UNDERSTANDING THE CHALDEAN SYSTEM
print("\n━" * 50)
print("About Chaldean Numerology")
print("━" * 50)

print("""
📖 The Chaldean system is one of the oldest numerology systems,
   dating back to ancient Babylon (modern-day Iraq).

🔢 Number-Letter Correspondence:
   1 = A, I, J, Q, Y
   2 = B, K, R
   3 = C, G, L, S
   4 = D, M, T
   5 = E, H, N, X
   6 = U, V, W
   7 = O, Z
   8 = F, P

   Note: Number 9 is considered sacred and not assigned to letters

🎯 What It Measures:
   - Name vibrations and their influence on your life
   - Compatibility between name and birth date
   - Strengths in various life aspects (finance, romance, etc.)
   - Karmic influences and life lessons

💡 How to Use:
   - Check which life aspects have low scores
   - Consider name changes or corrections for improvement
   - Use favorable numbers in important decisions
   - Understand your natural talents and challenges
""")

# PRACTICAL APPLICATIONS
print("\n━" * 50)
print("Practical Applications")
print("━" * 50)

print("""
✅ Business: Choose company names with high Finance scores
✅ Babies: Select names with balanced life aspect scores
✅ Relationships: Check Romance and Family scores before marriage
✅ Career: Names with high Career and Reputation scores help professional growth
✅ Education: High Education scores indicate academic success

⚠️  Important Notes:
- Numerology is guidance, not destiny
- Low scores can be improved with effort and awareness
- Consider name corrections (spelling changes) for better vibrations
- Multiple factors influence life outcomes, not just numbers
""")

# BONUS: Save Report to File
print("\n💾 Saving full report to file...\n")

with open('numerology_report.json', 'w') as f:
    json.dump(numerology_report, f, indent=2)

print("✅ Full report saved to: numerology_report.json")

# NEXT STEPS
print("\n━" * 50)
print("Next Steps")
print("━" * 50)

print("""
1. Try different name spellings to see score changes
2. Calculate for multiple family members
3. Use for baby name selection
4. Compare names before choosing business/brand names
5. Check name compatibility with birth chart: Calculate.HoroscopePredictions()
""")

# CUSTOMIZATION IDEAS
print("\n💡 Customization Ideas:\n")
print("1. Build a web app for name analysis")
print("2. Create a baby name suggestion tool based on desired scores")
print("3. Add name change recommendations for low scores")
print("4. Compare multiple name variations side-by-side")
print("5. Integrate with birth chart analysis for complete profile")

# COMMON QUESTIONS
print("\n❓ Common Questions:\n")

print("Q: Can I change my name to improve scores?")
print("A: Yes! Even small spelling changes can shift vibrations.")
print("   Try different variations and compare scores.\n")

print("Q: Which number system is most accurate?")
print("A: Chaldean is considered most accurate by many numerologists")
print("   because it's based on sound vibrations, not alphabetical order.\n")

print("Q: Do nicknames matter?")
print("A: Yes! The name you use most frequently has the strongest influence.")
print("   Calculate for both legal name and nickname.\n")

print("Q: What if I have low scores in important areas?")
print("A: Options:")
print("   - Conscious effort to improve (awareness is half the battle)")
print("   - Name correction (spelling variation)")
print("   - Use favorable numbers in daily life (phone, address, etc.)")
print("   - Combine with other tools (astrology, gemstones, mantras)\n")

# BONUS: Try Multiple Names
print("\n🔄 Want to try multiple names? Here's how:\n")

print("""
names_to_test = [
    "John Doe",
    "John David Doe",  # With middle name
    "Jon Doe",         # Spelling variation
    "J. Doe",          # Initial
]

for name in names_to_test:
    report = Calculate.NumerologyReport(name, birth)
    finance_score = [a['Score'] for a in report['LifeAspectList'] if a['Name'] == 'Finance'][0]
    print(f"{name:<20} Finance: {finance_score}/100")
""")

# EXAMPLE: Quick Name Comparison
print("\n📊 Example - Quick Comparison:\n")

test_names = [
    "John Doe",
    "Jon Doe",
]

print(f"{'Name':<20} {'Finance':<10} {'Romance':<10} {'Career':<10}")
print("─" * 50)

for test_name in test_names:
    report = Calculate.NumerologyReport(test_name, birth)

    # Extract specific scores
    finance = [a['Score'] for a in report['LifeAspectList'] if a['Name'] == 'Finance'][0]
    romance = [a['Score'] for a in report['LifeAspectList'] if a['Name'] == 'Romance'][0]
    career = [a['Score'] for a in report['LifeAspectList'] if a['Name'] == 'Career'][0]

    print(f"{test_name:<20} {finance:<10} {romance:<10} {career:<10}")

print("\n✨ Numerology analysis complete!")
