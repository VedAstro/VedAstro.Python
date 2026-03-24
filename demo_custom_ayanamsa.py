from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed  API key from "vedastro.org/API.html"

# Set custom ayanamsa (default is Raman if not set)
Calculate.SetAyanamsa(Ayanamsa.Lahiri)

# PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geo = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +08:00", geo)

# get planet data using custom ayanamsa
result = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
Tools.Print(result)
