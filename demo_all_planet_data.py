from vedastro import *  # install via pip
import re

#PART 1 : Define CALCULATE Planet DATA Function
#---------------------------------------
def getplanetinfo(planet, time):

    planet_data = Calculate.AllPlanetData(planet, time)
    degree = str(planet_data[83])
    # Extracting degrees, minutes, and seconds from a string
    degree, minute, second = map(int, re.findall(r'\d+', degree))
    # Convert to decimal
    decimal_degrees = degree + (minute / 60) + (second / 3600)

    is_retrograde = str(planet_data[28])
    if is_retrograde == 'True':
       is_retrograde = True
    else:
       is_retrograde = False

    json_data = {"name":str(planet),
                 "is_retrograde":is_retrograde,
                 "position":str(planet_data[0]),
                 "degree":decimal_degrees,
                 "longitude":float(str(planet_data[61]))
                 }

    return json_data


#PART 2 : PREPARE NEEDED DATA
#-----------------------------------

# set birth location
geolocation = GeoLocation("Tokyo, Japan", 139.83, 35.65)

# group all birth time data together (day/month/year)
time = Time("23:40 31/12/2010 +08:00", geolocation)

#PART 3 : Make all Planet Json Format Info using Method
#------------------------------------------------------

# PLANETS
json_data = []
json_data.append(getplanetinfo(PlanetName.Sun, time))
json_data.append(getplanetinfo(PlanetName.Moon, time))
json_data.append(getplanetinfo(PlanetName.Mercury, time))
json_data.append(getplanetinfo(PlanetName.Venus, time))
json_data.append(getplanetinfo(PlanetName.Mars, time))
json_data.append(getplanetinfo(PlanetName.Jupiter, time))
json_data.append(getplanetinfo(PlanetName.Saturn, time))
json_data.append(getplanetinfo(PlanetName.Rahu, time))
json_data.append(getplanetinfo(PlanetName.Ketu, time))

result = {'status': 'ok',
        'data': {'planet_position':json_data}
}

# Print
print(result)