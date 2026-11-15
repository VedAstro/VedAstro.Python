from vedastro import *  # install via pip
import json

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # !!unlimited speed  API key from "vedastro.org/API.html"

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

# Choose the starting system explicitly; levels controls nesting depth.
levels = 3 # represents Dasa, Bhukti, Antaram, Pratyanthar, etc...

dasaAtRange = Calculate.DasaAtRange(birth_time, start_time, end_time, "VimshottariJanma", levels=levels)

print(json.dumps(dasaAtRange, indent=4))
