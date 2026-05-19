"""
DEMO: Batch Processing Multiple Charts
USE CASE: Efficiently process hundreds of birth charts (for research, app data, etc.)
DIFFICULTY: Advanced

WHAT YOU'LL LEARN:
- How to process multiple charts efficiently
- How to respect rate limits (free tier)
- How to save results to CSV/JSON
- How to handle errors in batch processing
- How to show progress for long operations

PREREQUISITES:
- pip install vedastro

RUN:
python demo_batch_processing.py

EXPECTED OUTPUT:
🔄 Batch Processing 10 Charts
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Progress: [████████░░] 80% (8/10 charts)
Estimated time remaining: 24 seconds
...
"""

from vedastro import *
import time
import json
import csv
from datetime import datetime

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

print("🔄 Batch Processing Demo\n")
print("━" * 60)

# Step 2: Prepare Sample Data
# In production, this would come from a database, CSV file, or API
sample_charts = [
    {"name": "Person 1", "time": "14:30 25/10/1992 +05:30", "location": "Mumbai", "long": 72.8777, "lat": 19.0760},
    {"name": "Person 2", "time": "09:00 01/01/1990 -05:00", "location": "New York", "long": -74.006, "lat": 40.7128},
    {"name": "Person 3", "time": "23:00 15/08/1985 +09:00", "location": "Tokyo", "long": 139.83, "lat": 35.65},
    {"name": "Person 4", "time": "11:30 12/06/1988 +00:00", "location": "London", "long": -0.1278, "lat": 51.5074},
    {"name": "Person 5", "time": "16:45 20/03/1995 +08:00", "location": "Singapore", "long": 103.8198, "lat": 1.3521},
    {"name": "Person 6", "time": "08:15 05/11/1987 -08:00", "location": "Los Angeles", "long": -118.2437, "lat": 34.0522},
    {"name": "Person 7", "time": "13:20 18/07/1991 +01:00", "location": "Paris", "long": 2.3522, "lat": 48.8566},
    {"name": "Person 8", "time": "19:40 22/09/1993 +10:00", "location": "Sydney", "long": 151.2093, "lat": -33.8688},
    {"name": "Person 9", "time": "07:50 30/12/1989 +03:00", "location": "Dubai", "long": 55.2708, "lat": 25.2048},
    {"name": "Person 10", "time": "21:10 14/04/1994 -03:00", "location": "São Paulo", "long": -46.6333, "lat": -23.5505},
]

# APPROACH 1: Simple Sequential Processing
print("📋 APPROACH 1: Simple Sequential Processing\n")
print("Use this for small batches (<10 charts)\n")

def simple_batch_process(charts_list, delay_seconds=12):
    """Process charts one by one with delays for rate limiting"""

    results = []
    total = len(charts_list)

    print(f"Processing {total} charts (estimated time: {total * delay_seconds} seconds)\n")

    for i, chart in enumerate(charts_list):
        try:
            # Create location and time objects
            location = GeoLocation(chart['location'], chart['long'], chart['lat'])
            birth = Time(chart['time'], location)

            # Calculate sun sign
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

            # Store result
            results.append({
                "name": chart['name'],
                "location": chart['location'],
                "sun_sign": sun_sign,
                "success": True,
                "error": None
            })

            print(f"✅ {i+1}/{total} - {chart['name']}: {sun_sign}")

        except Exception as e:
            results.append({
                "name": chart['name'],
                "location": chart['location'],
                "sun_sign": None,
                "success": False,
                "error": str(e)
            })
            print(f"❌ {i+1}/{total} - {chart['name']}: Error - {e}")

        # Rate limiting: Free tier = 5 req/min = 12 seconds between requests
        if i < total - 1:  # Don't sleep after last request
            # Show a simple progress indicator
            print(f"   ⏳ Waiting {delay_seconds} seconds (rate limit)...")
            time.sleep(delay_seconds)

    return results

# Process first 3 charts (to save time in demo)
print("Demo: Processing first 3 charts only\n")
results = simple_batch_process(sample_charts[:3])

print(f"\n✅ Completed! {len(results)} charts processed")
print(f"   Success: {sum(1 for r in results if r['success'])}")
print(f"   Failed: {sum(1 for r in results if not r['success'])}")

# APPROACH 2: With Progress Bar
print("\n━" * 60)
print("📋 APPROACH 2: Progress Bar (Better UX)\n")
print("Use this for larger batches to show progress\n")

def batch_process_with_progress(charts_list, delay_seconds=12):
    """Process with visual progress bar"""

    results = []
    total = len(charts_list)
    start_time = time.time()

    print(f"🔄 Processing {total} charts\n")

    for i, chart in enumerate(charts_list):
        try:
            location = GeoLocation(chart['location'], chart['long'], chart['lat'])
            birth = Time(chart['time'], location)
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

            results.append({
                "name": chart['name'],
                "sun_sign": sun_sign,
                "success": True
            })

            # Calculate progress
            progress = (i + 1) / total
            bar_length = 40
            filled_length = int(bar_length * progress)
            bar = '█' * filled_length + '░' * (bar_length - filled_length)

            # Calculate time estimates
            elapsed = time.time() - start_time
            if i > 0:
                avg_time_per_chart = elapsed / (i + 1)
                remaining_charts = total - (i + 1)
                estimated_remaining = remaining_charts * (avg_time_per_chart + delay_seconds)
            else:
                estimated_remaining = total * delay_seconds

            # Print progress bar (overwrite previous line)
            print(f"\rProgress: [{bar}] {progress*100:.0f}% ({i+1}/{total}) | "
                  f"ETA: {int(estimated_remaining)}s", end='', flush=True)

        except Exception as e:
            results.append({"name": chart['name'], "sun_sign": None, "success": False})

        # Rate limiting
        if i < total - 1:
            time.sleep(delay_seconds)

    print()  # New line after progress bar
    return results

# Demo with 3 charts
print("Demo: Processing with progress bar (3 charts)\n")
results_with_progress = batch_process_with_progress(sample_charts[:3])

# APPROACH 3: Save Results to CSV
print("\n━" * 60)
print("📋 APPROACH 3: Save Results to CSV\n")
print("Use this to export data for Excel, Google Sheets, analysis\n")

def batch_process_and_save_csv(charts_list, filename="birth_charts.csv"):
    """Process charts and save to CSV file"""

    results = []

    # Process charts
    for i, chart in enumerate(charts_list):
        try:
            location = GeoLocation(chart['location'], chart['long'], chart['lat'])
            birth = Time(chart['time'], location)

            # Get multiple calculations
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
            moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth)
            ascendant = Calculate.HouseSignName(HouseName.House1, birth)

            results.append({
                "Name": chart['name'],
                "BirthTime": chart['time'],
                "Location": chart['location'],
                "SunSign": sun_sign,
                "MoonSign": moon_sign,
                "Ascendant": ascendant,
                "Success": "Yes"
            })

            print(f"✅ {chart['name']}: Sun={sun_sign}, Moon={moon_sign}, Asc={ascendant}")

        except Exception as e:
            results.append({
                "Name": chart['name'],
                "BirthTime": chart['time'],
                "Location": chart['location'],
                "SunSign": "Error",
                "MoonSign": "Error",
                "Ascendant": "Error",
                "Success": "No"
            })
            print(f"❌ {chart['name']}: Error")

        # Rate limiting (skip for demo)
        # if i < len(charts_list) - 1:
        #     time.sleep(12)

    # Save to CSV
    if results:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = results[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"\n💾 Results saved to: {filename}")

    return results

# Demo with first 2 charts (to save API calls)
print("Demo: Processing and saving to CSV (2 charts)\n")
csv_results = batch_process_and_save_csv(sample_charts[:2], "demo_charts.csv")

# APPROACH 4: Save Results to JSON
print("\n━" * 60)
print("📋 APPROACH 4: Save Results to JSON\n")
print("Use this for structured data, API responses, databases\n")

def batch_process_and_save_json(charts_list, filename="birth_charts.json"):
    """Process charts and save to JSON file"""

    results = {
        "metadata": {
            "total_charts": len(charts_list),
            "processed_at": datetime.now().isoformat(),
            "api_tier": "Free"
        },
        "charts": []
    }

    for chart in charts_list:
        try:
            location = GeoLocation(chart['location'], chart['long'], chart['lat'])
            birth = Time(chart['time'], location)

            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
            moon_sign = Calculate.PlanetSignName(PlanetName.Moon, birth)

            results["charts"].append({
                "name": chart['name'],
                "birth_time": chart['time'],
                "location": chart['location'],
                "coordinates": {
                    "longitude": chart['long'],
                    "latitude": chart['lat']
                },
                "signs": {
                    "sun": sun_sign,
                    "moon": moon_sign
                },
                "success": True,
                "error": None
            })

            print(f"✅ {chart['name']}: Processed")

        except Exception as e:
            results["charts"].append({
                "name": chart['name'],
                "success": False,
                "error": str(e)
            })
            print(f"❌ {chart['name']}: Error")

    # Save to JSON
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(results, jsonfile, indent=2)

    print(f"\n💾 Results saved to: {filename}")

    return results

# Demo with first 2 charts
print("Demo: Processing and saving to JSON (2 charts)\n")
json_results = batch_process_and_save_json(sample_charts[:2], "demo_charts.json")

# APPROACH 5: Error Recovery (Resume from failure)
print("\n━" * 60)
print("📋 APPROACH 5: Error Recovery (Resume interrupted batches)\n")
print("Use this for very large batches that may get interrupted\n")

def batch_process_with_checkpoints(charts_list, checkpoint_file="checkpoint.json"):
    """Process with ability to resume from interruption"""

    # Load checkpoint if exists
    try:
        with open(checkpoint_file, 'r') as f:
            checkpoint = json.load(f)
            results = checkpoint['results']
            start_index = checkpoint['last_processed_index'] + 1
            print(f"📌 Resuming from checkpoint: {start_index}/{len(charts_list)}")
    except FileNotFoundError:
        results = []
        start_index = 0
        print(f"🆕 Starting fresh batch")

    # Process from start_index onwards
    for i in range(start_index, len(charts_list)):
        chart = charts_list[i]

        try:
            location = GeoLocation(chart['location'], chart['long'], chart['lat'])
            birth = Time(chart['time'], location)
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

            results.append({
                "name": chart['name'],
                "sun_sign": sun_sign,
                "success": True
            })

            print(f"✅ {i+1}/{len(charts_list)} - {chart['name']}")

        except Exception as e:
            results.append({"name": chart['name'], "success": False, "error": str(e)})
            print(f"❌ {i+1}/{len(charts_list)} - {chart['name']}: Error")

        # Save checkpoint after each successful process
        checkpoint = {
            "last_processed_index": i,
            "results": results
        }
        with open(checkpoint_file, 'w') as f:
            json.dump(checkpoint, f, indent=2)

        # Rate limiting (skip for demo)
        # time.sleep(12)

    # Clean up checkpoint file when done
    import os
    if os.path.exists(checkpoint_file):
        os.remove(checkpoint_file)
        print(f"\n✅ Batch complete! Checkpoint file removed.")

    return results

# Demo
print("Demo: Processing with checkpoints (2 charts)\n")
checkpoint_results = batch_process_with_checkpoints(sample_charts[:2], "demo_checkpoint.json")

# BEST PRACTICES SUMMARY
print("\n━" * 60)
print("✅ Batch Processing Best Practices")
print("━" * 60)

print("""
1. RATE LIMITING (Critical for free tier)
   - Free tier: 5 requests/minute
   - Add 12-second delays: time.sleep(12)
   - For premium: No delays needed!

2. ERROR HANDLING
   - Wrap each chart in try-catch
   - Log errors with chart details
   - Continue processing even if one chart fails

3. PROGRESS TRACKING
   - Show progress bar for large batches
   - Display estimated time remaining
   - Let users know it's working

4. CHECKPOINTS
   - Save progress periodically
   - Resume from interruptions
   - Don't lose work due to crashes/network issues

5. OUTPUT FORMATS
   - CSV: For Excel, Google Sheets, data analysis
   - JSON: For databases, APIs, structured data
   - Both: For maximum flexibility

6. BATCH SIZE
   - Small batches (< 10): Simple sequential processing
   - Medium batches (10-100): Progress bar + checkpoints
   - Large batches (> 100): Consider premium tier for speed

7. DATA VALIDATION
   - Validate ALL inputs before processing
   - Skip invalid entries with error logging
   - Don't let bad data crash entire batch

8. PERFORMANCE
   - Free tier: ~5 charts/minute (12s per chart)
   - Premium tier: ~60 charts/minute (1s per chart)
   - For 1000 charts:
     - Free: ~3.3 hours
     - Premium: ~17 minutes
""")

# EXAMPLE USE CASES
print("\n━" * 60)
print("💡 Real-World Use Cases")
print("━" * 60)

print("""
1. DATING APP
   - Import user birth data from database
   - Calculate compatibility scores for all users
   - Save results for quick matching
   - Update daily for new users

2. ASTROLOGY WEBSITE
   - Process user sign-ups
   - Generate horoscope reports in bulk
   - Cache results for fast page loads
   - Re-process monthly for transit updates

3. RESEARCH PROJECT
   - Analyze 1000s of celebrity charts
   - Extract patterns and correlations
   - Export to CSV for statistical analysis
   - Compare different ayanamsa systems

4. FAMILY TREE APP
   - Import family members from GEDCOM file
   - Calculate charts for all members
   - Generate family astrological tree
   - Show generational patterns

5. BUSINESS ANALYTICS
   - Analyze company founding dates
   - Check employee birth charts
   - Find auspicious business timings
   - Track planetary cycles for planning
""")

print("\n✨ Batch processing demonstration complete!")
print("\n📁 Files created:")
print("   - demo_charts.csv (CSV export)")
print("   - demo_charts.json (JSON export)")
print("\n💡 Tip: For production batches > 100 charts, upgrade to premium ($1/month)")
print("   to remove rate limits and process 12x faster!")
