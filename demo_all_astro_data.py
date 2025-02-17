from vedastro import *  # install via pip

# PART 0 : Set API key
Calculate.SetAPIKey('FreeAPIUser')  # ⚡ unlimited speed API key from "vedastro.org/Account"

#PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +08:00", geolocation)


#PART 2 : CALCULATE ALL DATA
#-----------------------------------

#HOROSCOPE PREDICTIONS
horoscopePredictions = Calculate.HoroscopePredictions(birth_time, "Empty")
print(json.dumps(horoscopePredictions, indent=4))

#PLANETS
allPlanetDataList = Calculate.AllPlanetData(PlanetName.Sun, birth_time)
print(json.dumps(allPlanetDataList, indent=4))

#HOUSES
allHouseDataList = Calculate.AllHouseData(HouseName.House1, birth_time)
print(json.dumps(allHouseDataList, indent=4))

#ZODIAC SIGNS
allZodiacDataList = Calculate.AllZodiacSignData(ZodiacName.Gemini, birth_time)
print(json.dumps(allZodiacDataList, indent=4))

#SUNRISE TIME
sunriseTime = Calculate.SunriseTime(birth_time)
print(json.dumps(sunriseTime, indent=4))

#SUNSET TIME
sunsetTime = Calculate.SunsetTime(birth_time)
print(json.dumps(sunriseTime, indent=4))

#Panchanga Table
panchangaTable = Calculate.PanchangaTable(birth_time)
print(json.dumps(panchangaTable, indent=4))

#Lagna Sign Name
panchangaTable = Calculate.LagnaSignName(birth_time)
print(json.dumps(panchangaTable, indent=4))

#Bhinnashtakavarga Chart
bhinnashtakavarga = Calculate.BhinnashtakavargaChart(birth_time)
print(json.dumps(bhinnashtakavarga, indent=4))

#Gulika Longitude
gulikaLongitude = Calculate.GulikaLongitude(birth_time)
print(json.dumps(gulikaLongitude, indent=4))

#Day of week
dayOfWeek = Calculate.DayOfWeek(birth_time)
print(json.dumps(dayOfWeek, indent=4))
