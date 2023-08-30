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


#PART 2 : SET CUSTOM AYANAMSA
# note : must be set before making calling calculator
#-----------------------------------

print(f"LAHIRI AYANAMSA : 285 AD") 
libray.AstronomicalCalculator.YearOfCoincidence = int(libray.Ayanamsa.Lahiri);

#PART 3 : MAKE CALCULATION
#-----------------------------------
moon_constellation = libray.AstronomicalCalculator.GetPlanetConstellation(birth_time, libray.PlanetName.Sun)
planet_longitude = libray.AstronomicalCalculator.GetPlanetNirayanaLongitude(birth_time, libray.PlanetName.Sun)
print(f"Sun Constellation : {moon_constellation}")  
print(f"Nirayana Longitude : {planet_longitude}")


#PART 4 : CHANGE CUSTOM AYANAMSA
# note : must be set before making calling calculator
#-----------------------------------

print(f"\nRAMAN AYANAMSA : 397 AD")  
libray.AstronomicalCalculator.YearOfCoincidence = int(libray.Ayanamsa.Raman);

#PART 5 : MAKE CALCULATION
#-----------------------------------
moon_constellation = libray.AstronomicalCalculator.GetPlanetConstellation(birth_time, libray.PlanetName.Sun)
planet_longitude = libray.AstronomicalCalculator.GetPlanetNirayanaLongitude(birth_time, libray.PlanetName.Sun)
print(f"Sun Constellation : {moon_constellation}") 
print(f"Nirayana Longitude : {planet_longitude}") 
