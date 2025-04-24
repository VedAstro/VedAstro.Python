# AUTO GENERATED ON 10:37 07/02/2025 +08:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any
import requests
import json
from enum import Enum


class Calculate:
    api_key = None
    base_url = "http://api.vedastro.org/api/Calculate"
    
    @classmethod
    def SetAPIKey(cls, api_key):
        cls.api_key = api_key
    
    @classmethod
    def _make_request(cls, endpoint, params):
        url = f"{cls.base_url}/{endpoint}"
        params["APIKey"] = cls.api_key
        query_string = "/".join(f"{key}/{value}" for key, value in params.items())
        full_url = f"{url}/{query_string}"
        response = requests.get(full_url)
        if response.status_code == 200:
            data = json.loads(response.text)
            if "Status" in data and data["Status"] == "Fail":
                print(data["Payload"])
            if "Payload" in data and data["Payload"]:
                if isinstance(data["Payload"], list):
                    return data["Payload"]
                else:
                    return list(data["Payload"].values())[0]
            else:
                raise ValueError("Payload is missing or empty")
        else:
            return f"Error: API request failed with status code {response.status_code}"

    @classmethod
    def FindBirthTimeByAnimal(cls, possibleBirthTime, precisionHours):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "FindBirthTimeByAnimal"
        params = {
            "Location": possibleBirthTime.geolocation.location_name,
            "Time": possibleBirthTime.url_time_string(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByRisingSign(cls, possibleBirthTime, precisionHours):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "FindBirthTimeByRisingSign"
        params = {
            "Location": possibleBirthTime.geolocation.location_name,
            "Time": possibleBirthTime.url_time_string(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeHouseStrengthPerson(cls, possibleBirthTime, precisionHours):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "FindBirthTimeHouseStrengthPerson"
        params = {
            "Location": possibleBirthTime.geolocation.location_name,
            "Time": possibleBirthTime.url_time_string(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BouncBackInputPlanet(cls, planetName, time):
        """
         Special debug function 
        :return: String
         """
        endpoint = "BouncBackInputPlanet"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BouncBackInputGeoLocation(cls, time):
        """
         Basic bounce back data to confirm validity or ML table needs 
        :return: GeoLocation
         """
        endpoint = "BouncBackInputGeoLocation"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BouncBackInputTime(cls, time):
        """
         Basic bounce back data to confirm validity or ML table needs 
        :return: String
         """
        endpoint = "BouncBackInputTime"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
        :return: GeoLocation
         """
        endpoint = "AddressToGeoLocation"
        params = {
            "address": address,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchLocation(cls, address):
        """
        Empty sample text
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
    def EventsAtTime(cls, birthTime, checkTime, eventTagList):
        """
         Gets all events occuring at given time. Basically a slice from Events Chart Can be used by LLM to interprate final prediction. Also known as Muhurtha 
        :return: List`1
         """
        endpoint = "EventsAtTime"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "eventTagList": eventTagList,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventsAtRange(cls, birthTime, startTime, endTime, eventTagList, precisionHours):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "EventsAtRange"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": startTime.geolocation.location_name,
            "Time": startTime.url_time_string(),
            "Location": endTime.geolocation.location_name,
            "Time": endTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "nameOfEvent": nameOfEvent,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventStartTime(cls, birthTime, checkTime, eventData, precisionInHours):
        """
        Empty sample text
        :return: Time
         """
        endpoint = "EventStartTime"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "eventData": eventData,
            "precisionInHours": precisionInHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EventEndTime(cls, birthTime, checkTime, eventData, precisionInHours):
        """
        Empty sample text
        :return: Time
         """
        endpoint = "EventEndTime"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
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
            "Location": maleBirthTime.geolocation.location_name,
            "Time": maleBirthTime.url_time_string(),
            "Location": femaleBirthTime.geolocation.location_name,
            "Time": femaleBirthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthTimeLocationAutoAIFill(cls, personFullName):
        """
        Empty sample text
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
        Empty sample text
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
    def HoroscopeChat(cls, birthTime, userQuestion, userId, sessionId):
        """
         Ask questions to AI astrologer about life horoscope predictions 
        :return: Task`1
         """
        endpoint = "HoroscopeChat"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "userQuestion": userQuestion,
            "userId": userId,
            "sessionId": sessionId,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopeChat2(cls, birthTime, userQuestion, userId, sessionId):
        """
        Empty sample text
        :return: Task
         """
        endpoint = "HoroscopeChat2"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "userQuestion": userQuestion,
            "userId": userId,
            "sessionId": sessionId,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopeChatFeedback(cls, answerHash, feedbackScore):
        """
        Empty sample text
        :return: Task`1
         """
        endpoint = "HoroscopeChatFeedback"
        params = {
            "answerHash": answerHash,
            "feedbackScore": feedbackScore,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopeFollowUpChat(cls, birthTime, followUpQuestion, primaryAnswerHash, userId, sessionId):
        """
        Empty sample text
        :return: Task`1
         """
        endpoint = "HoroscopeFollowUpChat"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "followUpQuestion": followUpQuestion,
            "primaryAnswerHash": primaryAnswerHash,
            "userId": userId,
            "sessionId": sessionId,
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
            "Location": maleBirthTime.geolocation.location_name,
            "Time": maleBirthTime.url_time_string(),
            "Location": femaleBirthTime.geolocation.location_name,
            "Time": femaleBirthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": startTime.geolocation.location_name,
            "Time": startTime.url_time_string(),
            "Location": endTime.geolocation.location_name,
            "Time": endTime.url_time_string(),
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
            "HouseName": house.value,
            "ZodiacName": sign.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseZodiacSign(cls, houseNumber, time):
        """
         Gets the zodiac sign at middle longitude of the house with degrees data Bhava Chalit 
        :return: ZodiacSign
         """
        endpoint = "HouseZodiacSign"
        params = {
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseZodiacSigns(cls, time):
        """
         Gets the zodiac sign at middle longitude of the house. 
        :return: Dictionary`2
         """
        endpoint = "AllHouseZodiacSigns"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHouseRasiSigns(cls, time):
        """
        Empty sample text
        :return: Dictionary`2
         """
        endpoint = "AllHouseRasiSigns"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
            "divisionalNo": divisionalNo,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DivisionalLongitude(cls, totalDegrees, divisionalNo):
        """
        Empty sample text
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "scanYear": scanYear,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromLagna(cls, transitPlanet, checkTime, birthTime):
        """
        Empty sample text
        :return: HouseName
         """
        endpoint = "TransitHouseFromLagna"
        params = {
            "PlanetName": transitPlanet.value,
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromNavamsaLagna(cls, transitPlanet, checkTime, birthTime):
        """
        Empty sample text
        :return: HouseName
         """
        endpoint = "TransitHouseFromNavamsaLagna"
        params = {
            "PlanetName": transitPlanet.value,
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromMoon(cls, transitPlanet, checkTime, birthTime):
        """
        Empty sample text
        :return: HouseName
         """
        endpoint = "TransitHouseFromMoon"
        params = {
            "PlanetName": transitPlanet.value,
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TransitHouseFromNavamsaMoon(cls, transitPlanet, checkTime, birthTime):
        """
        Empty sample text
        :return: HouseName
         """
        endpoint = "TransitHouseFromNavamsaMoon"
        params = {
            "PlanetName": transitPlanet.value,
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Murthi(cls, transitPlanet, checkTime, birthTime):
        """
        Empty sample text
        :return: String
         """
        endpoint = "Murthi"
        params = {
            "PlanetName": transitPlanet.value,
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AbstractActivity(cls, checkTime):
        """
         In each of the main activities the other four activities also occur as abstract subactivity for short duration of time gaps covering the complete duration of the main activity the period being 2 hrs. 24 min for Pancha Pakshi 
        :return: BirdActivity
         """
        endpoint = "AbstractActivity"
        params = {
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MainActivity(cls, birthTime, checkTime):
        """
         Each bird performs these five activities during each day and in night over the week days and during waxing and waning Moon cycles during the 5 YAMAS in day and 5 YAMAS in night in a stipulated order for Pancha Pakshi 
        :return: BirdActivity
         """
        endpoint = "MainActivity"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BirthYama(cls, inputTime):
        """
         These 5 elemental vibrations act in 5 gradations offaculties for stipulated time intervals called YAMAS consisting of 2 hrs. 24 mits. each 6 Ghatikas each over the 5 YAMAS in the day and 5 YAMAS in the night thus spread over evenly in 24 hours. 
        :return: BirthYama
         """
        endpoint = "BirthYama"
        params = {
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def VedicDayStartTime(cls, inputTime):
        """
         Given a time it will find out the start time of for that vedic day If time is before sunrise the previous day 
        :return: Time
         """
        endpoint = "VedicDayStartTime"
        params = {
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AbstractActivityStrength(cls, birthTime, checkTime):
        """
         yama works out to 2 hrs. 24 mts. of our modern time. It is to be noted that the beginning of the day is reckoned from Sun rise to Sun set in Hindu system. Similarly night is reckoned from Sun set to Sun rise on the following day thus consisting of 24 hours for one day. The timings of the five Yamas are the same during day and night for Pancha Pakshi 
        :return: Double
         """
        endpoint = "AbstractActivityStrength"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PanchaPakshiBirthBird(cls, birthTime):
        """
         Gets birth bird for a birth time. Sidhas have personified the elements as birds identifying each element under which an individual is born when these elements are all functioning differentially during each time gap. These 5 elemental vibrations are personified as PAKSHIS or BIRDS and the gradations of their faculities are named as 5 activities. This bird is called his birth Stellar Lunar bird. 
        :return: BirdName
         """
        endpoint = "PanchaPakshiBirthBird"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PanchaPakshiBirthBirdFromName(cls, name):
        """
         Ancients have evolved a method of identifying the birth bird of other individuals by recognising the first vowel sound that shoots out while uttering the name of such individual. Here we have to be very careful in identifying the first vowel sound and not the first vowel letter ofthe other mans name. In this system the vowels referred to are ofthe Dravidian Origin TAMIL and do not indicate the English vowel sounds. This should always be borne in mind. It should be remembered that the eleven vowels of Dravidian Tamil language are distributed among the 5 birds. These vowels and consonants which contain them are to be identified from the first sound of the name. Virtually these eleven vowel sounds are to be equated and sounded by the five English vowels A E I O and U. In this language U is uttered as V U VU to project the Dravidian sound. Except the sound I all other sounds have short and long vowels. From what has been explained so far it can be understood that for the same name the birds are different during bright half and dark halfperiods of Moon where we do not know the birth data of the other person and for such persons only we should use this system 
        :return: BirdName
         """
        endpoint = "PanchaPakshiBirthBirdFromName"
        params = {
            "name": name,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsWaxingMoon(cls, birthTime):
        """
         Given a time will return true if it is on Waxing moon or Shukla Paksha or Bright half 
        :return: Boolean
         """
        endpoint = "IsWaxingMoon"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsWaningMoon(cls, birthTime):
        """
         Given a time will return true if it is on Waning moon or Krishna Paksha or Dark half 
        :return: Boolean
         """
        endpoint = "IsWaningMoon"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FirstVowelSound(cls, word):
        """
         Given a name will extract out the 1st vowel sound. Used to get Pancha Pakshi bird when birth date not known 
        :return: String
         """
        endpoint = "FirstVowelSound"
        params = {
            "word": word,
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": ccc.geolocation.location_name,
            "Time": ccc.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSignTransit(cls, startTime, endTime, planetName):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "PlanetSignTransit"
        params = {
            "Location": startTime.geolocation.location_name,
            "Time": startTime.url_time_string(),
            "Location": endTime.geolocation.location_name,
            "Time": endTime.url_time_string(),
            "PlanetName": planetName.value,
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
            "Location": startTime.geolocation.location_name,
            "Time": startTime.url_time_string(),
            "Location": endTime.geolocation.location_name,
            "Time": endTime.url_time_string(),
            "PlanetName": planetName.value,
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "HouseName": houseName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": zodiacName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def TimeToJulianUniversalTime(cls, time):
        """
        Empty sample text
        :return: Double
         """
        endpoint = "TimeToJulianUniversalTime"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": inputBirthTime.geolocation.location_name,
            "Time": inputBirthTime.url_time_string(),
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
            "Location": inputBirthTime.geolocation.location_name,
            "Time": inputBirthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictions(cls, birthTime, filterTag):
        """
         Given a birth time will calculate all predictions that match for given birth time. Default includes all predictions ie Yoga Planets in Sign AshtakavargaYoga Can be filtered. 
        :return: List`1
         """
        endpoint = "HoroscopePredictions"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "filterTag": filterTag,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionNames(cls, birthTime):
        """
         Given a birth time will calculate all prediction names that match for given birth time example Moon House 8 10th Lord in 8th House note used by AI Chat when talking to Astro tuned LLM server 
        :return: List`1
         """
        endpoint = "HoroscopePredictionNames"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "ZodiacName": ascZodiacSignName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
            "ZodiacName": ascZodiacSignName.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
    def SkyChartGIF(cls, time):
        """
         Get sky chart as animated GIF. URL can be used like a image source link 
        :return: Task`1
         """
        endpoint = "SkyChartGIF"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet1.value,
            "PlanetName": planet2.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DistanceBetweenPlanets(cls, planet1, planet2):
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for Expects you to calculate longitude 
        :return: Angle
         """
        endpoint = "DistanceBetweenPlanets"
        params = {
            "planet1": planet1,
            "planet2": planet2,
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDasaNature(cls, birthTime, planet):
        """
         WARNING MARKED FOR DELETION ERONEOUS RESULTS NOT SUITED FOR INTENDED PURPOSE METHOD NOT VERIFIED This methods perpose is to define the final good or bad nature of planet in antaram. For now only data from chapter Keyplanets for Each Sign If this proves to be inacurate add more checks in this method. bindu points Similar to method GetDasaInfoForAscendant Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology TODO meant to determine nature of antram 
        :return: EventNature
         """
        endpoint = "PlanetDasaNature"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "PlanetName": planet.value,
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SwissEphemerisAll(cls, time):
        """
         For all planets including Pluto Neptune Uranus Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Uses Swiss Ephemeris directly to get values 
        :return: List`1
         """
        endpoint = "SwissEphemerisAll"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "HouseName": inputHouse.value,
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
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
            "PlanetName": inputPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetIshtaKashtaScoreDegree(cls, planet, birthTime):
        """
         Used for judging dasa good or bad Bala book pg 110 output range 5 to 5 
        :return: Double
         """
        endpoint = "PlanetIshtaKashtaScoreDegree"
        params = {
            "PlanetName": planet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKashtaScore(cls, planet, birthTime):
        """
         Kashta Phala Bad Strength of a Planet 
        :return: Double
         """
        endpoint = "PlanetKashtaScore"
        params = {
            "PlanetName": planet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetIshtaScore(cls, planet, birthTime):
        """
         Ishta Phala Good Strength of a Planet 
        :return: Double
         """
        endpoint = "PlanetIshtaScore"
        params = {
            "PlanetName": planet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "PlanetName": planet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Nutation(cls, time):
        """
         Gets nutation from Swiss Ephemeris
        :return: Double
         """
        endpoint = "Nutation"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AscendantDegreesToARMC(cls, ascendant, obliquityOfEcliptic, geographicLatitude, time):
        """
         This method is used to convert the tropical ascendant to the ARMC Ascendant Right Meridian Circle. It first calculates the right ascension and declination using the provided tropical ascendant and obliquity of the ecliptic. Then it calculates the oblique ascension by subtracting a value derived from the declination and geographic latitude from the right ascension. Finally it calculates the ARMC based on the value of the tropical ascendant and the oblique ascension. 
        :return: Double
         """
        endpoint = "AscendantDegreesToARMC"
        params = {
            "ascendant": ascendant,
            "obliquityOfEcliptic": obliquityOfEcliptic,
            "geographicLatitude": geographicLatitude,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AyanamsaDegree(cls, time):
        """
         The distance between the Hindu First Point and the Vernal Equinox measured at an epoch is known as the Ayanamsa in Varahamihiras time the summer solistice coincided with the first degree of Cancer and the winter solistice with the first degree of Capricorn whereas at one time the summer solistice coincided with the middle of the Aslesha 
        :return: Angle
         """
        endpoint = "AyanamsaDegree"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSayanaLongitude(cls, planetName, time):
        """
         Get fixed longitude used in western systems connects SwissEph Library with VedAstro NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        endpoint = "PlanetSayanaLongitude"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNirayanaLongitude(cls, planetName, time):
        """
         Planet longitude that has been corrected with Ayanamsa Gets planet longitude used vedic astrology Nirayana Longitude Sayana Longitude corrected to Ayanamsa Number from 0 to 360 represent the degrees in the zodiac as viewed from earth Note Since Nirayana is corrected in actuality 0 degrees will start at Taurus not Aries 
        :return: Angle
         """
        endpoint = "PlanetNirayanaLongitude"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextLunarEclipse(cls, time):
        """
         find time of next lunar eclipse UTC time 
        :return: DateTime
         """
        endpoint = "NextLunarEclipse"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextSolarEclipse(cls, time):
        """
         finds the next solar eclipse globally UTC time 
        :return: DateTime
         """
        endpoint = "NextSolarEclipse"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetEphemerisLongitude(cls, planetName, time):
        """
         Get fixed longitude used in western systems aka Sayana longitude NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        endpoint = "PlanetEphemerisLongitude"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSayanaLatitude(cls, planetName, time):
        """
         Gets Swiss Ephemeris longitude for a planet 
        :return: Angle
         """
        endpoint = "PlanetSayanaLatitude"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSpeed(cls, planetName, time):
        """
         Speed of planet from Swiss eph 
        :return: Double
         """
        endpoint = "PlanetSpeed"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ConstellationAtLongitude(cls, planetLongitude):
        """
         Converts Planet Longitude to Constellation equivelant Gets info about the constellation at a given longitude ie. Constellation Name Quarter Degrees in constellation etc. 
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
         Converts Planet Longitude to Zodiac Sign equivalent 
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
         Converts Zodiac Sign to Planet Longitude equivalent 
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
         Get Vedic Day Of Week The Hindu day begins with sunrise and continues till next sunrise.The first hora on any day will be the first hour after sunrise and the last hora the hour before sunrise the next day. 
        :return: DayOfWeek
         """
        endpoint = "DayOfWeek"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LordOfHoraFromWeekday(cls, hora, day):
        """
         Gets hora lord based on hora number week day 
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
         Each day starts at sunrise and ends at next days sunrise. This period is divided into 24 equal parts and they are called horas. A hora is almost equal to an hour. These horas are ruled by different planets. The lords of hora come in the order of decreasing speed with respect to earth Saturn Jupiter Mars Sun Venus Mercury and Moon. After Moon we go back to Saturn and repeat the 7 planets. 
        :return: PlanetName
         """
        endpoint = "LordOfHoraFromTime"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseJunctionPoint(cls, previousHouse, nextHouse):
        """
         Gets the junction point sandhi between 2 consecutive houses where one house begins and the other ends. 
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
         Gets planet which is the lord of a given sign 
        :return: PlanetName
         """
        endpoint = "LordOfZodiacSign"
        params = {
            "ZodiacName": signName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ZodiacSignsOwnedByPlanet(cls, planetName):
        """
         Given a planet name will return list of signs that the planet rules 
        :return: List`1
         """
        endpoint = "ZodiacSignsOwnedByPlanet"
        params = {
            "PlanetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextZodiacSign(cls, inputSign):
        """
         Gets next zodiac sign after input sign 
        :return: ZodiacName
         """
        endpoint = "NextZodiacSign"
        params = {
            "ZodiacName": inputSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NextHouseNumber(cls, inputHouseNumber):
        """
         Gets next house number after input house number goes to 1 after 12 
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
         Gets the exact longitude where planet is ExaltedExaltation Exaltation Each planet is held to be exalted when it is in a particular sign. The power to do good when in exaltation is greater than when in its own sign. Throughout the sign ascribed the planet is exalted but in a particular degree its exaltation is at the maximum level. NOTE For Upagrahas no exact degree for exaltation the whole sign is counted as such exalatiotn set at degree 1 Rahu ketu have exaltation points ref Astroloy for Beginners pg. 12 
        :return: ZodiacSign
         """
        endpoint = "PlanetExaltationPoint"
        params = {
            "PlanetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDebilitationPoint(cls, planetName):
        """
         Gets the exact sign longitude where planet is DebilitatedDebility TODO method needs testing Note Rahu ketu have debilitation points ref Astroloy for Beginners pg. 12 planet to sign relationship is the whole sign this is just a point The 7th house or the 180th degree from the place of exaltation is the place of debilitation or fall. The Sun is debilitated in the 10th degree of Libra the Moon 3rd of Scorpio and so on. For Upagrahas no exact degree for exaltation the whole sign is counted as such exalatiotn set at degree 1 The debilitation or depression points are found by adding 180 to the maximum points given above. While in a state of fall planets give results contrary to those when in exaltation. ref Astroloy for Beginners pg. 11 
        :return: ZodiacSign
         """
        endpoint = "PlanetDebilitationPoint"
        params = {
            "PlanetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEvenSign(cls, planetSignName):
        """
         Returns true if zodiac sign is an Even sign Yugma Rasis 
        :return: Boolean
         """
        endpoint = "IsEvenSign"
        params = {
            "ZodiacName": planetSignName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsOddSign(cls, planetSignName):
        """
         Returns true if zodiac sign is an Odd sign Oja Rasis 
        :return: Boolean
         """
        endpoint = "IsOddSign"
        params = {
            "ZodiacName": planetSignName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsFixedSign(cls, sunSign):
        """
         Fixed signs Taurus Leo Scropio Aquarius. 
        :return: Boolean
         """
        endpoint = "IsFixedSign"
        params = {
            "ZodiacName": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMovableSign(cls, sunSign):
        """
         Movable signs Aries Cancer Libra Capricorn. 
        :return: Boolean
         """
        endpoint = "IsMovableSign"
        params = {
            "ZodiacName": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsCommonSign(cls, sunSign):
        """
         Common signs Gemini Virgo Sagitarius Pisces. 
        :return: Boolean
         """
        endpoint = "IsCommonSign"
        params = {
            "ZodiacName": sunSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPermanentRelationshipWithPlanet(cls, mainPlanet, secondaryPlanet):
        """
         Gets a planets permenant relationship. Based on Hindu Predictive Astrology pg. 21 Note Rahu Ketu are not mentioned in any permenant relatioship by Raman. But some websites do mention this. As such Ramans take is taken as final. Since theres so far no explanation by Raman on Rahu Ketu permenant relation it is assumed that such relationship is not needed and to make them up for conveniece sake could result in wrong prediction down the line. But temporary relationship are mentioned by Raman for Rahu Ketu so explicitly use Temperary relationship where needed. 
        :return: PlanetToPlanetRelationship
         """
        endpoint = "PlanetPermanentRelationshipWithPlanet"
        params = {
            "PlanetName": mainPlanet.value,
            "PlanetName": secondaryPlanet.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ConvertJulianTimeToNormalTime(cls, julianTime):
        """
         Converts julian time to normal time normal time can be lmt lat utc 
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
         Gets Greenwich time in normal format from Julian days at Greenwich Note Inputed time is Julian days at greenwich callers reponsibility to make sure 
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
         Gets Local mean time LMT at Greenwich UTC in Julian days based on the inputed time 
        :return: Double
         """
        endpoint = "GreenwichLmtInJulianDays"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LmtToUtc(cls, time):
        """
         Converts Local Mean Time LMT to Universal Time UTC 
        :return: DateTimeOffset
         """
        endpoint = "LmtToUtc"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planet.value,
            "ZodiacName": signToCheck.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": mainAshtakvargaPlanet.value,
            "PlanetName": planetToCheck.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": currentTime.geolocation.location_name,
            "Time": currentTime.url_time_string(),
            "PlanetName": planet.value,
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
            "PlanetName": planet.value,
            "gocharaHouse": gocharaHouse,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": currentTime.geolocation.location_name,
            "Time": currentTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": currentTime.geolocation.location_name,
            "Time": currentTime.url_time_string(),
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
            "PlanetName": planet.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
            "PlanetName": planet.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": nowTime.geolocation.location_name,
            "Time": nowTime.url_time_string(),
            "PlanetName": planet.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "levels": levels,
            "precisionHours": precisionHours,
            "scanYears": scanYears,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtRange(cls, birthTime, startTime, endTime, levels, precisionHours):
        """
         Calculates dasa for a specific time frame 
        :return: JObject
         """
        endpoint = "DasaAtRange"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": startTime.geolocation.location_name,
            "Time": startTime.url_time_string(),
            "Location": endTime.geolocation.location_name,
            "Time": endTime.url_time_string(),
            "levels": levels,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtTime(cls, birthTime, checkTime, levels):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "DasaAtTime"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "Location": checkTime.geolocation.location_name,
            "Time": checkTime.url_time_string(),
            "levels": levels,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaForNow(cls, birthTime, levels):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "DasaForNow"
        params = {
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "levels": levels,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMercuryAfflicted(cls, time):
        """
         Whenever an affiiction by way of a malefic occupying a certain house or joining with a certain planet is suggested by implication an aspect is also meant though an affliction caused by aspect.is comparatively less malevolent Note TODO presently not 100 sure if what is meant by affliction is solely only limited to aspects conjunction with bad planets. Or Located in enemy sign an affliction Low shadbala an affliction Low drikbala an affliction At present malefic aspects conjunctions are used becasue it seems based on texts that this is correct. But it seems mercury in enemny sign or position in a house should also play a role. There must be a corelation between shadbala or drikbala to aspects conjucntion A more precise way of mesurement it could be via the bala method. Needs testing for sure to find out what bala values determine an afflicted mercury 
        :return: Boolean
         """
        endpoint = "IsMercuryAfflicted"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMercuryMalefic(cls, time):
        """
         Check if Mercury is malefic true returns false if benefic References Mercury by nature is called sournya or good. And if he is in conjunction with the Sun Saturn Mars Rahu or Ketu he will be a malefic. His conjunction with beneficial planets like Full Moon Jupiter or Venus will classify him as a benefic. Benefic means a good and malefic means an evil planet. TODO Does malefic moon make it malefic atm malefic moon makes it malefic Though in the earlier pages Mercury is defined either as a subba benefic or papa malefic according to its association is with a benefic or malefic Mercury for purposes of calculating Drisbtibala of Bbavas is to be deemed as a full benefic. This is in accord with the injunctions of classical writers Gurugnabbyam tu yuktasya poomamekam tu yojayet. 11. Benefics and Malefics. Among these Srya ani Mangal decreasing Candr Rahu and Ketu the ascending and the descending nodes of Candr are malefics while the rest are benefics. Budh however is a malefic if he joins a malefic. Note ATM malefic planets override benefic TODO not sure if malefic planet overrides benefic if both are conjunct 
        :return: Boolean
         """
        endpoint = "IsMercuryMalefic"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsMoonBenefic(cls, time):
        """
         Moon is a benefic from the 8th day of the bright half of the lunar month to the 8th day of the dark half of the lunar month and a malefic in the rest of the days. Returns true if benefic false if malefic 
        :return: Boolean
         """
        endpoint = "IsMoonBenefic"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetBenefic(cls, planetName, time):
        """
         Checks if a given planet is benefic 
        :return: Boolean
         """
        endpoint = "IsPlanetBenefic"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetList(cls, time):
        """
         Gets all planets that are benefics at a given time since moon mercury changes Benefics on the other hand tend to do good but sometimes they also become capable of doing harm. 
        :return: List`1
         """
        endpoint = "BeneficPlanetList"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMalefic(cls, planetName, time):
        """
         Checks if a given planet is Malefic 
        :return: Boolean
         """
        endpoint = "IsPlanetMalefic"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetList(cls, time):
        """
         Gets list of permanent malefic planets for moon mercury it is based on changing factors Malefics are always inclined to do harm but under certain conditions the intensity of the mischief is tempered. 
        :return: List`1
         """
        endpoint = "MaleficPlanetList"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInAspect(cls, inputPlanet, time):
        """
         Gets all planets the inputed planet is transmitting aspect to 
        :return: List`1
         """
        endpoint = "PlanetsInAspect"
        params = {
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAspectDegree(cls, receiver, trasmitter, time):
        """
         Calculate aspect angle between 2 planets 
        :return: Double
         """
        endpoint = "PlanetAspectDegree"
        params = {
            "PlanetName": receiver.value,
            "PlanetName": trasmitter.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsAspectingPlanet(cls, receivingAspect, time):
        """
         Gets all planets the transmitting aspect to inputed planet 
        :return: List`1
         """
        endpoint = "PlanetsAspectingPlanet"
        params = {
            "PlanetName": receivingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HousesInAspect(cls, planet, time):
        """
         Gets houses aspected by the inputed planet 
        :return: List`1
         """
        endpoint = "HousesInAspect"
        params = {
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsAspectingHouse(cls, inputHouse, time):
        """
         Gets all planets aspecting inputed house 
        :return: List`1
         """
        endpoint = "PlanetsAspectingHouse"
        params = {
            "HouseName": inputHouse.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByPlanet(cls, receiveingAspect, transmitingAspect, time):
        """
         Checks if the a planet is aspected by another planet 
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByPlanet"
        params = {
            "PlanetName": receiveingAspect.value,
            "PlanetName": transmitingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseAspectedByPlanet(cls, receiveingAspect, transmitingAspect, time):
        """
         Checks if a house is aspected by a planet 
        :return: Boolean
         """
        endpoint = "IsHouseAspectedByPlanet"
        params = {
            "HouseName": receiveingAspect.value,
            "PlanetName": transmitingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithPlanet(cls, planetA, planetB, time):
        """
         Checks if the a planet is conjunct with another planet Based on longitudes Note Both planets A B are checked if they are in conjunct with each other performance might be effected mildly but errors in conjunction calculation would be caught here. Can be removed once conjunction calculator is confirmed accurate. 
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithPlanet"
        params = {
            "PlanetName": planetA.value,
            "PlanetName": planetB.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetConjunctWithBeneficPlanets(cls, inputPlanet, time):
        """
         Check if benefic planets are conjunct with specified planet 
        :return: Boolean
         """
        endpoint = "IsPlanetConjunctWithBeneficPlanets"
        params = {
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPowerPercentage(cls, inputPlanet, time):
        """
         convert the planets strength into a value over hundred with max min set by strongest weakest planet 
        :return: Double
         """
        endpoint = "PlanetPowerPercentage"
        params = {
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PickOutStrongestPlanet(cls, relatedPlanets, birthTime):
        """
         Given a list of planets will pick out the strongest planet based on Shadbala 
        :return: PlanetName
         """
        endpoint = "PickOutStrongestPlanet"
        params = {
            "relatedPlanets": relatedPlanets,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetOrderedByStrength(cls, time):
        """
         Returns an array of all planets sorted by strenght 0 index being strongest to 8 index being weakest Note Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. 
        :return: List`1
         """
        endpoint = "AllPlanetOrderedByStrength"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetStrongInShadbala(cls, planet, time):
        """
         Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. Powerful Planets.Ravi is befd to be powerful when his Shadbala Pinda is 5 or more rupas. Chandra becomes strong when his Shadbala Pinda is 6 or more rupas. Kuja becomes powerful when bis Shadbala Pinda does not fall short of 5 rupas.Budha becomes potent by having his Sbadbala Pinda as 7 rupas Guru Sukra and Sani become thoroughly powerful if their Shadbala Pindas are 6.5 5.5 and 5 rupas or more respectively. 
        :return: Boolean
         """
        endpoint = "IsPlanetStrongInShadbala"
        params = {
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsHouseBeneficInShadbala(cls, house, birthTime, threshold):
        """
         sets benefic if above 450 score 
        :return: Boolean
         """
        endpoint = "IsHouseBeneficInShadbala"
        params = {
            "HouseName": house.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllPlanetStrength(cls, time):
        """
         Gets strength shadbala of all 9 planets 
        :return: List`1
         """
        endpoint = "AllPlanetStrength"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AllHousesOrderedByStrength(cls, time):
        """
         Returns an array of all houses sorted by strength 0 index being strongest to 11 index being weakest 
        :return: HouseName[]
         """
        endpoint = "AllHousesOrderedByStrength"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetShadbalaPinda(cls, planetName, time):
        """
         THE FINAL TOTAL STRENGTH Shadbala the six sources of strength and weakness the planets The importance of and the part played by the Shadbalas in the science of horoscopy are manifold In order to obtain the total strength of the Shadbala Pinda of each planet we have to add together its Sthana Bala Dik Bala Kala Bala. Chesta Bala and Naisargika Bala. And the Grahas Drik Bala must be added to or subtracted from the above sum according as it is positive or negative. The result obtained is the Shadbala Pinda of the planet in Shashtiamsas. Note Rahu Ketu supported via house lord 
        :return: Shashtiamsa
         """
        endpoint = "PlanetShadbalaPinda"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetStrength(cls, planetName, time):
        """
         get total combined strength of the inputed planet input birth time to get strength in horoscope note an alias method to GetPlanetShadbalaPinda strength is easier to remember 
        :return: Shashtiamsa
         """
        endpoint = "PlanetStrength"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDrikBala(cls, planetName, time):
        """
         Aspect strength This strength is gained by the virtue of the aspect Graha Dristi of different planets on other planet. The aspect of benefics is considered to be strength and the aspect of malefics is considered to be weaknesses. Drik Bala.This means aspect strength. The Drik Bala of a Gqaha is onefourth of the Drishti Pinda on it. It is positive or negative according as the Drishti Pinda is positive or negative. See the formula given on page 85. There is special aspect for Jupiter Mars and Saturn on the 5th and 9th 4th and 8th and 3rd and 10th signs respectively. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetDrikBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindViseshaDrishti(cls, dk, p):
        """
         Get special aspect if any of Kuja Guru and Sani 
        :return: Double
         """
        endpoint = "FindViseshaDrishti"
        params = {
            "dk": dk,
            "PlanetName": p.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindDrishtiValue(cls, dk):
        """
        Empty sample text
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
         Nalsargika Bala.This is the natural strength that each Graha possesses. The value assigned to each depends upon its luminosity. Ravi the brightest of all planets has the greatest Naisargika strength while Sani the darkest has the least Naisargika Bala. This is the natural or inherent strength of a planet. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetNaisargikaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetChestaBala(cls, planetName, time, useSpecialSunMoon):
        """
         NOTE sun moon get score for ISHTAKESHA calculation only when specified for IshataKashta MOTIONAL STRENGTH Chesta here means Vakra Chesta or act of retrogression. Each planet except the Sun and the Moon and shadowy planets get into the state of Vakra or retrogression when its distance from the Sun exceeds a particular limit. And the strength or potency due to the planet on account of the arc of the retrogression is termed as Chesta Bala Deduct from the Seeghrocbcha half the sum of the True and Mean Longitudes of planets and divide the difference by 3. The quotient is the Chestabala. Max 60 meaning RetrogradeVakra When the distance of any one planet from the Sun exceeds a particular limit it becomes retrograde i.e. when the planet goes from perihelion the point in a planets orbit nearest to the Sun to aphelion the part of a planets oroit most distant from the Sun as it recedes from the Sun it gradually loses the power of the Suns gravitation and consequently 
        :return: Shashtiamsa
         """
        endpoint = "PlanetChestaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
            "useSpecialSunMoon": useSpecialSunMoon,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SunChestaBala(cls, inputTime):
        """
         special function to get chesta score for IshtaKashta score Bala book pg. 108 Sun has no Chesta kendra or Chesta bala as he never gets into retrogression. But still a method is prescribed to find his Chesla Bala which is necessary to ascertain the lshta and Kashta Phalas. 
        :return: Shashtiamsa
         """
        endpoint = "SunChestaBala"
        params = {
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MoonChestaBala(cls, inputTime):
        """
         special function to get chesta score for IshtaKashta score Bala book pg. 108 
        :return: Shashtiamsa
         """
        endpoint = "MoonChestaBala"
        params = {
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Madhya(cls, epochToBirthDays, time1):
        """
         The mean position of a planet is the position which it would have attained at a uniform rate of motion and the corrections to be applied in respect of the eccentricity of the orbit are not considered 
        :return: Dictionary`2
         """
        endpoint = "Madhya"
        params = {
            "epochToBirthDays": epochToBirthDays,
            "Location": time1.geolocation.location_name,
            "Time": time1.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EpochInterval(cls, time1):
        """
         Get interval from the epoch to the birth date in days The result represents the interval from the epoch to the birth date. 
        :return: Double
         """
        endpoint = "EpochInterval"
        params = {
            "Location": time1.geolocation.location_name,
            "Time": time1.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetMotionName(cls, planetName, time):
        """
         Gets the planets motion name can be Retrograde Direct Stationary a name version of Chesta Bala 
        :return: PlanetMotion
         """
        endpoint = "PlanetMotionName"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetRetrograde(cls, planetName, time):
        """
         A retrograde planet moves in the reverse direction and instead of increasing its longitude decreases as the time elapses. Rahu and Ketu often move in retrograde direction only. Other planets except the Sun and the Moon are subject to retrogression from time to time. 
        :return: Boolean
         """
        endpoint = "IsPlanetRetrograde"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetCombust(cls, planetName, time):
        """
         Determines if a given planet is combust at a specific time. Combustion of planets Planets when too close to the Sun become invisible and are labelled as combust. A combust planet loses its strength and tends to behave adversely according to predictive astrology. Aryabhata has the following to say about combustion When the Moon has no latitude i.e. when it is at zero degree of latitude it is visible when situated at a distance of 12 degrees from the Sun. Venus is visible when 9 degrees distant from the Sun. The other planets taken in the order of decreasing sizes viz. Jupiter Mercury Saturn and Mars are visible when they are 9 degrees increased by twos i.e. when they are 11 13 15 and 17 degrees distant from the Sun. The degrees as mentioned above are generally taken as the limits within which the respective planets are said to be combust. 
        :return: Boolean
         """
        endpoint = "IsPlanetCombust"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetCirculationTime(cls, planetName):
        """
         circulation time of the objects in years used by cheshta bala calculation 
        :return: Double
         """
        endpoint = "PlanetCirculationTime"
        params = {
            "PlanetName": planetName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSaptavargajaBala(cls, planetName, time):
        """
         Sapthavargajabala This is the strength of a planet due to its residence in the seven subdivisions according to its relation with the dispositor. Saptavargaja bala means the strength a planet gets by virtue of its disposition in a friendly neutral or inimical Rasi Hora Drekkana Sapthamsa Navamsa Dwadasamsa and Thrimsamsa. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetSaptavargajaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSthanaBala(cls, planetName, time):
        """
         residence of the planet and as such a certain degree of strength or weakness attends on it Positonal strength A planet occupies a certain sign in a Rasi and friendly neutrai or inimical varga. It is either exalted or debilitated lt ocupies its Moolathrikona or it has its own varga. All these states refer to the position or residence of the planet and as such a certain degree of strength or weakness attends on it. This strength or potency is known as the Sthanabala. 1.Uccha Bala Uccha means exaltation. When a planet is placed in its highest exaltation point it is of full strength and when it is in its deepest debilitation point it is devoid of any strength. When in between the strength is calculated proportionately dependent on the distance these planets are placed from the highest exaltation or deepest debilitation point. 2.Sapta Vargiya Bala Rashi Hora Drekkana Saptamsha Navamsha Dwadasamsha and Trimsamsha constitute the Sapta Varga. The strength of the planets in these seven divisional charts based on their placements in Mulatrikona own sign friendly sign etc. constitute the Sapta vargiya bala. 3.OjaYugma RashiAmsha Bala Oja means odd signs and Yugma means even signs. Thus as the name imply this strength is derived from a planets placement in the odd or even signs in the Rashi and Navamsha. 4.Kendradi Bala The name itself implies how to compute this strength. A planet in a Kendra 14710 gets full strength while one in Panapara 25811 gets half and the one in Apoklimas 12369 gets quarter strength. 5.Drekkana Bala Due to placement in first second or third Drekkana of a sign male female and hermaphrodite planets respectively get a quarter strength according to placements in the first second and third Drekkana. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetSthanaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDrekkanaBala(cls, planetName, time):
        """
         Drekkanabala The Sun Jupiter and Mars in the lst Saturn and Mercury in the 2nd and the Moon and Venus in the last Drekkana get full strength of 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetDrekkanaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKendraBala(cls, planetName, time):
        """
         Kendrtzbala Planets in Kendras get 60 shashtiamsas in Panapara 30 and in Apoklima 15. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetKendraBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetOjayugmarasyamsaBala(cls, planetName, time):
        """
         Ojayugmarasyamsa In odd Rasi and Navamsa the Sun Mars Jupiter Mercury and Saturn get strength and the rest in even signs 
        :return: Shashtiamsa
         """
        endpoint = "PlanetOjayugmarasyamsaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetKalaBala(cls, planetName, time):
        """
         Gets a planets Kala Bala or Temporal strength 
        :return: Shashtiamsa
         """
        endpoint = "PlanetKalaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetYuddhaBala(cls, inputedPlanet, preKalaBalaValues, time):
        """
         Two planets are said to be in Yuddha or fight when they are in conjunction and the distance between them is less than one degree. TODO Not fully tested Yuddhabala All planets excepting the Sun and the Moon enter into war when two planets are in the same degree. The pJanet having the lesser longitude is the winner. Find out the sum total of the SthanabaJa Kalabala and Digbala of these two planets. Difference between the two divided by the difference of their diameters of its disc gives the Yuddhabala. Add this to the victorious planet and dedu_ct it from the vanquished. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetYuddhaBala"
        params = {
            "PlanetName": inputedPlanet.value,
            "preKalaBalaValues": preKalaBalaValues,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAyanaBala(cls, planetName, time):
        """
         Ayanabala All planets get 30 shasbtiamsas at the equator. For the Sun Jupiter Mars and Venus add proportionately when they are in northern course and for the Moon and Saturn when in southern course. Deduct proportionately when they are in the opposite direction. Unit of strength is 60 shashtiamsas. TODO some values for calculation with standard hooscope out of whack it seems small differences in longitude seem magnified at final value not 100 sure need further testing for confirmation but final values seem ok so far 
        :return: Shashtiamsa
         """
        endpoint = "PlanetAyanaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDeclination(cls, planetName, time):
        """
         A heavenly body moves northwards the equator for sometime and then gets southwards. This angular distance from the equinoctial or celestial equator is Kranti or the declination. Declinations are reckoned plus or minus according as the planet is situated in the northern or southern celestial hemisphere 
        :return: Double
         """
        endpoint = "PlanetDeclination"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def EclipticObliquity(cls, time):
        """
         true obliquity of the Ecliptic includes nutation 
        :return: Double
         """
        endpoint = "EclipticObliquity"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetHoraBala(cls, planetName, time):
        """
         Hora Bala AKA Horadhipathi Bala 
        :return: Shashtiamsa
         """
        endpoint = "PlanetHoraBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetAbdaBala(cls, planetName, time):
        """
         The planet who is the king of the year of birth is assigned a value of 15 Shashtiamsas as his Abdabala. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetAbdaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetMasaBala(cls, planetName, time):
        """
         Gets a planets masa bala the lord of the month of birth is assigned a value of 30 Shashtiamsas as his Masabala 
        :return: Shashtiamsa
         """
        endpoint = "PlanetMasaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetVaraBala(cls, planetName, time):
        """
        Empty sample text
        :return: Shashtiamsa
         """
        endpoint = "PlanetVaraBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def YearAndMonthLord(cls, time):
        """
         Gets year month lord at inputed time 
        :return: Object
         """
        endpoint = "YearAndMonthLord"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetTribhagaBala(cls, planetName, time):
        """
         Thribhagabala Mercury the Sun and Saturn get 60 shashtiamsas each during the lst 2nd and 3rd onethird positions of the day respectively. The Moon Venus and Mars govern the lst 2nd and 3rd onethird portion of the night respectively. Jupiter is always strong and gets 60 shashtiamsas of strength. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetTribhagaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetOchchaBala(cls, planetName, time):
        """
         Oochchabala The distance between the planets longitude and its debilitation point divided by 3 gives its exaltation strength or oochchabaJa. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetOchchaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetPakshaBala(cls, planetName, time):
        """
         Pakshabala When the Moon is waxing take the distance from the Sun to the Moon and divide it by 3. The quotient is the Pakshabala. When the Moon is waning take the distance from the Moon to the Sun and divide it by 3 for assessing Pakshabala. Moon Jupiter Venus and Mercury are strong in Sukla Paksha and the others in Krishna Paksha. Note Mercury is benefic or malefic based on planets conjunct with it 
        :return: Shashtiamsa
         """
        endpoint = "PlanetPakshaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetNathonnathaBala(cls, planetName, time):
        """
         Nathonnathabala Midnight to midday the Sun Jupiter and Venus gain strength proportionately till they get maximum at zenith. The other planets except Mercury. are gaining strength from midday to midnight proportionately. In the same way Mercury is always strong and gets 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetNathonnathaBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetDigBala(cls, planetName, time):
        """
         Gets Dig Bala of a planet. Jupiter and Mercury are strong in Lagna Ascendant the Sun and Mars in the 10th Saturn in the 7th and the Moon and Venus in the 4th. The opposite houses are weak points. Divide the distance between the longitude of the planet and its depression point by 3. Quotient is the strength. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetDigBala"
        params = {
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HouseStrength(cls, inputHouse, time):
        """
         Bhava Bala.Bhava means house and Bala means strength. Bhava Bala is the potency or strength of the house or bhava or signification. We have already seen that there are 12 bhavas which comprehend all human events. Each bhava signifies or indicates certain events or functions. For instance the first bhava represents Thanu or body the appearance of the individual his complexion his disposition his stature etc. If it attains certain strength the native will enjoy the indications of the bhava fully otherwise he will not sufficiently enjoy them. The strength of a bhava is composed of three factors viz. 1 Bhavadhipathi Bala 2 Bhava Digbala 3 Bhava Drishti Bala. 
        :return: Shashtiamsa
         """
        endpoint = "HouseStrength"
        params = {
            "HouseName": inputHouse.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaDrishtiBala(cls, time):
        """
         House received aspect strength Bhavadrishti Bala.Each bhava in a horoscope remains aspected by certain planets. Sometimes the aspect cast on a bhava will be positive and sometimes it will be negative according as it is aspected by benefics or malefics. For all 12 houses 
        :return: HouseSubStrength
         """
        endpoint = "BhavaDrishtiBala"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaDigBala(cls, time):
        """
         House strength from different types of signs Bhava Digbala.This is the strength acquired by the different bhavas falling in the different groups or types of signs. For all 12 houses 
        :return: HouseSubStrength
         """
        endpoint = "BhavaDigBala"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BhavaAdhipathiBala(cls, time):
        """
         Bhavadhipatbi Bala This is the potency of the lord of the bhava. For all 12 houses 
        :return: HouseSubStrength
         """
        endpoint = "BhavaAdhipathiBala"
        params = {
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetListByShadbala(cls, personBirthTime, threshold):
        """
         0 index is strongest 
        :return: List`1
         """
        endpoint = "BeneficPlanetListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficPlanetListByShadbala(cls, personBirthTime):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "BeneficPlanetListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficHouseListByShadbala(cls, personBirthTime, threshold):
        """
         0 index is strongest 
        :return: List`1
         """
        endpoint = "BeneficHouseListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def BeneficHouseListByShadbala(cls, personBirthTime):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "BeneficHouseListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListByShadbala(cls, personBirthTime, threshold):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "MaleficPlanetListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficPlanetListByShadbala(cls, personBirthTime):
        """
         0 index is most malefic 
        :return: List`1
         """
        endpoint = "MaleficPlanetListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficHouseListByShadbala(cls, personBirthTime, threshold):
        """
         0 index is most malefic 
        :return: List`1
         """
        endpoint = "MaleficHouseListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MaleficHouseListByShadbala(cls, personBirthTime):
        """
        Empty sample text
        :return: List`1
         """
        endpoint = "MaleficHouseListByShadbala"
        params = {
            "Location": personBirthTime.geolocation.location_name,
            "Time": personBirthTime.url_time_string(),
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
            "HouseName": house.value,
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
            "ZodiacName": zodiacName.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetPlanetTags(cls, planetList):
        """
        Empty sample text
        :return: String
         """
        endpoint = "GetPlanetTags"
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
            "PlanetName": lordOfHouse.value,
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
            "HouseName": houseNumber.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetDasaInfoForAscendant(cls, ascendantName):
        """
         Get general planetary info for persons dasa hardcoded table It is intended to be used to interpret dasa predictions as such should be displayed next to dasa chart. This method is direct translation from the book. Similar to method GetPlanetDasaNature Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology 
        :return: String
         """
        endpoint = "GetDasaInfoForAscendant"
        params = {
            "ZodiacName": ascendantName.value,
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
            "ZodiacName": inputSign.value,
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": zodiacName.value,
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetsInHouse(cls, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "PlanetsInHouse"
        params = {
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": signName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": inputSign.value,
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
            "PlanetName": startPlanet.value,
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "Location": inputTime.geolocation.location_name,
            "Time": inputTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "ZodiacName": signInput.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "ZodiacName": zodiacSignName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": mainPlanet.value,
            "PlanetName": secondaryPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": house.value,
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": mainPlanet.value,
            "PlanetName": secondaryPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": signName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": receivingAspect.value,
            "PlanetName": transmitingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": receivingAspect.value,
            "PlanetName": transmitingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSthanaBalaNeutralPoint(cls, planet):
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        endpoint = "PlanetSthanaBalaNeutralPoint"
        params = {
            "PlanetName": planet.value,
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": kendraFrom.value,
            "PlanetName": kendraTo.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": startPlanet.value,
            "PlanetName": endPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": lordHouse.value,
            "HouseName": occupiedHouse.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": lordHouse.value,
            "HouseName": occupiedHouse.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": sign.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": sign.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": sign.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": sign.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": house.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": house.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetAspectedByMaleficPlanets(cls, planetReceivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectedByMaleficPlanets"
        params = {
            "PlanetName": planetReceivingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAllMaleficPlanetsAspecting(cls, planetReceivingAspect, time):
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        endpoint = "GetAllMaleficPlanetsAspecting"
        params = {
            "PlanetName": planetReceivingAspect.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": lord.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": startSign.value,
            "ZodiacName": endSign.value,
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
    def IsPlanetInHouse(cls, planet, houseNumber, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetInHouse"
        params = {
            "PlanetName": planet.value,
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": house.value,
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "HouseName": houseNumber.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "ZodiacName": moonSign.value,
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
            "ZodiacName": moonSign.value,
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
            "ZodiacName": moonSign.value,
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
            "ZodiacName": moonSign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetBeneficToLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetBeneficToLagna"
        params = {
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetMaleficToLagna(cls, planetName, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetMaleficToLagna"
        params = {
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": planetName.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": startPlanet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": startPlanet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "PlanetName": startPlanet.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
            "PlanetName": startPlanet.value,
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": startPlanet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "PlanetName": startPlanet.value,
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "PlanetName": inputPlanet.value,
            "Location": time.geolocation.location_name,
            "Time": time.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
            "Location": birthTime.geolocation.location_name,
            "Time": birthTime.url_time_string(),
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
