from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # unlimited use API key from "vedastro.org/Account"

#PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

romeo_birth_time = Time("23:40 31/12/1996 +08:00", geolocation)

juliet_birth_time = Time("23:40 31/12/1997 +08:00", geolocation)


#PART 2 : CALCULATE
#-----------------------------------
matchReport = Calculate.MatchReport(romeo_birth_time, juliet_birth_time)

print(json.dumps(matchReport, indent=4))
