# AUTO GENERATED ON 20:04 22/03/2026 +07:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any
import requests
import json
from enum import Enum


class Calculate:
    api_key = None
    ayanamsa = None
    base_url = "https://vedastro.azurewebsites.net/api/Calculate"

    @classmethod
    def SetAPIKey(cls, api_key):
        cls.api_key = api_key

    @classmethod
    def SetAyanamsa(cls, ayanamsa):
        cls.ayanamsa = ayanamsa

    @classmethod
    def _make_request(cls, endpoint, params):
        url = f"{cls.base_url}/{endpoint}"
        if cls.api_key:
            params["APIKey"] = cls.api_key
        if cls.ayanamsa:
            params["Ayanamsa"] = cls.ayanamsa.value if hasattr(cls.ayanamsa, 'value') else cls.ayanamsa
        response = requests.post(url, json=params, timeout=120)
        response.raise_for_status()
        data = response.json()
        if data.get("Status") == "Fail":
            raise RuntimeError(f"VedAstro API error: {data.get('Payload', 'Unknown error')}")
        payload = data.get("Payload")
        if not payload:
            raise ValueError("Payload is missing or empty in API response")
        if isinstance(payload, list):
            return payload
        if isinstance(payload, dict):
            values = list(payload.values())
            return values[0] if len(values) == 1 else payload
        return payload

    @classmethod
    def FindBirthTimeByAnimal(cls, possibleBirthTime, precisionHours):
        """
         Finds possible birth time based on matching animal prediction Yoni Kuta 
        :return: JObject
         """
        endpoint = "FindBirthTimeByAnimal"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByRisingSign(cls, possibleBirthTime, precisionHours):
        """
         Finds possible birth time based on matching rising sign Lagna 
        :return: JObject
         """
        endpoint = "FindBirthTimeByRisingSign"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeHouseStrengthPerson(cls, possibleBirthTime, precisionHours):
        """
         Finds possible birth time by calculating house strength for each time slice 
        :return: JObject
         """
        endpoint = "FindBirthTimeHouseStrengthPerson"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByMachineLearning(cls, possibleBirthTime, bodyHeight, bodyShape, precisionHours):
        """
         Finds the possible birth time based on machine learning predictions of body attributes. 
        :return: TimeRange
         """
        endpoint = "FindBirthTimeByMachineLearning"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "bodyHeight": bodyHeight,
            "bodyShape": bodyShape,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ListAPICalls(cls, ):
        """
         Returns list of all API calls for fun why not 
        :return: JArray
         """
        endpoint = "ListAPICalls"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AddressToGeoLocation(cls, address):
        """
         Given an address will convert to its geo location equivelant httplocalhost7071apiCalculateAddressToGeoLocationAddressGaithersburg 
        :return: Task`1
         """
        endpoint = "AddressToGeoLocation"
        params = {
            "address": address,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchLocation(cls, address):
        """
         Searches for a location by name using the Google Maps API or configured provider. 
        :return: Task`1
         """
        endpoint = "SearchLocation"
        params = {
            "address": address,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CoordinatesToGeoLocation(cls, latitude, longitude):
        """
         Given coordinates will convert to its geo location equivalent httplocalhost7071apiCalculateCoordinatesToGeoLocationLatitude35.6764Longitude139.6500 
        :return: Task`1
         """
        endpoint = "CoordinatesToGeoLocation"
        params = {
            "latitude": latitude,
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GeoLocationToTimezone(cls, geoLocation, timeAtLocation):
        """
         Gets all timezone given a location accounts for Daylight savings historical changes Note location name is not mandatory it is there because location names can change but coordinates are essential .....apiCalculateGeoLocationToTimezoneLocationTokyo JapanCoordinates35.65139.83Time1402091119770000 
        :return: Task`1
         """
        endpoint = "GeoLocationToTimezone"
        params = {
            "geoLocation": geoLocation,
            "timeAtLocation": timeAtLocation,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IpAddressToGeoLocation(cls, ipAddress):
        """
         .....apiCalculateIpAddressToGeoLocationIpAddress180.89.33.89 
        :return: Task`1
         """
        endpoint = "IpAddressToGeoLocation"
        params = {
            "ipAddress": ipAddress,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def StandardTimeNowAtLocation(cls, locationName):
        """
         Gets the current standard time at the specified location. 
        :return: Task`1
         """
        endpoint = "StandardTimeNowAtLocation"
        params = {
            "locationName": locationName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventsAtTime(cls, birthTime, checkTime, eventTagList):
        """
         Gets all events occuring at given time. Basically a slice from Events Chart Can be used by LLM to interprate final prediction. Also known as Muhurtha 
        :return: List`1
         """
        endpoint = "EventsAtTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "eventTagList": eventTagList,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventsAtRange(cls, birthTime, startTime, endTime, eventTagList, precisionHours):
        """
         Calculates all events occurring within a specified time range. 
        :return: List`1
         """
        endpoint = "EventsAtRange"
        params = {
            "birthTime": birthTime.to_json(),
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "eventTagList": eventTagList,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventStartEndTime(cls, birthTime, checkTime, nameOfEvent):
        """
         Given a birth time current time and event name gets the event data occuring at current time Easy way to check if Gochara is occuring at given time with start and end time calculated Precision hard set to 1 hour TODO 
        :return: Event
         """
        endpoint = "EventStartEndTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "nameOfEvent": nameOfEvent,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventStartTime(cls, birthTime, checkTime, eventData, precisionInHours):
        """
         Finds the start time of a specific event given a check time where the event is occurring. Scans backwards from check time. 
        :return: Time
         """
        endpoint = "EventStartTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "eventData": eventData,
            "precisionInHours": precisionInHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventEndTime(cls, birthTime, checkTime, eventData, precisionInHours):
        """
         Finds the end time of a specific event given a check time where the event is occurring. Scans forwards from check time. 
        :return: Time
         """
        endpoint = "EventEndTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "eventData": eventData,
            "precisionInHours": precisionInHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MatchReport(cls, maleBirthTime, femaleBirthTime):
        """
         Get full kuta match data for 2 horoscopes 
        :return: MatchReport
         """
        endpoint = "MatchReport"
        params = {
            "maleBirthTime": maleBirthTime.to_json(),
            "femaleBirthTime": femaleBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MatchReportWithBazi(cls, maleBirthTime, femaleBirthTime):
        """
         Generates a compatibility report including both Vedic and Bazi analysis. 
        :return: Task`1
         """
        endpoint = "MatchReportWithBazi"
        params = {
            "maleBirthTime": maleBirthTime.to_json(),
            "femaleBirthTime": femaleBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthTimeLocationAutoAIFill(cls, personFullName):
        """
         Automatically fills birth time and location using AI for a given famous persons name. 
        :return: Task`1
         """
        endpoint = "BirthTimeLocationAutoAIFill"
        params = {
            "personFullName": personFullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthTimeAutoAIFill(cls, personFullName):
        """
         Given a famous person name will auto find birth time using LLM AI 
        :return: Task`1
         """
        endpoint = "BirthTimeAutoAIFill"
        params = {
            "personFullName": personFullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarriageTagsAutoAIFill(cls, personA, personB):
        """
         Uses AI to find marriage related tagsinfo for a couple. 
        :return: Task`1
         """
        endpoint = "MarriageTagsAutoAIFill"
        params = {
            "personA": personA,
            "personB": personB,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthLocationAutoAIFill(cls, personFullName):
        """
         Given a famous person name will auto find birth location using LLM AI 
        :return: Task`1
         """
        endpoint = "BirthLocationAutoAIFill"
        params = {
            "personFullName": personFullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarriagePartnerNameAutoAIFill(cls, personFullName):
        """
         Given a famous person name will auto find marriage partner using LLM AI 
        :return: Task`1
         """
        endpoint = "MarriagePartnerNameAutoAIFill"
        params = {
            "personFullName": personFullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MatchChat(cls, maleBirthTime, femaleBirthTime, userQuestion, chatSession):
        """
         Ask questions to AI astrologer about life horoscope predictions 
        :return: Task`1
         """
        endpoint = "MatchChat"
        params = {
            "maleBirthTime": maleBirthTime.to_json(),
            "femaleBirthTime": femaleBirthTime.to_json(),
            "userQuestion": userQuestion,
            "chatSession": chatSession,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopeLLMSearch(cls, birthTime, textInput):
        """
         Searches all horoscopes predictions with LLM 
        :return: Task`1
         """
        endpoint = "HoroscopeLLMSearch"
        params = {
            "birthTime": birthTime.to_json(),
            "textInput": textInput,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GenerateTimeListCSV(cls, startTime, endTime, hoursBetween):
        """
         Given a start time end time and space in hours between. Will generate massive CSV tables for ML Data Science Will contain 3 columns NameTimeLocation this can then be fed into ML Table Generator to make datasets worthy of HuggingFace 
        :return: String
         """
        endpoint = "GenerateTimeListCSV"
        params = {
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "hoursBetween": hoursBetween,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseSignName(cls, house, sign, time):
        """
         Checks if the inputed sign was the sign of the house during the inputed time 
        :return: Boolean
         """
        endpoint = "IsHouseSignName"
        params = {
            "house": house.value,
            "sign": sign.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseSignName(cls, houseNumber, time):
        """
         Gets only the the zodiac sign name at middle longitude of the house. 
        :return: ZodiacName
         """
        endpoint = "HouseSignName"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseBhavaChalitSign(cls, houseNumber, time):
        """
         Gets the zodiac sign at middle longitude of the house with degrees data Bhava Chalit 
        :return: ZodiacSign
         """
        endpoint = "HouseBhavaChalitSign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseRasiSign(cls, houseNumber, time):
        """
         Gets zodiac sign for a given house counted from lagna 
        :return: ZodiacSign
         """
        endpoint = "HouseRasiSign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseBhavaChalitSigns(cls, time):
        """
         Gets the zodiac sign at middle longitude of the house. 
        :return: Dictionary`2
         """
        endpoint = "AllHouseBhavaChalitSigns"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseRasiSigns(cls, time):
        """
         Gets signs for all houses in respective Vargas Divisional Charts 
        :return: Dictionary`2
         """
        endpoint = "AllHouseRasiSigns"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseHoraSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseHoraSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseDrekkanaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseDrekkanaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseChaturthamsaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseChaturthamsaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseSaptamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseSaptamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseNavamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseNavamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseDashamamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseDashamamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseDwadashamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseDwadashamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseShodashamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseShodashamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseVimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseVimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseChaturvimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseChaturvimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseBhamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseBhamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseTrimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseTrimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseKhavedamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseKhavedamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseAkshavedamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseAkshavedamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseShashtyamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseShashtyamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDivisionalLongitude(cls, planetName, inputTime, divisionalNo):
        """
         Calculates the divisional longitude of a planet in a Dchart divisional chart in Vedic Astrology. written by AI Human 
        :return: Angle
         """
        endpoint = "PlanetDivisionalLongitude"
        params = {
            "planetName": planetName.value,
            "inputTime": inputTime.to_json(),
            "divisionalNo": divisionalNo,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DivisionalLongitude(cls, totalDegrees, divisionalNo):
        """
         General calculator for divisional longitude. 
        :return: Angle
         """
        endpoint = "DivisionalLongitude"
        params = {
            "totalDegrees": totalDegrees,
            "divisionalNo": divisionalNo,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetZodiacSignBasedOnHouseLongitudes(cls, planetName, time):
        """
         Get zodiac sign planet is in based on house longitudes basically the sign of the house the planet is in based on longitudes D0 Bhava chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetZodiacSignBasedOnHouseLongitudes"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetRasiD1Sign(cls, planetName, time):
        """
         Get zodiac sign planet is in. D1 
        :return: ZodiacSign
         """
        endpoint = "PlanetRasiD1Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetHoraD2Signs(cls, planetName, time):
        """
         Gets Hora D2 zodiac sign of a planet 
        :return: ZodiacSign
         """
        endpoint = "PlanetHoraD2Signs"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoraSignName(cls, zodiacSign):
        """
         D2 chart 
        :return: ZodiacSign
         """
        endpoint = "HoraSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoraSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Hora D2 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "HoraSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseHoraD2Sign(cls, houseNumber, time):
        """
         Gets the zodiac sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseHoraD2Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDrekkanaD3Sign(cls, planetName, time):
        """
         Gets the Drekkana sign the planet is in D3 
        :return: ZodiacSign
         """
        endpoint = "PlanetDrekkanaD3Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DrekkanaSignName(cls, zodiacSign):
        """
         Given a zodiac sign will convert to drekkana D3 
        :return: ZodiacSign
         """
        endpoint = "DrekkanaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DrekkanaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Drekkana D3 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "DrekkanaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseDrekkanaD3Sign(cls, houseNumber, time):
        """
         Gets the Drekkana sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseDrekkanaD3Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetChaturthamshaD4Sign(cls, planetName, time):
        """
         D4 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetChaturthamshaD4Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChaturthamshaSignName(cls, zodiacSign):
        """
         D4 chart 
        :return: ZodiacSign
         """
        endpoint = "ChaturthamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChaturthamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Hora D4 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "ChaturthamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseChaturthamshaD4Sign(cls, houseNumber, time):
        """
         Gets the Chaturthamsha D4 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseChaturthamshaD4Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSaptamshaD7Sign(cls, planetName, time):
        """
         D7 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetSaptamshaD7Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SaptamshaSignName(cls, zodiacSign):
        """
         D7 chart 
        :return: ZodiacSign
         """
        endpoint = "SaptamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SaptamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Saptamsha D7 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "SaptamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseSaptamshaD7Sign(cls, houseNumber, time):
        """
         Gets the Saptamsha D7 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseSaptamshaD7Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSaptamshaSignOLD(cls, planetName, time):
        """
         Saptamsa D7 and measures 4.28 degrees TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacName
         """
        endpoint = "PlanetSaptamshaSignOLD"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNavamshaD9Sign(cls, planetName, time):
        """
         D9 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetNavamshaD9Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NavamshaSignName(cls, zodiacSign):
        """
         D9 chart 
        :return: ZodiacSign
         """
        endpoint = "NavamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NavamshaSignAtLongitude(cls, longitude):
        """
         Gets Navamsa D9 sign given a longitude 
        :return: ZodiacSign
         """
        endpoint = "NavamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseNavamshaD9Sign(cls, houseNumber, time):
        """
         Get Navamsa D9 sign of house mid point 
        :return: ZodiacSign
         """
        endpoint = "HouseNavamshaD9Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NavamshaSignAtLongitudeOLD(cls, longitude):
        """
         Gets Navamsa D9 sign given a longitude TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacSign
         """
        endpoint = "NavamshaSignAtLongitudeOLD"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDashamamshaD10Sign(cls, planetName, time):
        """
         D10 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetDashamamshaD10Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DashamamshaSignName(cls, zodiacSign):
        """
         D10 chart 
        :return: ZodiacSign
         """
        endpoint = "DashamamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DashamamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Dashamamsha D10 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "DashamamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseDashamamshaD10Sign(cls, houseNumber, time):
        """
         Gets the Dashamamsha D10 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseDashamamshaD10Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDwadashamshaD12Sign(cls, planetName, time):
        """
         D12 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetDwadashamshaD12Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DwadashamshaSignName(cls, zodiacSign):
        """
         D12 chart 
        :return: ZodiacSign
         """
        endpoint = "DwadashamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DwadashamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Dwadashamsha D12 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "DwadashamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseDwadashamshaD12Sign(cls, houseNumber, time):
        """
         Gets the Dwadashamsha D12 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseDwadashamshaD12Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDwadashamshaSignOLD(cls, planetName, time):
        """
         When a sign is divided into 12 equal parts each is called a Dwadasamsa D12 and measures 2.5 degrees. The Bhachakra can thus he said to contain 12x12144 Dwadasamsas. The lords of the 12 Dwadasamsas in a sign are the lords of the 12 signs from it i.e. the lord of the first Dwadasamsa in Mesha is Kuja that of the second Sukra and so on. TODO BV RAMAN method OLD MARKED FOR OBLIVION NEEDS TESTING AGAINST NEW METHOD 
        :return: ZodiacName
         """
        endpoint = "PlanetDwadashamshaSignOLD"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetShodashamshaD16Sign(cls, planetName, time):
        """
         D16 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetShodashamshaD16Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShodashamshaSignName(cls, zodiacSign):
        """
         D16 chart 
        :return: ZodiacSign
         """
        endpoint = "ShodashamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShodashamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Shodashamsha D16 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "ShodashamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseShodashamshaD16Sign(cls, houseNumber, time):
        """
         Gets the Shodashamsha D16 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseShodashamshaD16Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetVimshamshaD20Sign(cls, planetName, time):
        """
         D20 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetVimshamshaD20Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def VimshamshaSignName(cls, zodiacSign):
        """
         D20 chart 
        :return: ZodiacSign
         """
        endpoint = "VimshamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def VimshamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Vimshamsha D20 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "VimshamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseVimshamshaD20Sign(cls, houseNumber, time):
        """
         Gets the Vimshamsha D20 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseVimshamshaD20Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetChaturvimshamshaD24Sign(cls, planetName, time):
        """
         D24 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetChaturvimshamshaD24Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChaturvimshamshaSignName(cls, zodiacSign):
        """
         D24 chart 
        :return: ZodiacSign
         """
        endpoint = "ChaturvimshamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChaturvimshamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Chaturvimshamsha D24 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "ChaturvimshamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseChaturvimshamshaD24Sign(cls, houseNumber, time):
        """
         Gets the Chaturvimshamsha D24 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseChaturvimshamshaD24Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetBhamshaD27Sign(cls, planetName, time):
        """
         D27 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetBhamshaD27Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhamshaSignName(cls, zodiacSign):
        """
         D27 chart 
        :return: ZodiacSign
         """
        endpoint = "BhamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Bhamsha D27 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "BhamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseBhamshaD27Sign(cls, houseNumber, time):
        """
         Gets the Bhamsha D27 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseBhamshaD27Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTrimshamshaD30Sign(cls, planetName, time):
        """
         Get Thrimsamsa D30 sign of planet Trimshamsha or onethirtieth of a sign Reference Elements of Astrology Trimshamsha Table X12 Literally speaking it is considered as one thirtieth division of a sign. Actually however each sign is divided into five unequal parts each part belonging to one of the five planets from Mars to Saturn. In odd signs the first five degrees belong to Mars the next five degrees to Saturn the next eight degrees to Jupiter the subsequent seven degrees to Mercury and the last five degrees to Venus. This order gets reversed in case of even signs where the planets Venus Mercury Jupiter Saturn and Mars respectively own five degrees seven degrees eight degrees five degrees and five degrees in a sign. 
        :return: ZodiacSign
         """
        endpoint = "PlanetTrimshamshaD30Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TrimshamshaSignName(cls, zodiacSign):
        """
         D30 chart 
        :return: ZodiacSign
         """
        endpoint = "TrimshamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TrimshamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Trimshamsha D30 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "TrimshamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseTrimshamshaD30Sign(cls, houseNumber, time):
        """
         Gets the Trimshamsha D30 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseTrimshamshaD30Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKhavedamshaD40Sign(cls, planetName, time):
        """
         D40 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetKhavedamshaD40Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def KhavedamshaSignName(cls, zodiacSign):
        """
         D40 chart 
        :return: ZodiacSign
         """
        endpoint = "KhavedamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def KhavedamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Khavedamsha D40 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "KhavedamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseKhavedamshaD40Sign(cls, houseNumber, time):
        """
         Gets the Khavedamsha D40 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseKhavedamshaD40Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAkshavedamshaD45Sign(cls, planetName, time):
        """
         D45 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetAkshavedamshaD45Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AkshavedamshaSignName(cls, zodiacSign):
        """
         D45 chart 
        :return: ZodiacSign
         """
        endpoint = "AkshavedamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AkshavedamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Akshavedamsha D45 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "AkshavedamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseAkshavedamshaD45Sign(cls, houseNumber, time):
        """
         Gets the Akshavedamsha D45 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseAkshavedamshaD45Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetShashtyamshaD60Sign(cls, planetName, time):
        """
         D60 chart 
        :return: ZodiacSign
         """
        endpoint = "PlanetShashtyamshaD60Sign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShashtyamshaSignName(cls, zodiacSign):
        """
         D60 chart 
        :return: ZodiacSign
         """
        endpoint = "ShashtyamshaSignName"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShashtyamshaSignAtLongitude(cls, longitude):
        """
         Given a longitude will return Shashtyamsha D60 sign at that longitude 
        :return: ZodiacSign
         """
        endpoint = "ShashtyamshaSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseShashtyamshaD60Sign(cls, houseNumber, time):
        """
         Gets the Shashtyamsha D60 sign at middle longitude of the house with degrees data 
        :return: ZodiacSign
         """
        endpoint = "HouseShashtyamshaD60Sign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetSignsBasedOnHouseLongitudes(cls, time):
        """
         Gets list of all planets and the zodiac signs they are in based on house longitudes 
        :return: Dictionary`2
         """
        endpoint = "AllPlanetSignsBasedOnHouseLongitudes"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetRasiSigns(cls, time):
        """
         Gets list of all planets and the zodiac signs they are in 
        :return: Dictionary`2
         """
        endpoint = "AllPlanetRasiSigns"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetHoraSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetHoraSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetDrekkanaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetDrekkanaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetChaturthamsaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetChaturthamsaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetSaptamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetSaptamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetNavamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetNavamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetDashamamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetDashamamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetDwadashamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetDwadashamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetShodashamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetShodashamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetVimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetVimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetChaturvimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetChaturvimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetBhamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetBhamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetTrimshamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetTrimshamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetKhavedamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetKhavedamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetAkshavedamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetAkshavedamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetShashtyamshaSign(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllPlanetShashtyamshaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTajikaLongitude(cls, planetName, birthTime, scanYear):
        """
         Gets a given planets Tajika Longitude 
        :return: Angle
         """
        endpoint = "PlanetTajikaLongitude"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTajikaConstellation(cls, planetName, birthTime, scanYear):
        """
         Gets a given planets Tajika constellation 
        :return: Constellation
         """
        endpoint = "PlanetTajikaConstellation"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTajikaZodiacSign(cls, planetName, birthTime, scanYear):
        """
         Gets a given planets Tajika zodiac sign 
        :return: ZodiacSign
         """
        endpoint = "PlanetTajikaZodiacSign"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TajikaDateForYear2(cls, birthTime, scanYear):
        """
         Annual or Progressed Horoscope The annual or progressed horoscope sidereal solar return according to Western astrology is cast the same way as the birth horoscope. The time of the commencement of the anniversary known as Varsharambha is said to begin at the exact moment when the Sun comes to the same position he was in at the time of birth. In other words the individuals New Year begins when the Sun comes back to the same point he heJd at the time of birth. Given a birth time and scan year will return exact time for tajika chart The tjika system attempts to predict in detail the likely happenings in one year of an individuals life. The system goes to such details as to predict events even on a daybyday basis or even halfaday. On account of this this system is also called the varaphala system. 
        :return: Time
         """
        endpoint = "TajikaDateForYear2"
        params = {
            "birthTime": birthTime.to_json(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TajikaDateForYear(cls, birthTime, scanYear):
        """
         Annual or Progressed Horoscope The annual or progressed horoscope sidereal solar return according to Western astrology is cast the same way as the birth horoscope. The time of the commencement of the anniversary known as Varsharambha is said to begin at the exact moment when the Sun comes to the same position he was in at the time of birth. In other words the individuals New Year begins when the Sun comes back to the same point he heJd at the time of birth. Calculated based on method in BV Raman book Varshaphala 
        :return: Time
         """
        endpoint = "TajikaDateForYear"
        params = {
            "birthTime": birthTime.to_json(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromLagna(cls, transitPlanet, checkTime, birthTime):
        """
         Calculates the house a transiting planet is in relative to natal Lagna 
        :return: HouseName
         """
        endpoint = "TransitHouseFromLagna"
        params = {
            "transitPlanet": transitPlanet.value,
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromNavamsaLagna(cls, transitPlanet, checkTime, birthTime):
        """
         Calculates the house a transiting planet is in relative to natal Navamsa Lagna 
        :return: HouseName
         """
        endpoint = "TransitHouseFromNavamsaLagna"
        params = {
            "transitPlanet": transitPlanet.value,
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromMoon(cls, transitPlanet, checkTime, birthTime):
        """
         Calculates the house a transiting planet is in relative to natal Moon 
        :return: HouseName
         """
        endpoint = "TransitHouseFromMoon"
        params = {
            "transitPlanet": transitPlanet.value,
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromNavamsaMoon(cls, transitPlanet, checkTime, birthTime):
        """
         Calculates the house a transiting planet is in relative to natal Navamsa Moon 
        :return: HouseName
         """
        endpoint = "TransitHouseFromNavamsaMoon"
        params = {
            "transitPlanet": transitPlanet.value,
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Murthi(cls, transitPlanet, checkTime, birthTime):
        """
         Calculates the Murthi form of a planet during transit. Swarna Gold Rajata Silver Tamra Copper Loha Iron. 
        :return: String
         """
        endpoint = "Murthi"
        params = {
            "transitPlanet": transitPlanet.value,
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PanchangaTable(cls, inputTime):
        """
         Its used to determine auspicious times and rituals. It includes multiple attributes such as Tithi lunar day Lunar Month Vara weekday Nakshatra constellation Yoga lunisolar day and Karana half of a Tithi. Disha Shool 
        :return: PanchangaTable
         """
        endpoint = "PanchangaTable"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DishaShool(cls, inputTime):
        """
         Here are the following Disha shool days and the directions that are considered as inauspicious or Disha shool. Check the Disha Shool chart to find the inauspicious direction to travel 
        :return: String
         """
        endpoint = "DishaShool"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LunarMonth(cls, inputTime, ignoreLeapMonth):
        """
         Also know as Chandramana or Hindu Month. Each Hindu month begins with the New Moon. These lunar months go by special names. The name of a lunar month is decided by the rasi in which SunMoon conjunction takes place. These names come from the constellation that Moon is most likely to occupy on the full Moon day. Names are Chaitra Vaisaakha Jyeshtha Aashaadha Sraavana etc... 
        :return: LunarMonth
         """
        endpoint = "LunarMonth"
        params = {
            "inputTime": inputTime.to_json(),
            "ignoreLeapMonth": ignoreLeapMonth,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextNewMoon(cls, inputTime):
        """
         Gets next future New Moon date when tithi will be 1. Uses conjunctions angle to calculate with accuracy of 30min Includes start time in scan 
        :return: Time
         """
        endpoint = "NextNewMoon"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PreviousNewMoon(cls, inputTime):
        """
         Gets last occured New Moon date when tithi will be 1. Uses conjunctions angle to calculate with accuracy of 30min Includes start time in scan 
        :return: Time
         """
        endpoint = "PreviousNewMoon"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunMoonConjunctionAngle(cls, ccc):
        """
         Gets the distance in degrees between Sun Moon at a given time Used to calculate lunar months. 
        :return: Angle
         """
        endpoint = "SunMoonConjunctionAngle"
        params = {
            "ccc": ccc.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAvasta(cls, planetName, time):
        """
         Gets all the Avastas for a planet Lajjita Garvita Kshudita etc... 
        :return: List`1
         """
        endpoint = "PlanetAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInLajjitaAvasta(cls, planetName, time):
        """
         Lajjita humiliated Planet in the 5th house in conjunction with rahu or ketu Saturn or mars. 
        :return: Boolean
         """
        endpoint = "IsPlanetInLajjitaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInGarvitaAvasta(cls, planetName, time):
        """
         Garvita proud Planet in exaltation sign or moolatrikona zone happiness and gains 
        :return: Boolean
         """
        endpoint = "IsPlanetInGarvitaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInKshuditaAvasta(cls, planetName, time):
        """
         Kshudita hungry Planet in enemys sign or conjoined with enemy or aspected by enemy Grief 
        :return: Boolean
         """
        endpoint = "IsPlanetInKshuditaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInTrashitaAvasta(cls, planetName, time):
        """
         Trashita thirsty Planet in a watery sign aspected by a enemy and is without the aspect of benefic Planets The Planet who being conjoined or aspected by a Malefic or his enemy Planet is situated without the aspect of a benefic Planet in the 4th House is Trashita. Another version If the Planet is situated in a watery sign is aspected by an enemy Planet and is without the aspect of benefic Planets he is called Trashita. A planet in a Water Sign and aspected by an enemy planet with no auspiscious Graha aspecting is said to be Trishita AvasthaThirsty State. This state is in effect whenever a planet is in a Water Sign and it gets aspected by an enemy planet. But if a Gentle Planet MercuryVenusMoon aspects here it strengthens the planet in Water Sign. This Avastha is only for the aspecting enemy planet that will cause TrishitaThirst. This state shows that a planet in a watery Rasi can still be productive even when aspected by enemies though it will not be happy. As the name Thirsty State implies it indicates the lack of emotional fulfillment that a planet experiences. 
        :return: Boolean
         """
        endpoint = "IsPlanetInTrashitaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInMuditaAvasta(cls, planetName, time):
        """
         The Planet who is in his friends sign is in conjunction with Jupiter and is together with or is aspected by a friendly Planet is called Mudita Mudita sated happy Planet in a friends sign or aspected by a friend and conjoined with Jupiter Gains If a planet is in a friends sign or joined with a friend or aspected by a friend or that joined with Jupiter is called Mudita AvasthaDelighted State It is clear from explanation itself that a planet will feel delighted when it is in friendly sign or friendly planet conjunctsaspects or it is joined by the biggest benefic planet Jupiter. We can understand planets delight in such cases. Planet in friendly sign A planet in a friendly sign is productive and the stronger that friend planet the more productive it will be. 
        :return: Boolean
         """
        endpoint = "IsPlanetInMuditaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInKshobhitaAvasta(cls, planetName, time):
        """
         If a planet is conjunct by Sun or it is aspected by Enemy Malefic Planets then it should always be known as Kshobhita AvasthaAgitated State Kshobhita guilty repentant Planet in conjunction with sun and aspected by malefics and an enemy. Penury 
        :return: Boolean
         """
        endpoint = "IsPlanetInKshobhitaAvasta"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSignTransit(cls, startTime, endTime, planetName):
        """
         Calculates the sign transits of a planet between a start and end time. Returns a list of tuples containing start time end time sign name and planet name. 
        :return: List`1
         """
        endpoint = "PlanetSignTransit"
        params = {
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetConstellationTransitStartTime(cls, startTime, endTime, planetName):
        """
         Gets all the constellation start time for a given planet Set to an accuracy of 1 minute 
        :return: List`1
         """
        endpoint = "GetConstellationTransitStartTime"
        params = {
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetConstellation(cls, time):
        """
         Niryana Constellation of all 9 planets 
        :return: Dictionary`2
         """
        endpoint = "AllPlanetConstellation"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllTimeData(cls, time):
        """
         Gets all possible calculations for a given Time 
        :return: List`1
         """
        endpoint = "AllTimeData"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetData(cls, planetName, time):
        """
         Gets all possible calculations for a Planet at a given Time 
        :return: List`1
         """
        endpoint = "AllPlanetData"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseData(cls, houseName, time):
        """
         All possible calculations for a House at a given Time 
        :return: List`1
         """
        endpoint = "AllHouseData"
        params = {
            "houseName": houseName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetHouseData(cls, planetName, houseName, time):
        """
         All possible calculations for a Planet and House at a given Time 
        :return: List`1
         """
        endpoint = "AllPlanetHouseData"
        params = {
            "planetName": planetName.value,
            "houseName": houseName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllZodiacSignData(cls, zodiacName, time):
        """
         All possible calculations for a Zodiac Sign at a given Time 
        :return: List`1
         """
        endpoint = "AllZodiacSignData"
        params = {
            "zodiacName": zodiacName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeOffsetToLongitude(cls, time):
        """
         Converts time back to longitude it is the reverse of LongitudeToLMTOffset Exp 5h. 10m. 20s. E. Long. to 77 35 E. Long 
        :return: Angle
         """
        endpoint = "TimeOffsetToLongitude"
        params = {
            "time": time,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeToJulianEphemerisTime(cls, time):
        """
         Gets the ephemris time that is consumed by Swiss Ephemeris Converts normal time to Ephemeris time shown as a number 
        :return: Double
         """
        endpoint = "TimeToJulianEphemerisTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeToJulianUniversalTime(cls, time):
        """
         Converts Time to Julian Day in Universal Time UT 
        :return: Double
         """
        endpoint = "TimeToJulianUniversalTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LmtToStd(cls, lmtDateTime, stdOffset):
        """
         Convert Local Mean Time LMT to Standard Time STD API URL ..LmtToStdTime054503051932Longitude75STDOffset0530 
        :return: DateTimeOffset
         """
        endpoint = "LmtToStd"
        params = {
            "lmtDateTime": lmtDateTime,
            "stdOffset": stdOffset,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LongitudeToLMTOffset(cls, longitudeDeg):
        """
         Convert longitude to LMT offset input longitude range 180 to 180 
        :return: TimeSpan
         """
        endpoint = "LongitudeToLMTOffset"
        params = {
            "longitudeDeg": longitudeDeg,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LocalMeanTime(cls, time):
        """
         Given a standard time LMT and location will get Local mean time 
        :return: String
         """
        endpoint = "LocalMeanTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LocalStandardTime(cls, time):
        """
         Given a standard time STD and location will get local standard time based on location Offset auto set by Google Offset API 
        :return: String
         """
        endpoint = "LocalStandardTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AutoCalculateTimeRange(cls, inputBirthTime, timePreset, outputTimezone):
        """
         supports dynamic 3 types of preset age1to10 3weeks 3months 3years fulllife 19902000 given a nice human time range will generate start and end times input users current timezone could be different from birth 
        :return: TimeRange
         """
        endpoint = "AutoCalculateTimeRange"
        params = {
            "inputBirthTime": inputBirthTime.to_json(),
            "timePreset": timePreset,
            "outputTimezone": outputTimezone,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DaysBetweenTimeRangePreset(cls, inputBirthTime, timePreset, outputTimezone):
        """
         Give a time preset 3 types will return days between them NOTE used by web UI via API for chart precision calculation 
        :return: Double
         """
        endpoint = "DaysBetweenTimeRangePreset"
        params = {
            "inputBirthTime": inputBirthTime.to_json(),
            "timePreset": timePreset,
            "outputTimezone": outputTimezone,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ParseJHDFiles(cls, personName, rawTextData):
        """
         Easyly import Jaganath Hora .jhd files into VedAstro. Yeah Competition drives growth 
        :return: Person
         """
        endpoint = "ParseJHDFiles"
        params = {
            "personName": personName,
            "rawTextData": rawTextData,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionAlpacaTemplateLoRA(cls, birthTime):
        """
         All horoscope predictions as Alpaca Template ready for LoRA training in JSON 
        :return: Task`1
         """
        endpoint = "HoroscopePredictionAlpacaTemplateLoRA"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionsForLargeAstrologyModelTrainingData(cls, birthTime):
        """
         Generates horoscope predictions formatted for training large astrology models. 
        :return: Task`1
         """
        endpoint = "HoroscopePredictionsForLargeAstrologyModelTrainingData"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionsWithBazi(cls, birthTime, sortByWeight):
        """
         Generates horoscope predictions including Bazi data. 
        :return: Task`1
         """
        endpoint = "HoroscopePredictionsWithBazi"
        params = {
            "birthTime": birthTime.to_json(),
            "sortByWeight": sortByWeight,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictions(cls, birthTime, filterTags, sortByWeight):
        """
         Given a birth time will calculate all predictions that match for given birth time. Default includes all predictions ie Yoga Planets in Sign AshtakavargaYoga Can be filtered. If sortByWeight is true the returned list will be ordered descending by Weight. 
        :return: List`1
         """
        endpoint = "HoroscopePredictions"
        params = {
            "birthTime": birthTime.to_json(),
            "filterTags": filterTags,
            "sortByWeight": sortByWeight,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FortunaPoint(cls, ascZodiacSignName, time):
        """
         Calculate Fortuna Point for a given birth time place. Returns Sign Number from Lagna for KP system a fastmoving point which can differentiate between two early births as twins. 
        :return: Int32
         """
        endpoint = "FortunaPoint"
        params = {
            "ascZodiacSignName": ascZodiacSignName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DestinyPoint(cls, time, ascZodiacSignName):
        """
         Calculate Destiny Point for a given birth time place. Returns Sign Number from Lagna 
        :return: Int32
         """
        endpoint = "DestinyPoint"
        params = {
            "time": time.to_json(),
            "ascZodiacSignName": ascZodiacSignName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def YoniKutaAnimal(cls, birthTime):
        """
         Given a person will give yoni kuta animal with sex 
        :return: String
         """
        endpoint = "YoniKutaAnimal"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def YoniKutaAnimalFromConstellation(cls, sign):
        """
         Given a constellation will give animal with sex used for yoni kuta calculations and body appearance prediction 
        :return: ConstellationAnimal
         """
        endpoint = "YoniKutaAnimalFromConstellation"
        params = {
            "sign": sign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SkyChart(cls, time):
        """
         Get sky chart at a given time. SVG image file. URL can be used like a image source link 
        :return: Task`1
         """
        endpoint = "SkyChart"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SouthIndianChart(cls, time, chartType):
        """
         Creates a kundali chart from D1 to D20. In south indian style. URL can be used like a SVG image source link 
        :return: String
         """
        endpoint = "SouthIndianChart"
        params = {
            "time": time.to_json(),
            "chartType": chartType,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NorthIndianChart(cls, time, chartType):
        """
         Creates a kundali chart from D1 to D20. In north indian style. URL can be used like a SVG image source link 
        :return: String
         """
        endpoint = "NorthIndianChart"
        params = {
            "time": time.to_json(),
            "chartType": chartType,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeToJulianDay(cls, time):
        """
         special function localized to allow caching note there is another version that does caching 
        :return: Double
         """
        endpoint = "TimeToJulianDay"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ConvertLmtToJulian(cls, time):
        """
         Convert LMT to Julian Days used in Swiss Ephemeris 
        :return: Double
         """
        endpoint = "ConvertLmtToJulian"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DistanceBetweenPlanets(cls, planet1, planet2, time):
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for. Calculation in Nirayana longitudes Calculates longitudes for you 
        :return: Angle
         """
        endpoint = "DistanceBetweenPlanets"
        params = {
            "planet1": planet1.value,
            "planet2": planet2.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GreenwichApparentInJulianDays(cls, time):
        """
         Greenwich Apparent In Julian Days 
        :return: Double
         """
        endpoint = "GreenwichApparentInJulianDays"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LocalApparentTime(cls, time):
        """
         Shows local apparent time from Swiss Eph 
        :return: DateTime
         """
        endpoint = "LocalApparentTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SwissEphemeris(cls, planetName, time):
        """
         Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Swiss Ephemeris swe_calc wrapper for open API 
        :return: Object
         """
        endpoint = "SwissEphemeris"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SwissEphemerisAll(cls, time):
        """
         For all planets including Pluto Neptune Uranus Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Uses Swiss Ephemeris directly to get values 
        :return: Dictionary`2
         """
        endpoint = "SwissEphemerisAll"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetSameHouseWithHouseLord(cls, houseNumber, planet, birthTime):
        """
         Checks if a planet is same house not nessarly conjunct with the lord of a certain house Example Is Sun joined with lord of 9th 
        :return: Boolean
         """
        endpoint = "IsPlanetSameHouseWithHouseLord"
        params = {
            "houseNumber": houseNumber,
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseNatureScore(cls, birthTime, inputHouse):
        """
         Based on Shadvarga get nature of house for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary Experimental Code 
        :return: Double
         """
        endpoint = "HouseNatureScore"
        params = {
            "birthTime": birthTime.to_json(),
            "inputHouse": inputHouse.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNatureScore(cls, personBirthTime, inputPlanet):
        """
         Based on Shadvarga get nature of planet for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary 
        :return: Int32
         """
        endpoint = "PlanetNatureScore"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "inputPlanet": inputPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DhumaLongitude(cls, time):
        """
         Dhuma Sun s longitude 13320 
        :return: Angle
         """
        endpoint = "DhumaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def VyatipaataLongitude(cls, time):
        """
         360Dhumas longitude 
        :return: Angle
         """
        endpoint = "VyatipaataLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PariveshaLongitude(cls, time):
        """
         Vyatipaatas longitude 180 
        :return: Angle
         """
        endpoint = "PariveshaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IndrachaapaLongitude(cls, time):
        """
         360 Pariveshas longitude 
        :return: Angle
         """
        endpoint = "IndrachaapaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def UpaketuLongitude(cls, time):
        """
         Indrachaapas longitude 1640 
        :return: Angle
         """
        endpoint = "UpaketuLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def KaalaLongitude(cls, time):
        """
         Kaala rises at the middle of Suns part. In other words we find the time at the middle of Suns part and find lagna rising then. That gives Kaalas longitude. 
        :return: Angle
         """
        endpoint = "KaalaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MrityuLongitude(cls, time):
        """
         Mrityu rises at the middle of Marss part. 
        :return: Angle
         """
        endpoint = "MrityuLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ArthaprahaaraLongitude(cls, time):
        """
         Artha Praharaka rises at the middle of Mercurys part. 
        :return: Angle
         """
        endpoint = "ArthaprahaaraLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def YamaghantakaLongitude(cls, time):
        """
         Yama ghantaka rises at the middle of Jupiters part 
        :return: Angle
         """
        endpoint = "YamaghantakaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GulikaLongitude(cls, time):
        """
         Gulika rises at the middle of Saturns part. 
        :return: Angle
         """
        endpoint = "GulikaLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaandiLongitude(cls, time):
        """
         Maandi rises at the beginning of Saturns part. 
        :return: Angle
         """
        endpoint = "MaandiLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def UpagrahaLongitude(cls, time, relatedPlanet, upagrahaPart):
        """
         Calculates longitudes for the non sun based Upagrahas subplanets 
        :return: Angle
         """
        endpoint = "UpagrahaLongitude"
        params = {
            "time": time.to_json(),
            "relatedPlanet": relatedPlanet,
            "upagrahaPart": upagrahaPart,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def UpagrahaPartNumber(cls, inputTime, inputPlanet):
        """
         Depending on whether one is born during the day or the night we divide the length of the daynight into 8 equal parts. Each part is assigned a planet. Given a planet and time the part number will be returned. Each part is 128 1.5 hours. 
        :return: Int32
         """
        endpoint = "UpagrahaPartNumber"
        params = {
            "inputTime": inputTime.to_json(),
            "inputPlanet": inputPlanet,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsUpagraha(cls, planet):
        """
         Given a planet name will tell if it is an Upagraha planet 
        :return: Boolean
         """
        endpoint = "IsUpagraha"
        params = {
            "planet": planet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SarvashtakavargaChart(cls, birthTime):
        """
         When the benefic points contributed by each planet in Bhinnashtakavargas different signs are added we get a Sarvashtakavarga. A total of 337 benefic points are contributed by the seven planets to various houses in relation to seven planets and the lagna. 
        :return: Sarvashtakavarga
         """
        endpoint = "SarvashtakavargaChart"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhinnashtakavargaChart(cls, birthTime):
        """
         Seven different charts are thus possible for the seven different planets. These are called as Bhinnashtakavargas. The position of each planet in the natal chart is of primary consideration. 
        :return: Bhinnashtakavarga
         """
        endpoint = "BhinnashtakavargaChart"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAshtakvargaBindu(cls, planet, signToCheck, time):
        """
         Give a planet and sign and ashtakvarga bindu can be calculated uses Bhinnashtakavarga EXP In the Suns own Ashtakvarga there are 5 bindus in Aries NOTE ON USE Ashtakvarga System pg.128 For example in the Standard Horoscope the Suns transit of Aries 3rd from Moon should prove favorable. In the Suns own Ashtakvarga there are 5 bindus in Aries. Therefore the good effects produced should be to the extent of 62. The Suns transit of Capricorn 12th from the Moon should prove adverse. Capricorn has no bindus.Therefore the evil results to be produced by this transit are to the brim. 
        :return: Int32
         """
        endpoint = "PlanetAshtakvargaBindu"
        params = {
            "planet": planet.value,
            "signToCheck": signToCheck.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAshtakvargaBinduByPlanet(cls, mainAshtakvargaPlanet, planetToCheck, time):
        """
         Example Get Venus bindu in Mercurys Ashtakvarga main planet 
        :return: Int32
         """
        endpoint = "PlanetAshtakvargaBinduByPlanet"
        params = {
            "mainAshtakvargaPlanet": mainAshtakvargaPlanet.value,
            "planetToCheck": planetToCheck.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetOwnAshtakvargaBindu(cls, planet, time):
        """
         Gets bindus for planet in its own Ashtakavarga in the sign it is in 
        :return: Int32
         """
        endpoint = "PlanetOwnAshtakvargaBindu"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GocharaKakshas(cls, checkTime, birthTime):
        """
         Kakshyas for daily use The concept of Kakshyas can be employed for daily use. The method of this application is simple. Prepare the Prastaraka charts for the seven planets. Then find out the longitudes of each of the seven planets on a given day. In the Prastaraka of the Sun see if the transiting Sun is passing through a Kakshya with a benefic point. For the Moons transit consider the Prastaraka of the Moon. See for all the planets. When several planets are transiting the Kakshyas where the natal planets have contributed benefic points that day is auspicious. When several planets transit the Kakshyas where there are no benefic points it is adverse time for the native The Concept of Kakshya The Prastaraka charts for different planets can be represented in a different manner to make use of the concept of Kakshyas. Each rashi or sign is divided into eight equal parts or Kakshyas The Prastaraka chart for each planet can thus be readjusted to bring in the concept of the Kakshyas. A planet is considered to be productive of benefic results when it transits a Kakshya where there is a benefic point 
        :return: GocharaKakshas
         """
        endpoint = "GocharaKakshas"
        params = {
            "checkTime": checkTime.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAshtakavargaReducedBindu(cls, planet, sign, birthTime):
        """
         Returns reduced bindu count for a planet at a specific sign after Trikona and Ekadhipatya reductions BV Raman pp.1418. 
        :return: Int32
         """
        endpoint = "PlanetAshtakavargaReducedBindu"
        params = {
            "planet": planet.value,
            "sign": sign.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAshtakavargaReductions(cls, planet, birthTime):
        """
         Returns full reduction result raw afterTrikona afterEkadhipatya for a planet. 
        :return: AshtakavargaReductionResult
         """
        endpoint = "PlanetAshtakavargaReductions"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSodyaPinda(cls, planet, birthTime, useReduced):
        """
         Calculates Sodya Pinda for a planets Ashtakavarga BV Raman Chapter XIV pp.139147. Sodya Pinda Rasi Pinda Graha Pinda. Used in longevity and timing predictions. 
        :return: SodyaPindaResult
         """
        endpoint = "PlanetSodyaPinda"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
            "useReduced": useReduced,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AshtakavargaLongevity(cls, birthTime):
        """
         Gross longevity estimate using Ashtakavarga Sodya Pinda method. Per BV Raman Method A pp.139147 SodyaPinda 7 27. Returns years. This is gross longevity before Haranas combustiondebilitation adjustments. 
        :return: Double
         """
        endpoint = "AshtakavargaLongevity"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaPeriodAshtakavargaStrength(cls, dasaPlanet, birthTime):
        """
         Returns Ashtakavargabased strength for a Dasa planet 0100 scale. Based on planets Sodya Pinda normalized to percentage. Higher Sodya Pinda stronger Dasa period. Typical range 80250. 
        :return: Double
         """
        endpoint = "DasaPeriodAshtakavargaStrength"
        params = {
            "dasaPlanet": dasaPlanet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SarvashtakavargaReductions(cls, birthTime):
        """
         Sarvashtakavarga with Mandala Sodhana Raw mod 12 Trikona Ekadhipatya BV Raman pp.1820. 
        :return: SarvashtakavargaReductionResult
         """
        endpoint = "SarvashtakavargaReductions"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def RekhaSarvashtakavargaReductions(cls, birthTime):
        """
         Rekha Sarvashtakavarga 56bindus with full reduction pipeline BV Raman pp.2122. 
        :return: SarvashtakavargaReductionResult
         """
        endpoint = "RekhaSarvashtakavargaReductions"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SarvashtakavargaSodyaPinda(cls, birthTime):
        """
         Sodya Pinda calculated from Sarvashtakavarga reduced figures. 
        :return: SodyaPindaResult
         """
        endpoint = "SarvashtakavargaSodyaPinda"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def RekhaSodyaPinda(cls, birthTime):
        """
         Sodya Pinda calculated from Rekha Sarvashtakavarga reduced figures. 
        :return: SodyaPindaResult
         """
        endpoint = "RekhaSodyaPinda"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AshtakavargaTransitPrediction(cls, planet, houseFromPlanet, divisor, birthTime, useRawBindus):
        """
         Universal Ashtakavarga transit prediction formula BV Raman pp.139165. result SodyaPinda bindus_in_house divisor. Divisor 27nakshatra 12sign. 
        :return: TransitPredictionResult
         """
        endpoint = "AshtakavargaTransitPrediction"
        params = {
            "planet": planet.value,
            "houseFromPlanet": houseFromPlanet,
            "divisor": divisor,
            "birthTime": birthTime.to_json(),
            "useRawBindus": useRawBindus,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathBySaturn1(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathBySaturn1"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathBySun(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathBySun"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathBySaturn2(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathBySaturn2"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathBySaturnSign(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathBySaturnSign"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FatherDeathBySunSign(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "FatherDeathBySunSign"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MotherDeathBySaturn1(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MotherDeathBySaturn1"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MotherDeathByJupiterAndSun(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MotherDeathByJupiterAndSun"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MotherDeathBySaturn2(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MotherDeathBySaturn2"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BrotherAfflictionBySaturn(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "BrotherAfflictionBySaturn"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BrotherProsperityByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "BrotherProsperityByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MentalBalanceByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MentalBalanceByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MentalAfflictionBySaturn(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MentalAfflictionBySaturn"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CareerLossBySaturn(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "CareerLossBySaturn"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChildBirthByJupiter1(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "ChildBirthByJupiter1"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChildBirthByJupiter2(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "ChildBirthByJupiter2"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChildBirthMonthBySun(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "ChildBirthMonthBySun"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChildBirthStar(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "ChildBirthStar"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ChildLagna(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "ChildLagna"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarriageByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MarriageByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarriageSignByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MarriageSignByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarriageMonthBySun(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "MarriageMonthBySun"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SpouseDeathByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "SpouseDeathByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NativeDeathBySaturn(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "NativeDeathBySaturn"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NativeDeathByJupiter(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "NativeDeathByJupiter"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NativeDeathMonthBySun(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "NativeDeathMonthBySun"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaAfflictionBySaturn(cls, bhava, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "BhavaAfflictionBySaturn"
        params = {
            "bhava": bhava,
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaImprovementBySaturn(cls, bhava, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "BhavaImprovementBySaturn"
        params = {
            "bhava": bhava,
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DeathMonthFromSarvashtakavarga(cls, t):
        """
        Empty sample text
        :return: TransitPredictionResult
         """
        endpoint = "DeathMonthFromSarvashtakavarga"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DetailedAshtakavargaLongevity(cls, birthTime):
        """
         Detailed perplanet longevity with Haranas BV Raman pp.139165. Includes combustion debilitation enemy sign reductions. Converts lunar to solar years. 
        :return: LongevityResult
         """
        endpoint = "DetailedAshtakavargaLongevity"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SarvashtakavargaLongevityDetailed(cls, birthTime):
        """
         Method B longevity using Sarvashtakavarga Sodya Pinda BV Raman pp.139165. 
        :return: LongevityResult
         """
        endpoint = "SarvashtakavargaLongevityDetailed"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GocharaZodiacSignCountFromMoon(cls, birthTime, currentTime, planet):
        """
         Gets the Gochara sign number which is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: Int32
         """
        endpoint = "GocharaZodiacSignCountFromMoon"
        params = {
            "birthTime": birthTime.to_json(),
            "currentTime": currentTime.to_json(),
            "planet": planet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsGocharaObstructed(cls, planet, gocharaHouse, birthTime, currentTime):
        """
         Check if there is an obstruction to a given Gochara obstructing housepoint Vedhanka 
        :return: Boolean
         """
        endpoint = "IsGocharaObstructed"
        params = {
            "planet": planet.value,
            "gocharaHouse": gocharaHouse,
            "birthTime": birthTime.to_json(),
            "currentTime": currentTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInGocharaHouse(cls, birthTime, currentTime, gocharaHouse):
        """
         Gets all the planets in a given Gochara House Note Gochara House number is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: List`1
         """
        endpoint = "PlanetsInGocharaHouse"
        params = {
            "birthTime": birthTime.to_json(),
            "currentTime": currentTime.to_json(),
            "gocharaHouse": gocharaHouse,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Vedhanka(cls, planet, house):
        """
         Gets the Vedhanka point of obstruction used for Gohchara calculations. The data returned comes from a fixed table. NOTE Planet exceptions are not accounted for here. Return 0 when no obstruction point exists Reference Hindu Predictive Astrology pg. 257 
        :return: Int32
         """
        endpoint = "Vedhanka"
        params = {
            "planet": planet.value,
            "house": house,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsGocharaOccurring(cls, birthTime, time, planet, gocharaHouse):
        """
         Is SunGocharaInHouse1 Checks if a Gochara is occuring for a planet in a given house without any obstructions at a given time Note Basically a wrapper method for Gochra event calculations 
        :return: Boolean
         """
        endpoint = "IsGocharaOccurring"
        params = {
            "birthTime": birthTime.to_json(),
            "time": time.to_json(),
            "planet": planet.value,
            "gocharaHouse": gocharaHouse,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetGocharaBindu(cls, birthTime, nowTime, planet, bindu):
        """
         Checks if a given planets with given number of bindu is transiting now Gochara 
        :return: Boolean
         """
        endpoint = "IsPlanetGocharaBindu"
        params = {
            "birthTime": birthTime.to_json(),
            "nowTime": nowTime.to_json(),
            "planet": planet.value,
            "bindu": bindu,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetGocharaBinduResult(cls, birthTime, nowTime, planet, bindu):
        """
         Like IsPlanetGocharaBindu but returns rich CalculatorResult with dynamic BV Ramancompliant transit description intensity house karakatwa kakshya. 
        :return: CalculatorResult
         """
        endpoint = "IsPlanetGocharaBinduResult"
        params = {
            "birthTime": birthTime.to_json(),
            "nowTime": nowTime.to_json(),
            "planet": planet.value,
            "bindu": bindu,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetCharaDasaAtTime(cls, birthTime, checkTime):
        """
         Calculates the Chara Dasa sign at the specified checkTime based on the birthTime. 
        :return: DashaPeriod
         """
        endpoint = "GetCharaDasaAtTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaForLife(cls, birthTime, levels, precisionHours, scanYears):
        """
         Given a start time and end time and birth time will calculate all dasa periods in nice JSON table format You can also set how many levels of dasa you want to calculate default is 4 7 Levels Dasa Bhukti Antaram Sukshma Prana Avi Prana Viprana 
        :return: JObject
         """
        endpoint = "DasaForLife"
        params = {
            "birthTime": birthTime.to_json(),
            "levels": levels,
            "precisionHours": precisionHours,
            "scanYears": scanYears,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtRange(cls, birthTime, startTime, endTime, levels, precisionHours):
        """
         Calculates dasa for a specific time frame 
        :return: String
         """
        endpoint = "DasaAtRange"
        params = {
            "birthTime": birthTime.to_json(),
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "levels": levels,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtTime(cls, birthTime, checkTime, levels):
        """
         Calculates the Dasa period active at a specific time. 
        :return: JObject
         """
        endpoint = "DasaAtTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "levels": levels,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaForNow(cls, birthTime, levels):
        """
         Calculates the Dasa period active right now at birth location. 
        :return: JObject
         """
        endpoint = "DasaForNow"
        params = {
            "birthTime": birthTime.to_json(),
            "levels": levels,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDasaEffectsBasedOnIshtaKashta(cls, planetName, birthTime):
        """
         Reference Bhava Graha Bala pg. 104 A planet with more lshta Phala is always supposed to be inclined to do good in its Dasa or Bhukti while a planet with more Kashta Phala is supposed to give rise to more evil results. In case of Venus in the Standard Horoscope the Kashta predominates over Ishta. Therefore in his Dasa or Bhukti Venus will give aJl sorts of miseries with regard to the bhavas ruled or aspected by him. As lord of the 5th house in such a circumstance Saturn is sure to cause loss of children and producing evil on this account. 
        :return: String
         """
        endpoint = "PlanetDasaEffectsBasedOnIshtaKashta"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAllEventDataGroupedByTag(cls, ):
        """
         Gets all events names grouped by tags for printing on website for user selection when generating events chart. 
        :return: JObject
         """
        endpoint = "GetAllEventDataGroupedByTag"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAllEventsChartAlgorithms(cls, ):
        """
         Gets all possible algorithm functions for printing on website for user selection when generating events chart. 
        :return: JArray
         """
        endpoint = "GetAllEventsChartAlgorithms"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetHouseTags(cls, house):
        """
         keywords or tag related to a house 
        :return: String
         """
        endpoint = "GetHouseTags"
        params = {
            "house": house.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetSignTags(cls, zodiacName):
        """
         Given a zodiac sign will return astro keywords related to sign These details would be highly useful in the delineation of character and mental disposition SourceHindu Predictive Astrology pg.16 
        :return: String
         """
        endpoint = "GetSignTags"
        params = {
            "zodiacName": zodiacName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetPlanetTagsFromList(cls, planetList):
        """
         Gets combined tags for a list of planets. 
        :return: String
         """
        endpoint = "GetPlanetTagsFromList"
        params = {
            "planetList": planetList,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetPlanetTags(cls, lordOfHouse):
        """
         Get keywords related to a planet. 
        :return: String
         """
        endpoint = "GetPlanetTags"
        params = {
            "lordOfHouse": lordOfHouse.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetHouseType(cls, houseNumber):
        """
         Source Hindu Predictive Astrology pg.17 
        :return: String
         """
        endpoint = "GetHouseType"
        params = {
            "houseNumber": houseNumber.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetDasaInfoForAscendant(cls, ascendantName):
        """
         Get general planetary info for persons dasa hardcoded table It is intended to be used to interpret dasa predictions as such should be displayed next to dasa chart. This method is direct translation from the book. Similar to method GetPlanetDasaNature Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology 
        :return: AscendantDasaInfo
         """
        endpoint = "GetDasaInfoForAscendant"
        params = {
            "ascendantName": ascendantName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignProperties(cls, inputSign):
        """
         Gets the characteristic of signs 
        :return: SignProperties
         """
        endpoint = "SignProperties"
        params = {
            "inputSign": inputSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PredictHealthConditions(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "PredictHealthConditions"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetMotionName(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetMotion
         """
        endpoint = "PlanetMotionName"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectingHouse(cls, planet, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectingHouse"
        params = {
            "planet": planet.value,
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectingHouse(cls, planet, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectingHouse"
        params = {
            "planet": planet.value,
            "houseNumber": houseNumber,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsWaxingMoon(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsWaxingMoon"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsWaningMoon(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsWaningMoon"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def VedicDayStartTime(cls, inputTime):
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        endpoint = "VedicDayStartTime"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def KujaDosaScore(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "KujaDosaScore"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ClassifyForKartari(cls, planet, coOccupants):
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        endpoint = "ClassifyForKartari"
        params = {
            "planet": planet.value,
            "coOccupants": coOccupants,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShubKartariPlanets(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "ShubKartariPlanets"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PaapaKartariPlanets(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PaapaKartariPlanets"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ShubKartariHouses(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "ShubKartariHouses"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PaapaKartariHouses(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PaapaKartariHouses"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DispositorFromOwnHouses(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "DispositorFromOwnHouses"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DispositorFromLagna(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "DispositorFromLagna"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DispositorFromMoon(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "DispositorFromMoon"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DispositorConjunctWith(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "DispositorConjunctWith"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AspectReceivedByDispositor(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AspectReceivedByDispositor"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HousesOwnedByPlanet(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "HousesOwnedByPlanet"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseFromSignName(cls, zodiacName, inputTime):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        endpoint = "HouseFromSignName"
        params = {
            "zodiacName": zodiacName.value,
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DayDurationHours(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "DayDurationHours"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsNightBirth(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsNightBirth"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsDayBirth(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsDayBirth"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GhatakaChakra(cls, time, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "GhatakaChakra"
        params = {
            "time": time.to_json(),
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfConstellation(cls, constellation):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfConstellation"
        params = {
            "constellation": constellation,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInWaterySign(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInWaterySign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LunarDay(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: LunarDay
         """
        endpoint = "LunarDay"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsSuklaPaksha(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsSuklaPaksha"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MoonConstellation(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        endpoint = "MoonConstellation"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetConstellation(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        endpoint = "PlanetConstellation"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Tarabala(cls, time, person):
        """
        NO DESC FOUND!! ERROR
        :return: Tarabala
         """
        endpoint = "Tarabala"
        params = {
            "time": time.to_json(),
            "person": person,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chandrabala(cls, time, person):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "Chandrabala"
        params = {
            "time": time.to_json(),
            "person": person,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MoonSignName(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "MoonSignName"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LagnaSignName(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "LagnaSignName"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NithyaYoga(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: NithyaYoga
         """
        endpoint = "NithyaYoga"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Karana(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Karana
         """
        endpoint = "Karana"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunSign(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacSign
         """
        endpoint = "SunSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeSunEnteredCurrentSign(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        endpoint = "TimeSunEnteredCurrentSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeSunLeavesCurrentSign(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        endpoint = "TimeSunLeavesCurrentSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInHouseBasedOnLongitudes(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInHouseBasedOnLongitudes"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInHouseBasedOnSign(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInHouseBasedOnSign"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInSign(cls, signName, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInSign"
        params = {
            "signName": signName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetLongitude(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetFixedLongitude(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetFixedLongitude"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HousePlanetOccupiesBasedOnLongitudes(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        endpoint = "HousePlanetOccupiesBasedOnLongitudes"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HousePlanetOccupiesBasedOnSign(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        endpoint = "HousePlanetOccupiesBasedOnSign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseAllPlanetOccupiesBasedOnLongitudes(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        endpoint = "HouseAllPlanetOccupiesBasedOnLongitudes"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfHouse(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfHouse"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetLordOfZodiacSign(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "PlanetLordOfZodiacSign"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetLordOfConstellation(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "PlanetLordOfConstellation"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfHouseList(cls, houseList, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "LordOfHouseList"
        params = {
            "houseList": houseList,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseConstellationLord(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        endpoint = "AllHouseConstellationLord"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseConstellationLord(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "HouseConstellationLord"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseConstellation(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        endpoint = "HouseConstellation"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHousePlanetsInHouseBasedOnSign(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        endpoint = "AllHousePlanetsInHouseBasedOnSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignCountedFromInputSign(cls, inputSign, countToNextSign):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "SignCountedFromInputSign"
        params = {
            "inputSign": inputSign.value,
            "countToNextSign": countToNextSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignCountedFromPlanetSign(cls, countToNextSign, startPlanet, inputTime):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "SignCountedFromPlanetSign"
        params = {
            "countToNextSign": countToNextSign,
            "startPlanet": startPlanet.value,
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignCountedFromLagnaSign(cls, countToNextSign, inputTime):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "SignCountedFromLagnaSign"
        params = {
            "countToNextSign": countToNextSign,
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseCountedFromInputHouse(cls, inputHouseNumber, countToNextHouse):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "HouseCountedFromInputHouse"
        params = {
            "inputHouseNumber": inputHouseNumber,
            "countToNextHouse": countToNextHouse,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInSign(cls, planetName, signInput, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInSign"
        params = {
            "planetName": planetName.value,
            "signInput": signInput.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignsPlanetIsAspecting(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "SignsPlanetIsAspecting"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInMoolatrikona(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInMoolatrikona"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetInSign(cls, signName, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetInSign"
        params = {
            "signName": signName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseLongitude(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: House
         """
        endpoint = "HouseLongitude"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Panchaka(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: PanchakaName
         """
        endpoint = "Panchaka"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfWeekday(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfWeekday"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfWeekday(cls, weekday):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfWeekday"
        params = {
            "weekday": weekday,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IshtaKaala(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "IshtaKaala"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeforeSunrise(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeforeSunrise"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoraAtBirth(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "HoraAtBirth"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunriseTime(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        endpoint = "SunriseTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunsetTime(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Time
         """
        endpoint = "SunsetTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NoonTime(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        endpoint = "NoonTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInTrikona(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInTrikona"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInKendra(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInKendra"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInUpachaya(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInUpachaya"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInKendra(cls, planetList, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInKendra"
        params = {
            "planetList": planetList,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInKendraFromPlanet(cls, kendraFrom, kendraTo, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInKendraFromPlanet"
        params = {
            "kendraFrom": kendraFrom.value,
            "kendraTo": kendraTo.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SignDistanceFromPlanetToPlanet(cls, startPlanet, endPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "SignDistanceFromPlanetToPlanet"
        params = {
            "startPlanet": startPlanet.value,
            "endPlanet": endPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseLordInHouseBasedOnLongitudes(cls, lordHouse, occupiedHouse, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHouseLordInHouseBasedOnLongitudes"
        params = {
            "lordHouse": lordHouse.value,
            "occupiedHouse": occupiedHouse.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseLordInHouseBasedOnSign(cls, lordHouse, occupiedHouse, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHouseLordInHouseBasedOnSign"
        params = {
            "lordHouse": lordHouse.value,
            "occupiedHouse": occupiedHouse.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ArudhaLagnaSign(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "ArudhaLagnaSign"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CountFromSignToSign(cls, startSign, endSign):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "CountFromSignToSign"
        params = {
            "startSign": startSign.value,
            "endSign": endSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CountFromConstellationToConstellation(cls, start, end):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "CountFromConstellationToConstellation"
        params = {
            "start": start,
            "end": end,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInHouseBasedOnLongitudes(cls, planet, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInHouseBasedOnLongitudes"
        params = {
            "planet": planet.value,
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInHouseBasedOnSign(cls, planet, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInHouseBasedOnSign"
        params = {
            "planet": planet.value,
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInHouseKP(cls, cusps, planetNirayanaDegrees, house):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInHouseKP"
        params = {
            "cusps": cusps,
            "planetNirayanaDegrees": planetNirayanaDegrees,
            "house": house.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsAllPlanetsInHouse(cls, planetList, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsAllPlanetsInHouse"
        params = {
            "planetList": planetList,
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsAnyPlanetsInHouse(cls, planetList, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsAnyPlanetsInHouse"
        params = {
            "planetList": planetList,
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetDebilitated(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetDebilitated"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetExaltedDegree(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetExaltedDegree"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetExaltedSign(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetExaltedSign"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsFullMoon(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsFullMoon"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsNewMoon(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsNewMoon"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsNaraRasi(cls, sign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsNaraRasi"
        params = {
            "sign": sign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsWaterSign(cls, moonSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsWaterSign"
        params = {
            "moonSign": moonSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsFireSign(cls, moonSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsFireSign"
        params = {
            "moonSign": moonSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthSign(cls, moonSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthSign"
        params = {
            "moonSign": moonSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsAirSign(cls, moonSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsAirSign"
        params = {
            "moonSign": moonSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetYogakarakaToLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetYogakarakaToLagna"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMarakaToLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetMarakaToLagna"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInOwnHouse(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInOwnHouse"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInOwnSign(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInOwnSign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInFriendSign(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInFriendSign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInEnemySign(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInEnemySign"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInEnemyHouse(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInEnemyHouse"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInFriendHouse(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInFriendHouse"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthVarna(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Varna
         """
        endpoint = "BirthVarna"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsSignsFromPlanet(cls, signsFromMoon, startPlanet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsSignsFromPlanet"
        params = {
            "signsFromMoon": signsFromMoon,
            "startPlanet": startPlanet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInASignFromLagna(cls, signsFromLagna, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInASignFromLagna"
        params = {
            "signsFromLagna": signsFromLagna,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsSignsFromPlanet(cls, signsFromList, startPlanet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsSignsFromPlanet"
        params = {
            "signsFromList": signsFromList,
            "startPlanet": startPlanet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsSignsFromPlanet(cls, signsFromList, birthTime, startPlanet):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsSignsFromPlanet"
        params = {
            "signsFromList": signsFromList,
            "birthTime": birthTime.to_json(),
            "startPlanet": startPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsSignsFromPlanet(cls, signsFromMoon, birthTime, startPlanet):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsSignsFromPlanet"
        params = {
            "signsFromMoon": signsFromMoon,
            "birthTime": birthTime.to_json(),
            "startPlanet": startPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInSignsFromLagna(cls, signsFromList, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInSignsFromLagna"
        params = {
            "signsFromList": signsFromList,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetsInSignsFromPlanet(cls, signsFromList, planetList, startPlanet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetsInSignsFromPlanet"
        params = {
            "signsFromList": signsFromList,
            "planetList": planetList,
            "startPlanet": startPlanet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetsInSignsFromLagna(cls, signsFromList, planetList, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetsInSignsFromLagna"
        params = {
            "signsFromList": signsFromList,
            "planetList": planetList,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAllHouseNirayanaMiddleLongitudes(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double[]
         """
        endpoint = "GetAllHouseNirayanaMiddleLongitudes"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseLongitudes(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllHouseLongitudes"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInConjunction(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInConjunction"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseFromPlanetByAspectOrKendra(cls, reference, target, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        endpoint = "HouseFromPlanetByAspectOrKendra"
        params = {
            "reference": reference.value,
            "target": target.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInFriendlyDrekkana(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInFriendlyDrekkana"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetVargottama(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetVargottama"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ArudhaOfHouse(cls, inputHouse, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName
         """
        endpoint = "ArudhaOfHouse"
        params = {
            "inputHouse": inputHouse.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInGopuraAmsha(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInGopuraAmsha"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MarakaPlanetList(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName[]
         """
        endpoint = "MarakaPlanetList"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsCruelNavamsa(cls, navamsaSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsCruelNavamsa"
        params = {
            "navamsaSign": navamsaSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HasBalarishtaExceptions(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "HasBalarishtaExceptions"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetsAspectingPlanet(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficPlanetsAspectingPlanet"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByMaleficPlanets(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByMaleficPlanets"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetExalted(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetExalted"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMercuryMalefic(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMercuryMalefic"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Nutation(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "Nutation"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AscendantDegreesToARMC(cls, ascendant, obliquityOfEcliptic, geographicLatitude, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "AscendantDegreesToARMC"
        params = {
            "ascendant": ascendant,
            "obliquityOfEcliptic": obliquityOfEcliptic,
            "geographicLatitude": geographicLatitude,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AyanamsaDegree(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "AyanamsaDegree"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSayanaLongitude(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "PlanetSayanaLongitude"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNirayanaLongitude(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "PlanetNirayanaLongitude"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextLunarEclipse(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        endpoint = "NextLunarEclipse"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextSolarEclipse(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        endpoint = "NextSolarEclipse"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetEphemerisLongitude(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "PlanetEphemerisLongitude"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSayanaLatitude(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "PlanetSayanaLatitude"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSpeed(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetSpeed"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ConstellationAtLongitude(cls, planetLongitude):
        """
        NO DESC FOUND!! ERROR
        :return: Constellation
         """
        endpoint = "ConstellationAtLongitude"
        params = {
            "planetLongitude": planetLongitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ZodiacSignAtLongitude(cls, longitude):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacSign
         """
        endpoint = "ZodiacSignAtLongitude"
        params = {
            "longitude": longitude,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LongitudeAtZodiacSign(cls, zodiacSign):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "LongitudeAtZodiacSign"
        params = {
            "zodiacSign": zodiacSign,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DayOfWeek(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: DayOfWeek
         """
        endpoint = "DayOfWeek"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfHoraFromWeekday(cls, hora, day):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfHoraFromWeekday"
        params = {
            "hora": hora,
            "day": day,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfHoraFromTime(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfHoraFromTime"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseJunctionPoint(cls, previousHouse, nextHouse):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "HouseJunctionPoint"
        params = {
            "previousHouse": previousHouse,
            "nextHouse": nextHouse,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfZodiacSign(cls, signName):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "LordOfZodiacSign"
        params = {
            "signName": signName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ZodiacSignsOwnedByPlanet(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "ZodiacSignsOwnedByPlanet"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextZodiacSign(cls, inputSign):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "NextZodiacSign"
        params = {
            "inputSign": inputSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextHouseNumber(cls, inputHouseNumber):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "NextHouseNumber"
        params = {
            "inputHouseNumber": inputHouseNumber,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetExaltationPoint(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacSign
         """
        endpoint = "PlanetExaltationPoint"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDebilitationPoint(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacSign
         """
        endpoint = "PlanetDebilitationPoint"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEvenSign(cls, planetSignName):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEvenSign"
        params = {
            "planetSignName": planetSignName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsOddSign(cls, planetSignName):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsOddSign"
        params = {
            "planetSignName": planetSignName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsFixedSign(cls, sunSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsFixedSign"
        params = {
            "sunSign": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMovableSign(cls, sunSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMovableSign"
        params = {
            "sunSign": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsCommonSign(cls, sunSign):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsCommonSign"
        params = {
            "sunSign": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPermanentRelationshipWithPlanet(cls, mainPlanet, secondaryPlanet):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToPlanetRelationship
         """
        endpoint = "PlanetPermanentRelationshipWithPlanet"
        params = {
            "mainPlanet": mainPlanet.value,
            "secondaryPlanet": secondaryPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ConvertJulianTimeToNormalTime(cls, julianTime):
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        endpoint = "ConvertJulianTimeToNormalTime"
        params = {
            "julianTime": julianTime,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GreenwichTimeFromJulianDays(cls, julianTime):
        """
        NO DESC FOUND!! ERROR
        :return: DateTimeOffset
         """
        endpoint = "GreenwichTimeFromJulianDays"
        params = {
            "julianTime": julianTime,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GreenwichLmtInJulianDays(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "GreenwichLmtInJulianDays"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LmtToUtc(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: DateTimeOffset
         """
        endpoint = "LmtToUtc"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FunctionalMaleficPlanetList(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "FunctionalMaleficPlanetList"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithMaleficPlanets(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithMaleficPlanets"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllMaleficPlanetsAspecting(cls, planetReceivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllMaleficPlanetsAspecting"
        params = {
            "planetReceivingAspect": planetReceivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMaleficToLagna(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetMaleficToLagna"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMercuryAfflicted(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMercuryAfflicted"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetBeneficToLagna(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetBeneficToLagna"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetFunctionalMalefic(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetFunctionalMalefic"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMaleficPlanetAspectHouse(cls, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMaleficPlanetAspectHouse"
        params = {
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetNaturalMalefic(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetNaturalMalefic"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NaturalMaleficPlanetList(cls, ):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "NaturalMaleficPlanetList"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PapaGrahasList(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PapaGrahasList"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetNaturalBenefic(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetNaturalBenefic"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NaturalBeneficPlanetList(cls, ):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "NaturalBeneficPlanetList"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SubhaGrahasList(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "SubhaGrahasList"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListForLagna(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficPlanetListForLagna"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PhysicallyHarmfulPlanetList(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PhysicallyHarmfulPlanetList"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMaleficForLagna(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetMaleficForLagna"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetPhysicallyHarmful(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetPhysicallyHarmful"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetBeneficLordForLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetBeneficLordForLagna"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMaleficLordForLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetMaleficLordForLagna"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetNeutralForLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetNeutralForLagna"
        params = {
            "planetName": planetName.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMercuryAfflictedByMalefics(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMercuryAfflictedByMalefics"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMoonBenefic(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMoonBenefic"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetList(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetList"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetBenefic(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetBenefic"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsAllMaleficsInUpachayas(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsAllMaleficsInUpachayas"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListInSign(cls, sign, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficPlanetListInSign"
        params = {
            "sign": sign.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMaleficPlanetInSign(cls, sign, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMaleficPlanetInSign"
        params = {
            "sign": sign.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PhysicallyHarmfulPlanetsAspectingHouse(cls, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PhysicallyHarmfulPlanetsAspectingHouse"
        params = {
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHarmfulPlanetAspectingHouse(cls, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHarmfulPlanetAspectingHouse"
        params = {
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPhysicallyHarmfulPlanetsAspecting(cls, planetReceivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPhysicallyHarmfulPlanetsAspecting"
        params = {
            "planetReceivingAspect": planetReceivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByPhysicallyHarmfulPlanets(cls, planetReceivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByPhysicallyHarmfulPlanets"
        params = {
            "planetReceivingAspect": planetReceivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPhysicallyHarmfulPlanetsConjunctWith(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPhysicallyHarmfulPlanetsConjunctWith"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithPhysicallyHarmfulPlanets(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithPhysicallyHarmfulPlanets"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMaleficPlanetInHouse(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsMaleficPlanetInHouse"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetHemmedByMalefics(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetHemmedByMalefics"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInBeneficSign(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInBeneficSign"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetWeak(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetWeak"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAfflicted(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAfflicted"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAfflictedSpecificallyByPlanets(cls, afflictedPlanet, damagingPlanets, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAfflictedSpecificallyByPlanets"
        params = {
            "afflictedPlanet": afflictedPlanet.value,
            "damagingPlanets": damagingPlanets,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTemporaryFriendList(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetTemporaryFriendList"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInGoodAspectToPlanet(cls, receivingAspect, transmitingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInGoodAspectToPlanet"
        params = {
            "receivingAspect": receivingAspect.value,
            "transmitingAspect": transmitingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInBadAspectToPlanet(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInBadAspectToPlanet"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetReceivingBadAspects(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetReceivingBadAspects"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInGoodAspectToHouse(cls, receivingAspect, transmitingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInGoodAspectToHouse"
        params = {
            "receivingAspect": receivingAspect.value,
            "transmitingAspect": transmitingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInBadAspectToHouse(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInBadAspectToHouse"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetInBadAspectToHouse(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInBadAspectToHouse"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficsInSignsFromPlanet(cls, signsFromList, startPlanet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficsInSignsFromPlanet"
        params = {
            "signsFromList": signsFromList,
            "startPlanet": startPlanet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficsInSignsFromLagna(cls, signsFromList, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficsInSignsFromLagna"
        params = {
            "signsFromList": signsFromList,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunAndMoonWellPlacedAndAspected(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "SunAndMoonWellPlacedAndAspected"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficsInKendra(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficsInKendra"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetListInSign(cls, sign, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetListInSign"
        params = {
            "sign": sign.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficPlanetInSign(cls, sign, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficPlanetInSign"
        params = {
            "sign": sign.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetsAspectingHouse(cls, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetsAspectingHouse"
        params = {
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficPlanetAspectHouse(cls, house, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficPlanetAspectHouse"
        params = {
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetsAspectingPlanet(cls, lord, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetsAspectingPlanet"
        params = {
            "lord": lord.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByBeneficPlanets(cls, lord, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByBeneficPlanets"
        params = {
            "lord": lord.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByEnemyPlanets(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByEnemyPlanets"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByFriendPlanets(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByFriendPlanets"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInEnemyConjunctionWith(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInEnemyConjunctionWith"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithEnemyPlanets(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithEnemyPlanets"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetsInFriendConjunctionWith(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetsInFriendConjunctionWith"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithFriendPlanets(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithFriendPlanets"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsBeneficPlanetInHouse(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsBeneficPlanetInHouse"
        params = {
            "houseNumber": houseNumber.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetRelationshipWithSign(cls, planetName, zodiacSignName, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToSignRelationship
         """
        endpoint = "PlanetRelationshipWithSign"
        params = {
            "planetName": planetName.value,
            "zodiacSignName": zodiacSignName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetCombinedRelationshipWithPlanet(cls, mainPlanet, secondaryPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToPlanetRelationship
         """
        endpoint = "PlanetCombinedRelationshipWithPlanet"
        params = {
            "mainPlanet": mainPlanet.value,
            "secondaryPlanet": secondaryPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetRelationshipWithHouse(cls, house, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToSignRelationship
         """
        endpoint = "PlanetRelationshipWithHouse"
        params = {
            "house": house.value,
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTemporaryRelationshipWithPlanet(cls, mainPlanet, secondaryPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetToPlanetRelationship
         """
        endpoint = "PlanetTemporaryRelationshipWithPlanet"
        params = {
            "mainPlanet": mainPlanet.value,
            "secondaryPlanet": secondaryPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetFortified(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetFortified"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInAspect(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInAspect"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAspectDegree(cls, receiver, trasmitter, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetAspectDegree"
        params = {
            "receiver": receiver.value,
            "trasmitter": trasmitter.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsAspectingPlanet(cls, receivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsAspectingPlanet"
        params = {
            "receivingAspect": receivingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HousesInAspect(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "HousesInAspect"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsAspectingHouse(cls, inputHouse, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsAspectingHouse"
        params = {
            "inputHouse": inputHouse.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByPlanet(cls, receiveingAspect, transmitingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByPlanet"
        params = {
            "receiveingAspect": receiveingAspect.value,
            "transmitingAspect": transmitingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseAspectedByPlanet(cls, receiveingAspect, transmitingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHouseAspectedByPlanet"
        params = {
            "receiveingAspect": receiveingAspect.value,
            "transmitingAspect": transmitingAspect.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithPlanet(cls, planetA, planetB, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithPlanet"
        params = {
            "planetA": planetA.value,
            "planetB": planetB.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllBeneficPlanetsInGoodConjunctionWith(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllBeneficPlanetsInGoodConjunctionWith"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithBeneficPlanets(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithBeneficPlanets"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHarmfulPlanetsInBadConjunctionWith(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllHarmfulPlanetsInBadConjunctionWith"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetReceivingHarmfulConjunctions(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetReceivingHarmfulConjunctions"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPowerPercentage(cls, inputPlanet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetPowerPercentage"
        params = {
            "inputPlanet": inputPlanet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PickOutStrongestPlanet(cls, relatedPlanets, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        endpoint = "PickOutStrongestPlanet"
        params = {
            "relatedPlanets": relatedPlanets,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetOrderedByStrength(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetOrderedByStrength"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetStrongInShadbala(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetStrongInShadbala"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseStrongInShadbala(cls, house, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHouseStrongInShadbala"
        params = {
            "house": house.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseWeakInShadbala(cls, house, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsHouseWeakInShadbala"
        params = {
            "house": house.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseStrengthCategory(cls, house, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Strength
         """
        endpoint = "HouseStrengthCategory"
        params = {
            "house": house.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetStrength(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "AllPlanetStrength"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHousesOrderedByStrength(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseName[]
         """
        endpoint = "AllHousesOrderedByStrength"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetShadbalaPinda(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetShadbalaPinda"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetStrength(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetStrength"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDrikBala(cls, target, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetDrikBala"
        params = {
            "target": target.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DistanceBetweenPlanets(cls, a, b):
        """
        NO DESC FOUND!! ERROR
        :return: Angle
         """
        endpoint = "DistanceBetweenPlanets"
        params = {
            "a": a,
            "b": b,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindViseshaDrishti(cls, dk, p):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "FindViseshaDrishti"
        params = {
            "dk": dk,
            "p": p.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindDrishtiValue(cls, dk):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "FindDrishtiValue"
        params = {
            "dk": dk,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNaisargikaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetNaisargikaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetChestaBala(cls, planetName, time, useSpecialSunMoon):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetChestaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
            "useSpecialSunMoon": useSpecialSunMoon,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Madhya(cls, epochToBirthDays, time1):
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        endpoint = "Madhya"
        params = {
            "epochToBirthDays": epochToBirthDays,
            "time1": time1.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EpochInterval(cls, time1):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "EpochInterval"
        params = {
            "time1": time1.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetRetrograde(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetRetrograde"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetCombust(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetCombust"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetCirculationTime(cls, planetName):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetCirculationTime"
        params = {
            "planetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSaptavargajaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetSaptavargajaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSthanaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetSthanaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDrekkanaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetDrekkanaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKendraBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetKendraBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetOjayugmarasyamsaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetOjayugmarasyamsaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKalaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetKalaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetYuddhaBala(cls, target, preKalaBalaValues, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetYuddhaBala"
        params = {
            "target": target.value,
            "preKalaBalaValues": preKalaBalaValues,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAyanaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetAyanaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDeclination(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetDeclination"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EclipticObliquity(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "EclipticObliquity"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetHoraBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetHoraBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAbdaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetAbdaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetMasaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetMasaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetVaraBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetVaraBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def YearAndMonthLord(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Object
         """
        endpoint = "YearAndMonthLord"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTribhagaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetTribhagaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetOchchaBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetOchchaBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPakshaBala(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetPakshaBala"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNathonnathaBala(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetNathonnathaBala"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDigBala(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "PlanetDigBala"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseStrength(cls, inputHouse, time):
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        endpoint = "HouseStrength"
        params = {
            "inputHouse": inputHouse.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaDrishtiBala(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseSubStrength
         """
        endpoint = "BhavaDrishtiBala"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaDigBala(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseSubStrength
         """
        endpoint = "BhavaDigBala"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaAdhipathiBala(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: HouseSubStrength
         """
        endpoint = "BhavaAdhipathiBala"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetListByShadbala(cls, personBirthTime, threshold):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetListByShadbala(cls, personBirthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficHouseListByShadbala(cls, personBirthTime, threshold):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficHouseListByShadbala(cls, personBirthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "BeneficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListByShadbala(cls, personBirthTime, threshold):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListByShadbala(cls, personBirthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficHouseListByShadbala(cls, personBirthTime, threshold):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficHouseListByShadbala(cls, personBirthTime):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "MaleficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ResidentialStrength(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "ResidentialStrength"
        params = {
            "planetName": planetName.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetIshtaKashtaScoreDegree(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetIshtaKashtaScoreDegree"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKashtaScore(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetKashtaScore"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetIshtaScore(cls, planet, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetIshtaScore"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CalculateAshtamangalaNumberFromShells(cls, leftPile, centerPile, rightPile, totalShells):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "CalculateAshtamangalaNumberFromShells"
        params = {
            "leftPile": leftPile,
            "centerPile": centerPile,
            "rightPile": rightPile,
            "totalShells": totalShells,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter7Predictions(cls, ashtamangalaRootNumber, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter7Predictions"
        params = {
            "ashtamangalaRootNumber": ashtamangalaRootNumber,
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter8Predictions(cls, ashtamangalaRootNumber, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter8Predictions"
        params = {
            "ashtamangalaRootNumber": ashtamangalaRootNumber,
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter17Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter17Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter18Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter18Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter23Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter23Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter24Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter24Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter29Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter29Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def RootNumberFriendship(cls, rootNumberA, rootNumberB):
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        endpoint = "RootNumberFriendship"
        params = {
            "rootNumberA": rootNumberA,
            "rootNumberB": rootNumberB,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthNumber(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "BirthNumber"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DestinyNumber(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "DestinyNumber"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NameNumber(cls, inputText):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "NameNumber"
        params = {
            "inputText": inputText,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NameNumberPrediction(cls, fullName):
        """
        NO DESC FOUND!! ERROR
        :return: NumerologyPrediction
         """
        endpoint = "NameNumberPrediction"
        params = {
            "fullName": fullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AIGenerateNames(cls, nameDescription, numberOfNames, excludeNames):
        """
        NO DESC FOUND!! ERROR
        :return: Task`1
         """
        endpoint = "AIGenerateNames"
        params = {
            "nameDescription": nameDescription,
            "numberOfNames": numberOfNames,
            "excludeNames": excludeNames,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MainActivity(cls, birthTime, checkTime):
        """
        NO DESC FOUND!! ERROR
        :return: BirdActivity
         """
        endpoint = "MainActivity"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthYamaPanchaPakshi(cls, t):
        """
        NO DESC FOUND!! ERROR
        :return: BirthYama
         """
        endpoint = "BirthYamaPanchaPakshi"
        params = {
            "t": t.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PanchaPakshiBirthBird(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: BirdName
         """
        endpoint = "PanchaPakshiBirthBird"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)


