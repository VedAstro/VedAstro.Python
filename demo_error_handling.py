"""
DEMO: Proper Error Handling Patterns
USE CASE: Learn how to handle API errors gracefully in production code
DIFFICULTY: Intermediate

WHAT YOU'LL LEARN:
- How to catch and handle API errors
- How to validate input before making API calls
- How to implement retry logic for transient failures
- How to provide user-friendly error messages
- Best practices for production-ready code

PREREQUISITES:
- pip install vedastro

RUN:
python demo_error_handling.py

EXPECTED OUTPUT:
✅ Test 1: Valid input - Success!
❌ Test 2: Invalid time format - Caught and handled
❌ Test 3: Invalid coordinates - Caught and handled
...
"""

from vedastro import *
import time
from datetime import datetime

# Step 1: Set API Key
Calculate.SetAPIKey('FreeAPIUser')

print("🛡️ Error Handling Patterns for VedAstro\n")
print("━" * 60)

# PATTERN 1: Basic Try-Catch
print("\n📋 PATTERN 1: Basic Try-Catch\n")

print("Use this for simple operations where you just need to know if it worked:\n")

def basic_error_handling():
    """Simple try-catch pattern"""
    try:
        birth = Time("14:30 25/10/1992 +05:30",
                    GeoLocation("Mumbai", 72.8777, 19.0760))
        sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
        print(f"✅ Success! Sun Sign: {sun_sign}")
        return sun_sign
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        return None

basic_error_handling()

# PATTERN 2: Specific Error Types
print("\n━" * 60)
print("📋 PATTERN 2: Catching Specific Error Types\n")

print("Handle different types of errors differently:\n")

def specific_error_handling():
    """Catch specific error types for better handling"""
    try:
        # Intentionally invalid time format to trigger error
        birth = Time("INVALID_FORMAT", GeoLocation("Mumbai", 72.8777, 19.0760))
        sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
        print(f"✅ Success! Sun Sign: {sun_sign}")
    except ValueError as e:
        print(f"❌ ValueError: Invalid input format - {e}")
    except ConnectionError as e:
        print(f"❌ ConnectionError: Network issue - {e}")
    except TimeoutError as e:
        print(f"❌ TimeoutError: Request took too long - {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {type(e).__name__} - {e}")

specific_error_handling()

# PATTERN 3: Input Validation Before API Call
print("\n━" * 60)
print("📋 PATTERN 3: Input Validation (Prevent errors before they happen)\n")

print("Validate inputs BEFORE making API calls:\n")

def validate_and_calculate(birth_time_str, location_name, longitude, latitude):
    """Validate inputs before making API call"""

    # Validate time format
    if not isinstance(birth_time_str, str) or len(birth_time_str) < 10:
        print(f"❌ Invalid time format: {birth_time_str}")
        return None

    # Check if time string has required components
    time_parts = birth_time_str.split()
    if len(time_parts) != 3:
        print(f"❌ Time must have format: 'HH:MM DD/MM/YYYY +TZ:TZ'")
        print(f"   Got: {birth_time_str}")
        return None

    # Validate coordinates
    if not (-90 <= latitude <= 90):
        print(f"❌ Invalid latitude: {latitude} (must be -90 to 90)")
        return None

    if not (-180 <= longitude <= 180):
        print(f"❌ Invalid longitude: {longitude} (must be -180 to 180)")
        return None

    # Validate location name
    if not location_name or not isinstance(location_name, str):
        print(f"❌ Invalid location name: {location_name}")
        return None

    # All validations passed, make API call
    try:
        location = GeoLocation(location_name, longitude, latitude)
        birth = Time(birth_time_str, location)
        sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
        print(f"✅ Valid input! Sun Sign: {sun_sign}")
        return sun_sign
    except Exception as e:
        print(f"❌ API Error: {e}")
        return None

# Test cases
print("Test 1: Valid input")
validate_and_calculate("14:30 25/10/1992 +05:30", "Mumbai", 72.8777, 19.0760)

print("\nTest 2: Invalid time format")
validate_and_calculate("invalid", "Mumbai", 72.8777, 19.0760)

print("\nTest 3: Invalid latitude")
validate_and_calculate("14:30 25/10/1992 +05:30", "Mumbai", 72.8777, 95.0)

print("\nTest 4: Invalid longitude")
validate_and_calculate("14:30 25/10/1992 +05:30", "Mumbai", 200.0, 19.0760)

# PATTERN 4: Retry Logic for Transient Failures
print("\n━" * 60)
print("📋 PATTERN 4: Retry Logic (Handle temporary failures)\n")

print("Retry failed requests (useful for network issues):\n")

def calculate_with_retry(birth_time_str, location, max_retries=3, delay=2):
    """Retry API call if it fails (handles temporary network issues)"""

    for attempt in range(max_retries):
        try:
            birth = Time(birth_time_str, location)
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
            print(f"✅ Success on attempt {attempt + 1}! Sun Sign: {sun_sign}")
            return sun_sign
        except ConnectionError as e:
            print(f"⚠️  Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                print(f"   Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"❌ All {max_retries} attempts failed")
                return None
        except Exception as e:
            # Non-network errors shouldn't be retried
            print(f"❌ Non-retryable error: {e}")
            return None

location = GeoLocation("Mumbai", 72.8777, 19.0760)
calculate_with_retry("14:30 25/10/1992 +05:30", location)

# PATTERN 5: Rate Limit Handling (Free Tier)
print("\n━" * 60)
print("📋 PATTERN 5: Rate Limit Handling (Free Tier: 5 req/min)\n")

print("Handle rate limits gracefully:\n")

def batch_calculate_with_rate_limit(birth_times_list):
    """Process multiple charts while respecting rate limits"""

    results = []

    for i, (name, birth_time_str, location) in enumerate(birth_times_list):
        try:
            birth = Time(birth_time_str, location)
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)
            results.append({"name": name, "sun_sign": sun_sign, "success": True})
            print(f"✅ {name}: {sun_sign}")

            # Rate limiting: Free tier = 5 req/min = 12 seconds between requests
            if i < len(birth_times_list) - 1:  # Don't sleep after last request
                print(f"   ⏳ Waiting 12 seconds to respect rate limit...")
                time.sleep(12)

        except Exception as e:
            results.append({"name": name, "sun_sign": None, "success": False, "error": str(e)})
            print(f"❌ {name}: Error - {e}")

    return results

# Example: Process 3 charts (would take ~24 seconds total)
print("Processing 3 charts with rate limiting:\n")

charts = [
    ("Person 1", "14:30 25/10/1992 +05:30", GeoLocation("Mumbai", 72.8777, 19.0760)),
    ("Person 2", "09:00 01/01/1990 -05:00", GeoLocation("NYC", -74.006, 40.7128)),
    ("Person 3", "23:00 15/08/1985 +09:00", GeoLocation("Tokyo", 139.83, 35.65)),
]

# Uncomment to test (takes ~24 seconds):
# results = batch_calculate_with_rate_limit(charts)
# print(f"\nProcessed {len(results)} charts")

print("(Skipped actual execution to save time)")

# PATTERN 6: User-Friendly Error Messages
print("\n━" * 60)
print("📋 PATTERN 6: User-Friendly Error Messages\n")

print("Convert technical errors into helpful guidance:\n")

def get_friendly_error_message(error):
    """Convert technical error to user-friendly message"""

    error_str = str(error).lower()

    if "connection" in error_str or "network" in error_str:
        return """
🔌 Connection Error

   Problem: Can't reach VedAstro servers
   Solutions:
   1. Check your internet connection
   2. Try again in a few seconds
   3. Check if firewall is blocking port 443
"""

    elif "time" in error_str or "format" in error_str:
        return """
⏰ Time Format Error

   Problem: Birth time is in wrong format
   Solutions:
   1. Use format: "HH:MM DD/MM/YYYY +TZ:TZ"
   2. Example: "14:30 25/10/1992 +05:30"
   3. Use 24-hour format (not AM/PM)
   4. Check timezone offset is correct
"""

    elif "rate" in error_str or "limit" in error_str:
        return """
🚦 Rate Limit Exceeded

   Problem: Too many requests (free tier = 5/min)
   Solutions:
   1. Wait 60 seconds and try again
   2. Add delays: time.sleep(12) between requests
   3. Upgrade to premium ($1/month unlimited)
"""

    elif "api" in error_str or "key" in error_str:
        return """
🔑 API Key Error

   Problem: Invalid or missing API key
   Solutions:
   1. Use: Calculate.SetAPIKey('FreeAPIUser')
   2. Or get premium key from vedastro.org/API.html
   3. Check key is spelled correctly (copy-paste)
"""

    else:
        return f"""
❌ Error Occurred

   Problem: {error}
   Solutions:
   1. Check input parameters are correct
   2. Try again in a few seconds
   3. Contact support if issue persists

   Email: contact@vedastro.org
   Telegram: t.me/vedastro_org
"""

# Test friendly error messages
try:
    # Simulate an error
    raise ConnectionError("Failed to establish connection")
except Exception as e:
    print(get_friendly_error_message(e))

# PATTERN 7: Logging for Debugging
print("\n━" * 60)
print("📋 PATTERN 7: Logging (Track what happened)\n")

print("Keep logs for debugging production issues:\n")

import logging

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='vedastro_errors.log'
)

def calculate_with_logging(birth_time_str, location_name, longitude, latitude):
    """Log all operations for debugging"""

    logging.info(f"Starting calculation for {location_name}")
    logging.info(f"Input: time={birth_time_str}, long={longitude}, lat={latitude}")

    try:
        location = GeoLocation(location_name, longitude, latitude)
        birth = Time(birth_time_str, location)
        sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

        logging.info(f"Success: Sun sign = {sun_sign}")
        print(f"✅ Success! Sun Sign: {sun_sign}")
        return sun_sign

    except Exception as e:
        logging.error(f"Error: {type(e).__name__} - {e}")
        logging.error(f"Failed inputs: time={birth_time_str}, location={location_name}")
        print(f"❌ Error: {e}")
        print(f"📝 Error logged to vedastro_errors.log")
        return None

calculate_with_logging("14:30 25/10/1992 +05:30", "Mumbai", 72.8777, 19.0760)

# BEST PRACTICES SUMMARY
print("\n━" * 60)
print("✅ Best Practices Summary")
print("━" * 60)

print("""
1. ALWAYS validate inputs before API calls
   - Check time format matches "HH:MM DD/MM/YYYY +TZ:TZ"
   - Verify coordinates are in valid range
   - Ensure timezone offset is correct

2. USE try-catch blocks for ALL API calls
   - Catch specific exceptions when possible
   - Provide fallback behavior
   - Never let errors crash the application

3. IMPLEMENT rate limiting for free tier
   - 5 requests per minute maximum
   - Add 12-second delays between batch requests
   - Consider upgrading to premium for production

4. PROVIDE user-friendly error messages
   - Don't show technical jargon to end users
   - Suggest specific solutions
   - Include examples of correct format

5. LOG errors for debugging
   - Save errors to file for later analysis
   - Include timestamp and input parameters
   - Track patterns in failures

6. RETRY transient failures
   - Network issues are temporary
   - Retry 2-3 times with delays
   - Don't retry validation errors

7. HANDLE edge cases
   - Empty strings, None values
   - Extreme coordinates (poles, date line)
   - Historic dates (before 1900)
   - Future dates

8. TEST error scenarios
   - Invalid inputs
   - Network failures
   - Rate limits
   - Timeout scenarios
""")

# PRODUCTION-READY FUNCTION
print("\n━" * 60)
print("🏭 Production-Ready Function (All patterns combined)")
print("━" * 60)

def production_calculate_sun_sign(birth_time_str, location_name, longitude, latitude,
                                  max_retries=3, retry_delay=2):
    """
    Production-ready calculation with:
    - Input validation
    - Error handling
    - Retry logic
    - Logging
    - User-friendly messages
    """

    # 1. Validate inputs
    if not isinstance(birth_time_str, str) or len(birth_time_str) < 10:
        return {"success": False, "error": "Invalid time format"}

    if not (-90 <= latitude <= 90):
        return {"success": False, "error": f"Invalid latitude: {latitude}"}

    if not (-180 <= longitude <= 180):
        return {"success": False, "error": f"Invalid longitude: {longitude}"}

    # 2. Retry logic
    for attempt in range(max_retries):
        try:
            # 3. Make API call
            location = GeoLocation(location_name, longitude, latitude)
            birth = Time(birth_time_str, location)
            sun_sign = Calculate.PlanetSignName(PlanetName.Sun, birth)

            # 4. Log success
            logging.info(f"Success: {location_name} -> {sun_sign}")

            # 5. Return success
            return {
                "success": True,
                "sun_sign": sun_sign,
                "location": location_name,
                "birth_time": birth_time_str
            }

        except ConnectionError as e:
            logging.warning(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(retry_delay)
            else:
                logging.error(f"All {max_retries} attempts failed")
                return {
                    "success": False,
                    "error": "Connection error",
                    "message": "Unable to reach VedAstro servers. Check internet connection."
                }

        except Exception as e:
            logging.error(f"Error: {type(e).__name__} - {e}")
            return {
                "success": False,
                "error": type(e).__name__,
                "message": get_friendly_error_message(e)
            }

# Test the production function
print("\nTesting production-ready function:\n")

result = production_calculate_sun_sign(
    "14:30 25/10/1992 +05:30",
    "Mumbai",
    72.8777,
    19.0760
)

if result["success"]:
    print(f"✅ Success!")
    print(f"   Sun Sign: {result['sun_sign']}")
    print(f"   Location: {result['location']}")
else:
    print(f"❌ Failed!")
    print(f"   Error: {result['error']}")

print("\n✨ Error handling patterns demonstration complete!")
print("📝 Check vedastro_errors.log for logged errors")
