# Load the necessary .NET assemblies
# Import the enum
from vedastro.calculators import *
from vedastro.objects import *


#PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation(location="Tokyo", latitude=35.6895, longitude=139.6917).geolocation

# set birth time
date = "31/12/2010" # day/month/year
time = "23:40" # 24 Hour
time_offset = "+08:00" # standard timezone at birth location

# group all birth time data together
birth_time = Time(date, time, time_offset, geolocation).time_object


#PART 2 : CALCULATE ALL DATA
#-----------------------------------

#PLANETS
allPlanetDataList = VedAstro.Calculate.AllPlanetData(VedAstro.PlanetName.Sun, birth_time)
allDataJson = VedAstro.APIFunctionResult.ToJsonList(allPlanetDataList)
print(allDataJson)

#HOUSES
allHouseDataList = VedAstro.Calculate.AllHouseData(VedAstro.HouseName.House1, birth_time)
allDataJson = VedAstro.APIFunctionResult.ToJsonList(allHouseDataList)
print(allDataJson)

#ZODIAC SIGNS
allZodiacDataList = VedAstro.Calculate.AllZodiacSignData(VedAstro.ZodiacName.Gemini, birth_time)
allDataJson = VedAstro.APIFunctionResult.ToJsonList(allZodiacDataList)
print(allDataJson)
