from vedastro import *  # install via pip

# THIS DEMO CALCULATES DATA NEEDED TO MAKE BHAVA CHART

# PART 0 : Set API key
Calculate.SetAPIKey('xxxxxxxxxxxxxxxxxx')  # free API key from "vedastro.org/Account"

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
print(json.dumps(house1ZodiacSign, indent=4))

# Get Planets in House 1 (Bhava Chart)
planetsInHouse1 = Calculate.PlanetsInHouse(HouseName.House1, birth_time)
print(json.dumps(planetsInHouse1, indent=4))

# Get Planets in House 1 (Rasi Chart)
planetsInHouse1BasedOnSign = Calculate.PlanetsInHouseBasedOnSign(HouseName.House1, birth_time)
print(json.dumps(planetsInHouse1BasedOnSign, indent=4))


# Get the sign for House 2
# ......
