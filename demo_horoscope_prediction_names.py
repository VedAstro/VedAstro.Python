from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed  API key from "vedastro.org/Account"

# set location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# set time hh:mm dd/mm/yyyy zzz
birthTime = Time("23:40 31/12/2010 +08:00", geolocation)

# run calculator to get result
calcResult = Calculate.HoroscopePredictionNames(birthTime)

# display results
print(json.dumps(calcResult, indent=4))
