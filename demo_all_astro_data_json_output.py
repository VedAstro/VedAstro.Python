from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed  API key from "vedastro.org/API.html"

# PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +08:00", geolocation)


#PART 2 : CALCULATE ALL DATA
#-----------------------------------

#PLANETS
allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
jsonStringA = Tools.AnyToJSON("", allPlanetDataList)
print(jsonStringA)

#HOUSES
allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)
jsonStringB = Tools.AnyToJSON("", allHouseDataList)
print(jsonStringB)

#ZODIAC SIGNS
allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)
jsonStringC = Tools.AnyToJSON("", allZodiacDataList)
print(jsonStringC)
