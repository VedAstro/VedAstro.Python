from vedastro import *  # install via pip

# BELOW DEMO FILE MADE FOR @itz-shubham & Maha Arjun
# IN HOPES THAT THEY WILL CONTRIBUTE BACK TO REPO

# THIS DEMO CALCULATES DATA NEEDED TO MAKE BHAVA CHART

#PART 1 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
birth_time = Time("23:40 31/12/2010 +08:00", geolocation)


#PART 2 : CALCULATE DATA FOR CHART
#-----------------------------------

# Get the sign for House 1
house1ZodiacSign = Calculate.HouseZodiacSign(HouseName.House1, birth_time)
Tools.Print(house1ZodiacSign)

# Get Planets in House 1
planetsInHouse1 = Calculate.PlanetsInHouse(HouseName.House1, birth_time)
Tools.Print(planetsInHouse1)

# Get the sign for House 2
# ......

# Please Please @itz-shubham & Maha Arjun do the rest of the code or at least PSUDO CODE! (HELP OTHER BEGINNERS ASWELL)