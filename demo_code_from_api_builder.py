from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed  API key from "vedastro.org/API.html"

# PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# set time hh:mm dd/mm/yyyy zzz
time = Time("23:40 31/12/2010 +08:00", geolocation)

# set planet
planetName = PlanetName.Sun

# run calculator to get result
calcResult = Calculate.HousePlanetOccupiesBasedOnSign(planetName, time)

# display results
Tools.Print(calcResult)