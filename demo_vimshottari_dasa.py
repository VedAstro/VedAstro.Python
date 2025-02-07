from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # unlimited use API key from "vedastro.org/Account"

# PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +07:00", geolocation)

# set start and end time for the range
start_time = Time("00:00 01/01/2020 +08:00", geolocation)
end_time = Time("23:59 31/12/2025 +08:00", geolocation)

# PART 2 : CALCULATE DASA
#-----------------------------------

# set levels and precision hours
levels = 3 # represents Dasa, Bhukti, Antaram, Pratyanthar, etc...
precision_hours = 100 # accuracy, if set 100h then accuracy ~100h (lower number takes longer to calculate)

dasaAtRange = Calculate.DasaAtRange(birth_time, start_time, end_time, levels, precision_hours)

print(json.dumps(dasaAtRange, indent=4))
