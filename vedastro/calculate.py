# AUTO GENERATED ON 13:25 16/06/2026 +08:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any
import requests
import json
from enum import Enum


class Calculate:
    api_key = None
    base_url = "https://api.vedastro.org/api/Calculate"

    @classmethod
    def SetAPIKey(cls, api_key):
        cls.api_key = api_key

    @classmethod
    def _make_request(cls, endpoint, params):
        url = f"{cls.base_url}/{endpoint}"
        if cls.api_key:
            params["APIKey"] = cls.api_key
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
    def FindBirthTimeByAnimal(cls, possibleBirthTime, precisionHours=1):
        """
         Builds a list of possible birth times for the given day by checking the animal prediction associated with each time slice. For every generated time slice the method calculates the Moons constellation derives the corresponding Yoni Kuta animal stores the result as a keyvalue pair where the key is the time slice and the value is the predicted animal. This is useful when narrowing down a birth time based on an expected or known animal association from constellationbased matching. 
        :return: JObject
         """
        endpoint = "FindBirthTimeByAnimal"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByRisingSign(cls, possibleBirthTime, precisionHours=1):
        """
         Builds a list of possible birth times for the given day by checking the rising sign Lagna prediction for each time slice. For every generated time slice the method calculates horoscope predictions using the RisingSign event tag selects the first matching prediction stores the result in a JSON object keyed by the time slice. This helps narrow down a possible birth time when the expected rising sign is already known or suspected. 
        :return: JObject
         """
        endpoint = "FindBirthTimeByRisingSign"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeHouseStrengthPerson(cls, possibleBirthTime, precisionHours=1):
        """
         Builds a birthtime comparison table by calculating the strength of every house for each time slice on the selected day. For every generated time slice the method loops through all houses calculates each houses strength formats the strengths into a single readable string stores the final summary beside the corresponding time. This is useful for manually comparing how house strength changes across the day when trying to refine a birth time. 
        :return: JObject
         """
        endpoint = "FindBirthTimeHouseStrengthPerson"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetActiveNccBodyRulesAtTime(cls, birthTime, bodyHeight, bodyShape, hair, lips, nose, complexion, faceShape, constitution, personality):
        """
         Diagnostic returns the classical NCC body rules that fire at the given birth time each scored against the supplied body features. Intended for explain this prediction UI panels and for the multirule tester percelebrity ruledatabase accuracy. Empty body fields are skipped during matching no penalty. 
        :return: JArray
         """
        endpoint = "GetActiveNccBodyRulesAtTime"
        params = {
            "birthTime": birthTime.to_json(),
            "bodyHeight": bodyHeight,
            "bodyShape": bodyShape,
            "hair": hair,
            "lips": lips,
            "nose": nose,
            "complexion": complexion,
            "faceShape": faceShape,
            "constitution": constitution,
            "personality": personality,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByMachineLearning(cls, possibleBirthTime, bodyHeight, bodyShape, hair, lips, nose, complexion, faceShape, constitution, personality, precisionHours=0.041666666666666664, modelType="NCC"):
        """
        Empty sample text
        :return: TimeRange
         """
        endpoint = "FindBirthTimeByMachineLearning"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "bodyHeight": bodyHeight,
            "bodyShape": bodyShape,
            "hair": hair,
            "lips": lips,
            "nose": nose,
            "complexion": complexion,
            "faceShape": faceShape,
            "constitution": constitution,
            "personality": personality,
            "precisionHours": precisionHours,
            "modelType": modelType,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def FindBirthTimeByMachineLearningTopK(cls, possibleBirthTime, bodyHeight, bodyShape, hair, lips, nose, complexion, faceShape, constitution, personality, precisionHours=0.041666666666666664, modelType="NCC"):
        """
         Returns the topK most likely birthtime ranges using only the NCC bodyrule database. Every NccBodyRuleEntry is evaluated directly against every time slice. Rules such as SaturnInLagna MarsInLagna SunInPisces LagnaLordCombust LagnaInFierySign etc. are treated as firstclass predictors. Rising sign is NOT the master class it is emitted diagnostically only. 
        :return: JArray
         """
        endpoint = "FindBirthTimeByMachineLearningTopK"
        params = {
            "possibleBirthTime": possibleBirthTime.to_json(),
            "bodyHeight": bodyHeight,
            "bodyShape": bodyShape,
            "hair": hair,
            "lips": lips,
            "nose": nose,
            "complexion": complexion,
            "faceShape": faceShape,
            "constitution": constitution,
            "personality": personality,
            "precisionHours": precisionHours,
            "modelType": modelType,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ListAPICalls(cls, ):
        """
         Returns a JSON array containing the method signatures of all calculator methods exposed for APIstyle use. The method gathers calculator metadata extracts a signature for each method and returns the results in a simple list format. This is useful for inspection debugging tooling documentation or quick discovery of available API calls. 
        :return: JArray
         """
        endpoint = "ListAPICalls"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchCalculateMethods(cls, query, topK=5):
        """
         Naturallanguage semantic search over all Calculate methods. Returns topK compact matches with only methodName description and rounded score. Powered by Cosmos DB vector index built from Calculate.cs by StaticTableGenerator. 
        :return: Task`1
         """
        endpoint = "SearchCalculateMethods"
        params = {
            "query": query,
            "topK": topK,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchSourceText(cls, query, topK=5, sourceName=None, contextSize=600):
        """
         Naturallanguage semantic search over the classical Vedic astrology sourcetext knowledge base e.g. Hindu Predictive Astrology BPHS. Returns topK most relevant passages with sourceName pageNumber chunkIndex text and similarity score. Powered by the same DashScope embeddings Cosmos DB vector index used by ContextBasedAstrologyDatas RAG enrichment step. 
        :return: Task`1
         """
        endpoint = "SearchSourceText"
        params = {
            "query": query,
            "topK": topK,
            "sourceName": sourceName,
            "contextSize": contextSize,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAvailableSourceTexts(cls, ):
        """
         Returns a list of all available source text names in the knowledge base. Used by the frontend dropdown to dynamically show which classical texts are searchable. 
        :return: Task`1
         """
        endpoint = "GetAvailableSourceTexts"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchWebsitePages(cls, query, topK=5):
        """
         Naturallanguage semantic search over the curated VedAstro website pages Horoscope MatchChecker Numerology etc.. Returns topK matching pages with slug url title description and similarity score one row per distinct page chunks deduped by slug. Powered by DashScope embeddings the websiteknowledgekb Cosmos vector index built by StaticTableGenerator task 5. Replaces the old keywordscoring catalog in MCPApps search_website_pages. 
        :return: Task`1
         """
        endpoint = "SearchWebsitePages"
        params = {
            "query": query,
            "topK": topK,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ContextBasedAstrologyData(cls, query, birthTime=None, checkTime=None):
        """
        NO DESC FOUND!! ERROR
        :return: Task`1
         """
        endpoint = "ContextBasedAstrologyData"
        params = {
            "query": query,
            "birthTime": birthTime,
            "checkTime": checkTime,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AddressToGeoLocation(cls, address):
        """
         Converts a freeform address or location string into its corresponding geographic location. The method decodes the incoming address if it was URLencoded checks the cache first calls the location provider only when needed returns the resolved GeoLocation. This is typically used when a user supplies a city name place name or coordinatelike text and the system needs a normalized location object. 
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
         Searches for matching locations based on a partial or full address string and returns a list of possible results. This method is designed for location search or autocompletestyle behavior. It checks the cache first and then delegates the lookup to the configured location provider. 
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
         Converts latitude and longitude coordinates into a humanreadable geographic location. The method checks the cache first and then performs reverse geolocation using the configured location provider. 
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
         Resolves the timezone offset for a given geographic location at a specific moment in time. This method is designed to account for daylight saving time historical timezone changes locationspecific offset rules. It first checks the cache and then delegates the timezone lookup to the location provider. 
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
         Resolves a geographic location from an IP address. The method checks the cache first then calls the location provider to perform IPbased geolocation. 
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
         Gets the current standard time for a given location name. The method 1. decodes the input if it is URLencoded 2. resolves the location name into a GeoLocation 3. determines the current timezone offset for that location 4. converts the current UTC time into the local standard time 5. returns the result as a Time object tied to the resolved location. 
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
         Returns all events that are active at a specific moment based on a persons birth time and a selected set of event tags. This method effectively creates a singletime slice from the larger event chart and can be used to inspect what is happening at one exact moment. The method wraps the birth time inside a temporary Person object so that the event engine can use the existing eventcalculation pipeline. 
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
    def EventsAtRange(cls, birthTime, startTime, endTime, eventTagList, precisionHours=100):
        """
         Calculates all matching events that occur within a given time range. The method wraps the birth time in a temporary Person object and then runs the main event engine across the requested interval. 
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
         Returns the full event window for a specific event if that event is active at the supplied check time. The method 1. finds the event definition 2. checks whether the event is occurring at the requested moment 3. scans backward to find the start time 4. scans forward to find the end time 5. returns a completed Event object with timing and tags. If the event is not active at the requested time the method returns Event.Empty. 
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
         Finds the start time of an event by scanning backward from a time when the event is already known to be active. The method repeatedly steps into the past until the event is no longer occurring then returns the last confirmed time at which the event was still active. 
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
         Finds the end time of an event by scanning forward from a time when the event is already known to be active. The method repeatedly steps into the future until the event is no longer occurring then returns the last confirmed time at which the event was still active. 
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
    def SearchEvents(cls, birthTime, atTime, eventTagList):
        """
         Searches for all matching events that are active at a single moment in time. This is the snapshot form of event discovery it answers what is happening right now. 
        :return: List`1
         """
        endpoint = "SearchEvents"
        params = {
            "birthTime": birthTime.to_json(),
            "atTime": atTime.to_json(),
            "eventTagList": eventTagList,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SearchEvents(cls, birthTime, startTime, endTime, eventTagList, precisionHours=100):
        """
         Searches for all matching events that occur within a specified time range. This is the workhorse for timeline and calendar views it answers what happens during this period. 
        :return: List`1
         """
        endpoint = "SearchEvents"
        params = {
            "birthTime": birthTime.to_json(),
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "eventTagList": eventTagList,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetEventTiming(cls, birthTime, checkTime, nameOfEvent):
        """
         Resolves the full timing window start and end for a single specific event given a moment at which the event is believed to be active. If the event is not active at the supplied check time returns Event.Empty. 
        :return: Event
         """
        endpoint = "GetEventTiming"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
            "nameOfEvent": nameOfEvent,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def ListEventTypes(cls, ):
        """
         Returns the full list of event definitions supported by the engine. Used for discovery autocomplete dropdowns app builders and any UI that needs to enumerate what kinds of events the system can compute. 
        :return: List`1
         """
        endpoint = "ListEventTypes"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MatchReport(cls, maleBirthTime, femaleBirthTime):
        """
         Creates a full Kutabased compatibility report for two birth times. The method wraps the male and female birth times into temporary Person objects passes those objects into the compatibility engine returns the generated MatchReport. This is the core compatibility method for producing a standard Vedic match report between two charts. 
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
         Generates a combined compatibility report that includes both the standard Vedic match report and additional Bazibased compatibility analysis. The method 1. builds the regular Vedic compatibility report 2. calls the external Bazi API twice in parallel once for friendship analysis once for marriage analysis 3. merges all results into a single JSON structure 4. removes extra indentation and carriage returns before returning the final string. This is useful when a broader multisystem compatibility summary is needed. 
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
         Builds a compact summary string of AIfilled relationship data for a famous person. The method collects the persons birth time the persons birth location the name of the first marriage partner the partners birth time the partners birth location the marriagerelated tag output. It then returns all of that information as a single commaseparated string. 
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
         Uses a language model to estimate or retrieve a famous persons birth time in a specific text format. The method reads the configured API key sends a prompt with example formatting asks the model to return a birth time in the form HHmm DDMMYYYY zzz extracts the assistant response from the returned JSON. 
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
         Uses a language model to generate a short marriagerelated tag for a couple. The prompt examples show the model how to respond using compact labels such as 2Years 14Years StillMarried This helper is intended to produce a quick summary of the couples marriage duration or status. 
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
         Uses a language model to generate a famous persons birth location in a simplified plaintext format. The prompt instructs the model to return a location in the form city state country 
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
         Uses a language model to return the name of a famous persons first marriage partner. The method sends a guided prompt with an example and returns the models final answer as plain text. 
        :return: Task`1
         """
        endpoint = "MarriagePartnerNameAutoAIFill"
        params = {
            "personFullName": personFullName,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AIBirthDataParser(cls, birthDataRawText):
        """
         Accepts a freeform naturallanguage birth description and returns a parsed Person JSON object. Sends the raw text to the Rahu Nova LLM and converts the reply to a valid Person instance. Defaults GenderFemale Time1200 noon LocationNew Delhi India 0530. 
        :return: Task`1
         """
        endpoint = "AIBirthDataParser"
        params = {
            "birthDataRawText": birthDataRawText,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def MatchChat(cls, maleBirthTime, femaleBirthTime, userQuestion, chatSession=None):
        """
         Intended to send a compatibilityrelated question to the AI astrologer using two birth charts. The method currently switches the ayanamsa setting to RAMAN prepares for a future chatbased compatibility workflow throws NotImplementedException. 
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
         Searches horoscope predictions using an LLMpowered or embeddingbased search service. The method 1. converts the birth time into URLfriendly form 2. prepares a JSON payload containing the search query and birth time 3. posts the request to a remote search endpoint 4. converts each returned item into a HoroscopePrediction 5. returns the final list. This is useful for semantic search across horoscope prediction data. 
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
         Generates a CSV table of evenly spaced time entries between two points in time. The output contains three columns Name Time Location For each generated time slice the method adds a row name such as row0 the formatted standard date and time the location name with commas removed so the CSV stays valid. This is useful for building machinelearning or datascience input tables from time ranges. 
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
         Checks whether a given house is in a specific zodiac sign at the supplied time. This is a convenience method that compares the current sign of the house against the expected sign and returns a simple trueorfalse result. 
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
         Returns only the zodiac sign name for the specified house at the given time. The method calls HouseRasiSign... and extracts just the sign name from the fuller ZodiacSign result. 
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
         Returns the Bhava Chalit sign for a house based on the houses middle longitude. The method loads all house longitudes finds the requested house reads that houses middle longitude converts the longitude into a zodiac sign. This gives the sign occupied by the actual house midpoint rather than the counted sign from Lagna. 
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
         Returns the Rasi sign of a house by counting from the sign of House 1 Lagna. The method 1. finds the sign at the midpoint of House 1 2. counts forward by the requested house number 3. returns the resulting sign while preserving the same degree position within the sign. This is the housesign calculation used for Rasistyle house mapping. 
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
         Returns the Bhava Chalit sign for every house at the given time. The method builds a dictionary where each key is a HouseName and each value is the Bhava Chalit sign for that house. 
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
         Returns the Rasi sign for every house at the given time. This is the bulk version of HouseRasiSign... packaged as a dictionary for all houses. 
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
         Returns the Hora D2 sign for every house at the given time. 
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
         Returns the Drekkana D3 sign for every house at the given time. 
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
         Returns the Chaturthamsha D4 sign for every house at the given time. 
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
         Returns the Saptamsha D7 sign for every house at the given time. 
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
         Returns the Navamsha D9 sign for every house at the given time. 
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
         Returns the Dashamamsha D10 sign for every house at the given time. 
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
         Returns the Dwadashamsha D12 sign for every house at the given time. 
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
         Returns the Shodashamsha D16 sign for every house at the given time. 
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
         Returns the Vimshamsha D20 sign for every house at the given time. 
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
         Returns the Chaturvimshamsha D24 sign for every house at the given time. 
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
         Returns the Bhamsha D27 sign for every house at the given time. 
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
         Returns the Trimshamsha D30 sign for every house at the given time. 
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
         Returns the Khavedamsha D40 sign for every house at the given time. 
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
         Returns the Akshavedamsha D45 sign for every house at the given time. 
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
         Returns the Shashtyamsha D60 sign for every house at the given time. 
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
         Calculates the divisional longitude of a planet for a specified divisional chart number. The method 1. gets the planets Nirayana longitude 2. multiplies that longitude by the divisional chart number 3. normalizes the result into the expected divisional range 4. returns the final angle. This is a generalpurpose helper for Dchart calculations. 
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
         Calculates a normalized divisional longitude from an input degree value and a divisional chart number. The method multiplies the incoming longitude by the divisional factor repeatedly subtracts 30 degrees until the result falls inside a singlesign range returns the final value as an Angle. 
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
         Returns a planets zodiac sign based on the house it occupies according to house longitudes. The method finds which house the planet occupies using houseboundary logic gets the Bhava Chalit sign for that house returns the resulting sign. This is a D0style housebased sign lookup rather than a direct Rasi sign lookup. 
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
         Returns the planets standard Rasi D1 sign at the given time. The method uses caching to avoid repeated calculation gets the planets Nirayana longitude converts that longitude into a zodiac sign returns the final ZodiacSign. 
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
         Returns the planets Hora D2 sign at the given time. The method starts from the planets Rasi sign and converts it into the corresponding Hora sign. 
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
         Converts a regular zodiac sign into its Hora D2 equivalent. This is the core signconversion helper for Hora chart calculations. 
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
         Returns the Hora D2 sign at a given longitude. The method first resolves the regular zodiac sign at the longitude and then converts it into the Hora sign. 
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
         Returns the Hora D2 sign of a house using the midpoint of House 1 as the starting reference. The method 1. finds the Hora sign of House 1 2. counts forward by the requested house number 3. preserves the degree component from the starting sign. 
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
         Returns the planets Drekkana D3 sign at the given time. The method converts the planets Rasi sign into its Drekkana equivalent. 
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
         Converts a zodiac sign into its Drekkana D3 equivalent. This is the main signconversion helper for Drekkana chart calculations. 
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
         Returns the Drekkana D3 sign at a given longitude. The method first resolves the regular zodiac sign at that longitude and then converts it to its Drekkana form. 
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
         Returns the Drekkana D3 sign for a house based on the Drekkana sign of House 1. The method finds the midpoint sign of House 1 in Drekkana terms counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the planets Chaturthamsha D4 sign at the given time. The method starts with the planets standard Rasi D1 sign and converts it into the corresponding D4 sign. 
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
         Converts a regular zodiac sign into its Chaturthamsha D4 equivalent. This is the core signconversion helper used for D4 chart calculations. 
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
         Returns the Chaturthamsha D4 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D4 sign. 
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
         Returns the Chaturthamsha D4 sign for a house using the midpoint of House 1 as the reference. The method 1. finds the D4 sign of House 1 2. counts forward to the requested house 3. preserves the degree value from the starting sign. 
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
         Returns the planets Saptamsha D7 sign at the given time. The method converts the planets Rasi sign into its D7 equivalent. 
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
         Converts a zodiac sign into its Saptamsha D7 equivalent. This is the main signconversion helper used for D7 chart calculations. 
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
         Returns the Saptamsha D7 sign at the specified longitude. The method first resolves the ordinary zodiac sign at that longitude and then converts it to its D7 form. 
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
         Returns the Saptamsha D7 sign for a house based on the D7 sign of House 1. The method finds the midpoint sign of House 1 in D7 terms counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Calculates a planets Saptamsha D7 sign using an older legacy method retained for reference and comparison. The method 1. gets the planets Rasi sign and degree within that sign 2. determines which seventhpart division the planet falls into 3. applies different counting rules for odd and even signs 4. returns the resulting zodiac sign name. This method appears to preserve an older B. V. Ramanstyle approach and is clearly marked in the source as legacy logic. 
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
         Returns the planets Navamsha D9 sign at the given time. The method converts the planets Rasi sign into its D9 equivalent. 
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
         Converts a zodiac sign into its Navamsha D9 equivalent. This is the main signconversion helper used for D9 chart calculations. 
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
         Returns the Navamsha D9 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D9 sign. 
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
         Returns the Navamsha D9 sign for a house using the midpoint of House 1 as the reference. The method 1. finds the D9 sign of House 1 2. counts forward to the requested house 3. preserves the degree component from the starting sign. 
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
         Calculates the Navamsha D9 sign at a longitude using an older manual method retained for compatibility and comparison. The method 1. determines the ordinary zodiac sign 2. chooses the starting Navamsha sign based on the sign group 3. calculates the current Navamsha division from the degrees in sign 4. counts forward to the final Navamsha sign. This is a legacy implementation preserved alongside the newer tabledriven approach. 
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
         Returns the planets Dashamamsha D10 sign at the given time. The method converts the planets Rasi sign into its D10 equivalent. 
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
         Converts a zodiac sign into its Dashamamsha D10 equivalent. This is the main signconversion helper used for D10 chart calculations. 
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
         Returns the Dashamamsha D10 sign at the specified longitude. The method resolves the ordinary zodiac sign at the longitude and then converts it into the D10 sign. 
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
         Returns the Dashamamsha D10 sign for a house based on the D10 sign of House 1. The method finds the D10 sign of House 1 counts forward to the requested house preserves the degree value from the starting sign. 
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
         Returns the planets Dwadashamsha D12 sign at the given time. The method converts the planets Rasi sign into its D12 equivalent. 
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
         Converts a zodiac sign into its Dwadashamsha D12 equivalent. This is the main signconversion helper used for D12 chart calculations. 
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
         Returns the Dwadashamsha D12 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D12 sign. 
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
         Returns the Dwadashamsha D12 sign for a house using the midpoint of House 1 as the reference. The method 1. finds the D12 sign of House 1 2. counts forward to the requested house 3. preserves the degree component from the starting sign. 
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
         Calculates a planets Dwadashamsha D12 sign using an older manual method retained in the codebase. The method gets the planets Rasi sign and degree within that sign determines which twelfthpart division the planet occupies counts forward from the planets sign by that division number returns the resulting zodiac sign name. This preserves a legacy calculation path for comparison with the newer tabledriven implementation. 
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
         Returns the planets Shodashamsha D16 sign at the given time. The method converts the planets Rasi sign into its D16 equivalent. 
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
         Converts a zodiac sign into its Shodashamsha D16 equivalent. This is the main signconversion helper used for D16 chart calculations. 
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
         Returns the Shodashamsha D16 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D16 sign. 
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
         Returns the Shodashamsha D16 sign for a house using the midpoint of House 1 as the reference. The method finds the D16 sign of House 1 counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the planets Vimshamsha D20 sign at the given time. The method converts the planets Rasi sign into its D20 equivalent. 
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
         Converts a zodiac sign into its Vimshamsha D20 equivalent. This is the main signconversion helper used for D20 chart calculations. 
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
         Returns the Vimshamsha D20 sign at the specified longitude. The method resolves the ordinary zodiac sign at the longitude and then converts it into the D20 sign. 
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
         Returns the Vimshamsha D20 sign for a house using House 1 as the reference point. The method 1. finds the D20 sign of House 1 2. counts forward to the requested house 3. keeps the degree value from the starting sign. 
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
         Returns the planets Chaturvimshamsha D24 sign at the given time. The method converts the planets Rasi sign into its D24 equivalent. 
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
         Converts a zodiac sign into its Chaturvimshamsha D24 equivalent. This is the main signconversion helper used for D24 chart calculations. 
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
         Returns the Chaturvimshamsha D24 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D24 sign. 
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
         Returns the Chaturvimshamsha D24 sign for a house using the midpoint of House 1 as the starting reference. The method finds the D24 sign of House 1 counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the planets Bhamsha Saptavimshamsha D27 sign at the given time. The method starts with the planets standard Rasi D1 sign and converts it into the corresponding D27 sign. 
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
         Converts a zodiac sign into its Bhamsha D27 equivalent. This is the main signconversion helper used for D27 chart calculations. 
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
         Returns the Bhamsha D27 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D27 sign. 
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
         Returns the Bhamsha D27 sign for a house using the midpoint of House 1 as the starting reference. The method 1. finds the D27 sign of House 1 2. counts forward to the requested house 3. preserves the degree component from the starting sign. 
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
         Returns the planets Trimshamsha D30 sign at the given time. Unlike most other divisional methods in this section this one uses dedicated D30 logic rather than a simple tablebased conversion. The method converts the planets Rasi sign into its D30 result using the Trimshamshaspecific division rules preserved in the source. 
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
         Converts a zodiac sign into its Trimshamsha D30 equivalent using the special Trimshamsha division rules. The method reads the sign and its degree position determines the current Trimshamsha segment applies different rulership rules for odd and even signs returns the resulting sign with a divisional degree value. This is a custom D30 implementation and is more detailed than the standard tabledriven divisional helpers. 
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
         Returns the Trimshamsha D30 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then applies the Trimshamsha conversion rules. 
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
         Returns the Trimshamsha D30 sign for a house based on the D30 sign of House 1. The method finds the midpoint sign of House 1 in D30 terms counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the planets Khavedamsha D40 sign at the given time. The method converts the planets Rasi sign into its D40 equivalent. 
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
         Converts a zodiac sign into its Khavedamsha D40 equivalent. This is the main signconversion helper used for D40 chart calculations. 
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
         Returns the Khavedamsha D40 sign at the specified longitude. The method first resolves the ordinary zodiac sign at that longitude and then converts it into the D40 sign. 
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
         Returns the Khavedamsha D40 sign for a house using the midpoint of House 1 as the reference. The method 1. finds the D40 sign of House 1 2. counts forward to the requested house 3. preserves the degree component from the starting sign. 
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
         Returns the planets Akshavedamsha D45 sign at the given time. The method converts the planets Rasi sign into its D45 equivalent. 
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
         Converts a zodiac sign into its Akshavedamsha D45 equivalent. This is the main signconversion helper used for D45 chart calculations. 
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
         Returns the Akshavedamsha D45 sign at the specified longitude. The method first resolves the ordinary zodiac sign at the given longitude and then converts it into the D45 sign. 
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
         Returns the Akshavedamsha D45 sign for a house using the midpoint of House 1 as the starting reference. The method finds the D45 sign of House 1 counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the planets Shashtyamsha D60 sign at the given time. The method converts the planets Rasi sign into its D60 equivalent. 
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
         Converts a zodiac sign into its Shashtyamsha D60 equivalent. This is the main signconversion helper used for D60 chart calculations. 
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
         Returns the Shashtyamsha D60 sign at the specified longitude. 
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
         Returns the Shashtyamsha D60 sign for a house based on the D60 sign of House 1. The method finds the D60 sign of House 1 counts forward to the requested house preserves the degree portion from the starting sign. 
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
         Returns the zodiac sign of every planet based on the houselongitude method rather than the direct Rasi sign. Each planet is mapped to the sign computed from the house midpoint longitude which can differ from the standard Rasi sign and is used in Bhavacentric analysis. 
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
         Returns the Rasi D1 sign for every planet at the given time. 
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
         Returns the Hora D2 sign for every planet at the given time. 
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
         Returns the Drekkana D3 sign for every planet at the given time. 
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
         Returns the Chaturthamsha D4 sign for every planet at the given time. 
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
         Returns the Saptamsha D7 sign for every planet at the given time. 
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
         Returns the Navamsha D9 sign for every planet at the given time. 
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
         Returns the Dashamsha D10 sign for every planet at the given time. 
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
         Returns the Dwadashamsha D12 sign for every planet at the given time. 
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
         Returns the Shodamsha D16 sign for every planet at the given time. 
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
         Returns the Vimshamsha D20 sign for every planet at the given time. 
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
         Returns the Chaturvimshamsha D24 sign for every planet at the given time. 
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
         Returns the Bhamsha D27 sign for every planet at the given time. 
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
         Returns the Trimshamsha D30 sign for every planet at the given time. 
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
         Returns the Khavedamsha D40 sign for every planet at the given time. 
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
         Returns the Akshavedamsha D45 sign for every planet at the given time. 
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
         Returns the Shashtyamsha D60 sign for every planet at the given time. 
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
         Returns the Tajika longitude of a planet for a specific year. The method calculates the Tajika or annualreturn date for the requested year finds the planets Nirayana longitude at that annualreturn moment returns the resulting longitude. This is useful when building or analyzing a Tajika Varshaphala chart for a given year of life. 
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
         Returns the Tajika constellation of a planet for a specific year. The method gets the planets Tajika longitude converts that longitude into a constellation returns the final Constellation. This is the constellationlevel view of a planets Tajika placement. 
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
         Returns the Tajika zodiac sign of a planet for a specific year. The method calculates the planets Tajika longitude converts that longitude into a zodiac sign returns the resulting ZodiacSign. This provides the sign placement of the planet in the annual Tajika chart. 
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
         Calculates the exact Tajika date and time for a given year by scanning forward until the Sun returns to the same sign and nearly the same degree it held at birth. The method gets the Suns sign and degree at birth starts searching a few days before the birthday in the requested year scans forward in small time steps compares the Suns current sign and insign degree against the birth position stops when both values match within a small tolerance. This method reflects the core Tajika idea that the annual chart begins when the Sun returns to the same position it occupied at birth. 
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
         Calculates the Tajika annualreturn date and time for a given year using a traditional tablebased approach described in B. V. Ramans Varshaphala. The source comments explain that this method is based on a siderealyear duration of roughly 365 days 6 hours 9 minutes 12 seconds. The method caches the result and prepares lookup records for year offsets drawn from the referenced text. 
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
         Calculates which house a transiting planet occupies when counted from the natal Lagna Ascendant. The method gets the natal Lagna sign gets the transiting planets current Rasi sign at checkTime counts from the natal Lagna sign to the transit sign returns the result as a HouseName. 
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
         Calculates which house a transiting planet occupies when counted from the natal Navamsha Lagna. The method gets the Navamsha sign of House 1 at birth gets the transiting planets current Rasi sign counts from the natal Navamsha Lagna sign to the transit sign returns the result as a HouseName. 
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
         Calculates which house a transiting planet occupies when counted from the natal Moon sign Janma Rashi. This is one of the core referenceframe helpers for transit interpretation. 
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
         Calculates which house a transiting planet occupies when counted from the natal Navamsha Moon sign. The method uses the Moons Navamsha sign at birth as the reference point rather than the standard Rasi Moon sign. 
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
         Intended to calculate the Murthi or symbolic transit form of a planet Swarna Gold Rajata Silver Tamra Copper Loha Iron. The method comments indicate that the result should be based on the planets transit position counted from the natal Moon sign. 
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
         Builds a full bPanchanga summary objectb for the supplied time. The method gathers a compact set of daily astrological values including ayanamsa tithi lunar month weekday Moon constellation nithya yoga karana hora lord disha shool sunrise sunset ishta kaala. This is a convenience method for producing one bundled Panchanga snapshot instead of calling each item separately. 
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
         Returns the binauspicious travel directionb for the weekday of the supplied time. The method 1. calculates the Vedic weekday 2. maps that weekday to its corresponding Disha Shool direction 3. returns the final direction as text. 
        :return: String
         """
        endpoint = "DishaShool"
        params = {
            "inputTime": inputTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def LunarMonth(cls, inputTime, ignoreLeapMonth=False):
        """
         Calculates the bcurrent lunar monthb using New Moon boundaries and the sign of the SunMoon conjunction. The method 1. starts from the sunrise of the given date 2. finds the previous and next New Moon 3. determines the relevant month sign 4. detects whether the month is a leap month cAdhikac 5. returns the corresponding cLunarMonthc enum value. 
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
         Finds the bnext New Moonb after the supplied time by scanning forward in small time steps. The method starts at the input time moves forward in 30minute increments checks the SunMoon conjunction angle at each step returns the first time where the conjunction angle is under 1 degree. 
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
         Finds the bmost recent New Moonb before the supplied time by scanning backward in small time steps. The method starts at the input time moves backward in 30minute increments checks the SunMoon conjunction angle at each step returns the first time where the conjunction angle is under 1 degree. 
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
         Calculates the bangular distance between the Moon and the Sunb at a given time. The method 1. gets the Nirayana longitudes of the Sun and Moon 2. computes the difference 3. normalizes the result to the c0360c range. This helper is used mainly for New Moon detection and lunarmonth calculations. 
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
         Returns all bAvasta statesb that match for a planet at the given time. The method checks the six supported Avastas in this section Lajjita Garvita Kshudita Trashita Trishita Mudita Kshobhita. Any matching states are collected into a list and returned. 
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
         Checks whether a planet is in bLajjita Avastab in the current implementation. The source description says Lajjita applies when a planet is in the 5th house and joined by certain difficult planets. The current code checks whether the input planet is in the 5th house and whether the list Rahu Ketu Saturn Mars is in the 5th house. 
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
         Checks whether a planet is in bGarvita Avastab. The method returns ctruec when the planet is either in exaltation or in its Moolatrikona zone. 
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
         Checks whether a planet is in bKshudita Avastab. The current implementation treats the planet as Kshudita when banyb of the following is true it is in an enemy sign it is conjoined with enemy planets it is aspected by enemy planets. 
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
         Checks whether a planet is in bTrashita Trishita Avastab. The current code requires all of the following the planet is in a watery sign the planet is aspected by an enemy the planet is bnotb aspected by benefic planets. 
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
         Checks whether a planet is in bMudita Avastab. The method returns ctruec when banyb of the following applies the planet is in a friendly sign the planet is conjoined with Jupiter the planet is conjoined with a friendly planet the planet is aspected by a friendly planet. 
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
         Checks whether a planet is in bKshobhita Avastab using the current code logic. The source description says this state involves conjunction with the Sun plus difficult hostile influence. The implementation checks conjunction with the Sun then combines the bnegatedb results of the enemyaspect and maleficaspect checks returns ctruec only if the full codedefined condition passes. 
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
         Calculates the periods during which a planet stays in each bzodiac signb between two times. The method 1. generates time slices across the requested range 2. tracks sign changes for the selected planet 3. records each finished sign interval as a tuple of start time end time sign name planet name. 
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
         Returns the times at which a planet benters a new constellationb between two dates. For each detected constellation change the method returns the transition time the new constellation name the zodiac sign occupied at that moment. 
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
         Returns the Nirayana bconstellation of all nine planetsb at the given time. 
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
         Runs the librarys automatic discovery system to return ball supported calculationsb that accept a single cTimec input. The method excludes itself from the search before executing the matching functions. 
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
         Runs the automatic discovery system to return ball supported calculationsb that accept a cPlanetNamec and cTimec. 
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
         Runs the automatic discovery system to return ball supported calculationsb that accept a cHouseNamec and cTimec. 
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
         Runs the automatic discovery system to return ball supported calculationsb that accept a cPlanetNamec cHouseNamec and cTimec. 
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
         Runs the automatic discovery system to return ball supported calculationsb that accept a cZodiacNamec and cTimec. 
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
         Converts a btime offsetb into its equivalent longitude. The method treats 1 hour as 15 degrees and returns the result as an cAnglec. 
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
         Converts a cTimec value into bJulian Day in Ephemeris Time ET TTb and caches the result. The method 1. converts the input time to UTC 2. calls the Swiss Ephemeris cswe_utc_to_jdc function 3. returns cresults0c which is Julian Day in ET TT. 
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
         Converts a cTimec value into bJulian Day in Universal Time UTb and caches the result. The method follows the same Swiss Ephemeris conversion path as cTimeToJulianEphemerisTime...c but returns cresults1c the UT component instead of ET. 
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
         Converts bLocal Mean Time LMTb into bStandard Time STDb using a supplied standard offset. The method 1. reconstructs the source cDateTimeOffsetc from the LMT date and longitude 2. converts that offset to the requested standard offset 3. returns the resulting standard time. 
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
         Converts a longitude into its corresponding bLocal Mean Time offsetb. The method validates that the longitude is in the expected range attempts a limited autocorrection when values appear to be off by a factor such as c1000c converts longitude to hours using the c15 1 hourc rule rounds the result to the nearest minute returns the final offset. 
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
         Returns the supplied time formatted as bLocal Mean Time LMTb text. 
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
         Returns the supplied time formatted as bLocal Standard Timeb text. 
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
         Builds a cTimeRangec automatically from a compact btime preset stringb. This method supports several preset styles including simple relative spans such as c3daysc c2yearsc cweekc or cmonthc year ranges such as c19902000c age ranges such as cage1to50c special presets such as cfulllifec The method 1. uses the birth location from cinputBirthTimec 2. interprets the requested output timezone as the display or client timezone 3. detects which preset style was supplied 4. routes the request to the matching preset parser 5. returns the resulting cTimeRangec. 
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
         Calculates the number of days represented by a time preset. The method 1. converts the preset into a cTimeRangec using cAutoCalculateTimeRange...c 2. measures the total days between the start and end 3. rounds the result to two decimal places. This is used by the web UI and API when estimating chart ranges or precision needs. 
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
         Parses raw bJagannatha Hora c.jhdc file textb and converts it into a cPersonc object that can be used inside VedAstro. The method 1. splits the raw file into lines 2. extracts the birth date and decimalhour time 3. converts the custom timezone format into a usable cTimeSpanc 4. parses the location name and coordinates 5. builds a cGeoLocationc 6. builds a cTimec 7. reads the gender code 8. combines everything into a cPersonc. This is a convenience importer for bringing JHora data into the librarys own object model. 
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
         Exports all horoscope prediction definitions in a simple bAlpacastyle instruction datasetb format for model training. For each stored horoscope rule the method creates a JSON object with cinstructionc the prediction name cinputc an empty string coutputc the prediction description. 
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
         Builds a compact btrainingdata summaryb from selected horoscope prediction categories. The method 1. limits processing to a small tag set Rising Sign Planet In Signs Planet In House House Yoga 2. gets the predictions for each tag 3. keeps the top 70 of each group after weight sorting 4. joins the selected descriptions and names into one combined string 5. returns the result inside a cJObjectc. 
        :return: Task`1
         """
        endpoint = "HoroscopePredictionsForLargeAstrologyModelTrainingData"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictionsWithBazi(cls, birthTime, sortByWeight=False):
        """
         Generates a combined horoscope result that includes both top weighted bVedic predictionsb and additional bBazi APIb output. The method 1. extracts birth date and hour from the cTimec object 2. calls the external Bazi API 3. removes part of the returned Bazi text 4. removes a specific malelabel marker from the Bazi output 5. calculates Vedic predictions 6. keeps the top 40 Vedic results 7. packages both streams into one JSON object. 
        :return: Task`1
         """
        endpoint = "HoroscopePredictionsWithBazi"
        params = {
            "birthTime": birthTime.to_json(),
            "sortByWeight": sortByWeight,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def HoroscopePredictions(cls, birthTime, filterTags=None, sortByWeight=False):
        """
         Returns all horoscope predictions whose underlying events are currently true for the given birth chart. The method 1. starts with the full stored prediction list 2. optionally filters by event tags 3. keeps only predictions whose event condition is active 4. optionally calculates a weight score using related planet and house strengths 5. sorts the results by descending weight when requested. 
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
         Calculates the bFortuna Pointb and returns its position as a bsign count from the Ascendant signb. The method 1. gets the Ascendant Moon and Sun longitudes 2. measures the Moons distance from the Sun 3. adds that arc to the Ascendant longitude 4. converts the resulting point into a zodiac sign 5. counts how many signs away that result is from the supplied Ascendant sign. 
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
         Calculates the bDestiny Pointb and returns its position as a bsign count from the Ascendant signb. The method 1. gets the Nirayana longitudes of Rahu and the Moon 2. measures the forward arc from Rahu to the Moon 3. takes the midpoint of that arc 4. adds the midpoint to Rahus longitude 5. converts the result into a zodiac sign 6. counts how many signs away that sign is from the Ascendant sign. 
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
         Returns the bYoni Kuta animalb for a birth chart as plain text. The method 1. gets the Moons constellation at birth 2. converts that constellation into its Yoni animal mapping 3. returns the animal information as a string. 
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
         Returns the bYoni Kuta animal and sex mappingb for a specific constellation. The method uses a fixed lookup table and returns the matching cConstellationAnimalc object. 
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
         Generates a bsky chartb for the given time and returns it as an SVG string. This is intended for direct display in a client application such as embedding the returned SVG as an image source or rendered chart asset. 
        :return: Task`1
         """
        endpoint = "SkyChart"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SouthIndianChart(cls, time, chartType="RasiD1"):
        """
         Creates a bSouth Indian style kundali chartb and returns the chart as an SVG string. The method supports different chart types such as D1 and other divisional charts supported by the chart factory. 
        :return: String
         """
        endpoint = "SouthIndianChart"
        params = {
            "time": time.to_json(),
            "chartType": chartType,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NorthIndianChart(cls, time, chartType="RasiD1"):
        """
         Creates a bNorth Indian style kundali chartb and returns the chart as an SVG string. Like the South Indian variant this method supports multiple chart types through the cchartTypec parameter. 
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
         Converts a time value into a bJulian Day number in Universal Time UTb using Swiss Ephemeris. The method 1. gets the local mean time from the cTimec object 2. converts it to UTC 3. passes the UTC date and fractional hour into Swiss Ephemeris 4. returns the resulting Julian Day value. This helper is a direct localized conversion method used when a Julian Day number is needed for astronomical calculations. 
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
         Converts a cTimec value from bLocal Mean Time LMTb into a bJulian Day number in Universal Time UTb and caches the result. The method 1. checks the cache using both the time and current cAyanamsac 2. extracts the LMT date parts 3. passes the values into Swiss Ephemeris 4. returns the Julian Day result. This is the cached Julian conversion helper used by the librarys astronomical calculations. 
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
         Calculates the bsmallest angular distanceb between two planets. The method 1. gets the Nirayana longitude of both planets 2. computes the absolute longitudinal difference 3. reduces the result to the smaller arc 4. returns the final value as an cAnglec. 
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
         Converts the supplied time into bGreenwich Apparent Time in Julian daysb. The method 1. gets the Greenwich LMT value in Julian days 2. reads the location longitude 3. calls Swiss Ephemeris to convert from local mean time to local apparent time 4. returns the final Julianday value. 
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
         Returns the bLocal Apparent Time LATb for a supplied time and caches the result. The method 1. converts the input into Julian LMT 2. converts that value to local apparent time through Swiss Ephemeris 3. converts the Julian result back into a normal cDateTimec 4. returns the final local apparent time. 
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
         Returns the raw bSwiss Ephemeris calculation outputb for a single planet. This is an APIfacing wrapper around the lowerlevel Swiss Ephemeris call and exposes values such as longitude latitude distance speed components. 
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
         Returns raw bSwiss Ephemeris data for a wider planet setb including the outer planets and the nodes. The method prepares a mapping of Swiss Ephemeris planet IDs and collects the returned values into a dictionary keyed by display name. 
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
         Checks whether a planet occupies the bsame houseb as the lord of a specified house. This method does bnotb require exact conjunction by degree. It only checks whether both bodies fall in the same house by signbased house occupation logic. 
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
         Calculates a brelative nature scoreb for a house based on house strength. The method 1. returns c0c immediately if no valid house is supplied 2. calculates the selected houses strength 3. finds the strongest and weakest houses in the chart 4. remaps the selected houses strength onto a simplified scoring range. This helper is designed for summarystyle interpretation rather than precise technical measurement. 
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
         Calculates a simplified bnature scoreb for a planet based on its Shadbaladerived strength. The method 1. calculates the planets Shadbala Pinda strength 2. maps that strength into broad score bands 3. returns a simplified positive or negative result. This is a summaryoriented helper intended for easy interpretation rather than full technical analysis. 
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
         Calculates the longitude of bDhumab an Upagraha derived from the Sun. The method 1. gets the Suns Nirayana longitude 2. adds b13320b 3. normalizes the result to the c0360c range. 
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
         Calculates the longitude of bVyatipaatab from Dhuma. The method 1. gets Dhumas longitude 2. subtracts it from b360b 3. normalizes the result. 
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
         Calculates the longitude of bPariveshab from Vyatipaata. The method 1. gets Vyatipaatas longitude 2. adds b180b 3. normalizes the result. 
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
         Calculates the longitude of bIndrachaapab from Parivesha. The method 1. gets Pariveshas longitude 2. subtracts it from b360b 3. normalizes the result. 
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
         Calculates the longitude of bUpaketub from Indrachaapa. The method 1. gets Indrachaapas longitude 2. adds b1640b 3. normalizes the result. 
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
         Calculates the longitude of bKaalab the Upagraha associated with the bmiddle of the Suns planetary partb. The method delegates to cUpagrahaLongitude...c which determines the relevant day or night segment and returns the Lagna longitude rising at that selected point. 
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
         Calculates the longitude of bMrityub the Upagraha associated with the bmiddle of Marss planetary partb. The method delegates to cUpagrahaLongitude...c and uses Mars as the related planet for the selected part. 
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
         Calculates the longitude of bArthaprahaarab the Upagraha associated with the bmiddle of Mercurys planetary partb. The method delegates the actual calculation to cUpagrahaLongitude...c. 
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
         Calculates the longitude of bYamaghantakab the Upagraha associated with the bmiddle of Jupiters planetary partb. The method delegates to cUpagrahaLongitude...c and uses Jupiter as the related planet. 
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
         Calculates the longitude of bGulikab using the bbeginning of Saturns planetary partb in the current implementation. The method delegates to cUpagrahaLongitude...c and requests the cbeginc position for Saturns part. 
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
         Calculates the longitude of bMaandib using the bmiddle of Saturns planetary partb in the current implementation. The method delegates to cUpagrahaLongitude...c and requests the cmiddlec position for Saturns part. 
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
         Calculates the longitude of a bnonsolar Upagrahab by finding the Lagna rising at a selected planetary part of the day or night. The method works as follows 1. determines which numbered part belongs to the related planet 2. checks whether the birth or event time is during the day or night 3. divides the relevant daylight or nighttime span into b8 equal partsb 4. calculates the start and middle of the requested part 5. selects either the bbeginningb or bmiddleb of that part 6. calculates the house longitudes for that selected moment 7. returns the longitude of bHouse 1 Lagnab as the Upagraha longitude. This is the central calculation helper behind Kaala Mrityu Arthaprahaara Yamaghantaka Gulika and Maandi. 
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
         Returns the numbered bUpagraha planetary partb for a planet at a given time. The method 1. checks whether the time falls in a day birth or night birth context 2. selects the matching weekday rule table 3. returns the part number from c1c to c8c for the requested planet. 
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
         Checks whether a planet name belongs to the bUpagrahab set used by this library. The method returns ctruec for the supported Upagraha names including Dhuma Vyatipaata Parivesha Indrachaapa Upaketu Kaala Mrityu Arthaprahaara Yamaghantaka Gulika Maandi. 
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
    def AshtakvargaLifeMap(cls, birthTime):
        """
         Returns housemapped Sarvashtakavarga with strength assessments for the Life Map visualization. Every chart totals 337 the distribution across 12 houses shows where life energy concentrates. Per BV Raman Ashtakavarga System Ch. XI. 
        :return: AshtakvargaLifeMapResult
         """
        endpoint = "AshtakvargaLifeMap"
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
         Returns the reduced bindu count for a planet in a specific sign after applying the standard Ashtakavarga reduction steps. The method applies the alreadycomputed reduction pipeline and then returns the final value after Trikona reduction Ekadhipatya reduction. 
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
         Returns the full Ashtakavarga reduction result for a planet. The result includes the major intermediate and final stages of the reduction pipeline such as the raw values the values after Trikona reduction the values after Ekadhipatya reduction. 
        :return: AshtakavargaReductionResult
         """
        endpoint = "PlanetAshtakavargaReductions"
        params = {
            "planet": planet.value,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetSodyaPinda(cls, planet, birthTime, useReduced=True):
        """
         Calculates the Sodya Pinda for a planets Ashtakavarga. The method returns the combined Pinda value used in a range of timing strength and longevity calculations. 
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
         Calculates a gross longevity estimate using the Ashtakavarga Sodya Pinda method. The method calculates reduced Sodya Pinda values for the seven classical planets sums those values applies the standard longevity formula returns the result in years. 
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
         Returns an Ashtakavargabased strength score for a Dasa planet on a 0100 scale. The method calculates the planets Sodya Pinda normalizes it to a percentagelike scale rounds the final result. This can be used as a quick indicator of how strong a Dasa period may be from an Ashtakavarga perspective. 
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
         Returns the Sarvashtakavarga reduction result after applying the Mandala Sodhana reduction pipeline. This is a higherlevel reduction across the combined Sarvashtakavarga figures rather than a singleplanet Bhinnashtakavarga result. 
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
         Returns the Rekha Sarvashtakavarga result after the full reduction pipeline. This is the reduced 56bindu style Sarvashtakavarga variant referenced in the source comments. 
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
         Calculates Sodya Pinda from the reduced Sarvashtakavarga figures. 
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
         Calculates Sodya Pinda from the reduced Rekha Sarvashtakavarga figures. 
        :return: SodyaPindaResult
         """
        endpoint = "RekhaSodyaPinda"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def AshtakavargaTransitPrediction(cls, planet, houseFromPlanet, divisor, birthTime, useRawBindus=True):
        """
         Applies the general Ashtakavarga transit prediction formula for a given planet and target house. The source describes the calculation in the form result Sodya Pinda x bindus in house divided by divisor. Typical divisor values include 27 for Nakshatrabased calculations and 12 for signbased calculations. 
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
        Returns the first Saturnbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the Jupiterbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the Sunbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the second Saturnbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the Saturnsignbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the Sunsignbased Ashtakavarga transit prediction related to the fathers death timing.
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
        Returns the first Saturnbased Ashtakavarga transit prediction related to the mothers death timing.
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
        Returns the JupiterandSun combined Ashtakavarga transit prediction related to the mothers death timing.
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
        Returns the second Saturnbased Ashtakavarga transit prediction related to the mothers death timing.
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
        Returns the Saturnbased Ashtakavarga transit prediction for trouble or affliction involving a brother.
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
        Returns the Jupiterbased Ashtakavarga transit prediction for a brothers prosperity or improvement.
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
        Returns the Jupiterbased Ashtakavarga transit prediction related to mental balance steadiness or emotional support.
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
        Returns the Saturnbased Ashtakavarga transit prediction related to mental strain affliction or difficulty.
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
        Returns the Saturnbased Ashtakavarga transit prediction related to career setbacks loss or professional difficulty.
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
        Returns the first Jupiterbased Ashtakavarga transit prediction related to childbirth timing.
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
        Returns the second Jupiterbased Ashtakavarga transit prediction related to childbirth timing.
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
        Returns the Sunbased Ashtakavarga transit prediction used to narrow childbirth timing to a month.
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
        Returns the Ashtakavarga transit prediction related to the childs birth star or starbased timing indicator.
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
        Returns the Ashtakavarga transit prediction related to the childs Lagna or Ascendant indication.
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
        Returns the Jupiterbased Ashtakavarga transit prediction related to marriage timing.
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
        Returns the Jupiterbased Ashtakavarga transit prediction for the sign connected with marriage timing.
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
        Returns the Sunbased Ashtakavarga transit prediction used to narrow marriage timing to a month.
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
        Returns the Jupiterbased Ashtakavarga transit prediction related to the spouses death timing.
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
        Returns the Saturnbased Ashtakavarga transit prediction related to the natives death timing.
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
        Returns the Jupiterbased Ashtakavarga transit prediction related to the natives death timing.
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
        Returns the Sunbased Ashtakavarga transit prediction used to narrow the natives death timing to a month.
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
         Returns the Saturnbased Ashtakavarga transit prediction for affliction or distress affecting a specific house bhava. 
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
         Returns the Saturnbased Ashtakavarga transit prediction for improvement or benefit affecting a specific house bhava. 
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
        Returns the Sarvashtakavargabased transit prediction used to estimate or narrow the month connected with death timing.
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
         Returns a more detailed perplanet longevity analysis based on Ashtakavarga. The source notes that this extended result includes Haranastyle adjustments such as combustion debilitation enemysign reductions lunartosolar year conversion. 
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
         Returns a Sarvashtakavargabased detailed longevity result using the method tied to Sarvashtakavarga Sodya Pinda. This is the more detailed wrapper around the Sarvashtakavarga longevity calculation path. 
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
         Returns the Gochara sign count from the natal Moon sign for a given planet at a specific time. In this codebase Gochara refers to transits. The method gets the Moon sign at birth janma rasi gets the planets current Rasi sign counts from the natal Moon sign to the planets current sign returns the resulting housestyle count. This is one of the core helper methods used throughout the transit and Gochara logic. 
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
         Checks whether a given Gochara transit is obstructed by Vedha Vedhanka. The method looks up the obstruction point for the planet and transit house exits early if no Vedhanka exists finds all planets currently transiting that obstruction house removes the standard exception pairs Sun and Saturn Moon and Mercury returns true if any obstructing planet remains. This method applies the Vedha rule layer used to suppress or modify an otherwise valid Gochara result. 
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
         Returns all planets currently occupying a specific Gochara house where the house count is measured from the natal Moon sign. The method calculates the Gochara house for each tracked planet and returns a list of all planets whose current transit count matches the requested house. The current implementation checks Sun Moon Mars Mercury Jupiter Venus and Saturn. 
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
         Returns the Vedhanka or obstruction point for a given planet and Gochara house. The result is taken from a fixed rule table and is used by the Gochara subsystem to decide whether a transit is blocked by Vedha. 
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
         Checks whether a specific Gochara event is currently occurring for a planet in a given house while also honoring Vedha obstruction rules when enabled. The method checks whether the planet is in the requested Gochara house optionally checks whether the transit is obstructed by Vedhanka returns true only if the house match is valid and no obstruction remains. This acts as a practical wrapper for higherlevel Gochara event calculations. 
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
         Checks whether a planet is currently transiting through a sign whose Ashtakavarga bindu count matches the requested value. The method finds the planets current Gochara sign count from the natal Moon converts that count back into the actual transit sign reads the planets Ashtakavarga bindu value for that sign compares it with the requested bindu count. 
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
         Checks whether a planet is currently transiting through a sign with the requested bindu count and returns a richer explanationfriendly result. The method performs the same bindumatching logic as IsPlanetGocharaBindu... returns a negative result immediately when no match is found otherwise generates a dynamic interpretation string based on transit intensity housefromLagna placement planetary significations and Kakshya analysis. 
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
         Calculates the active Chara Dasa sign period at a given moment and when found also fills in its subperiods. The method determines the natal Lagna sign builds the Chara Dasa sign order from that Lagna calculates the duration of each Dasa sign generates the full sequence of Dasa periods finds which period contains the requested checkTime computes the subperiods for the active Dasa. This is the main entry point for Chara Dasa lookup in this section. 
        :return: DashaPeriod
         """
        endpoint = "GetCharaDasaAtTime"
        params = {
            "birthTime": birthTime.to_json(),
            "checkTime": checkTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaForNow(cls, birthTime, levels=3):
        """
        Empty sample text
        :return: JObject
         """
        endpoint = "DasaForNow"
        params = {
            "birthTime": birthTime.to_json(),
            "levels": levels,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaAtTime(cls, birthTime, checkTime, levels=3):
        """
        Empty sample text
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
    def DasaAtRange(cls, birthTime, startTime, endTime, levels=3, precisionHours=100):
        """
        Empty sample text
        :return: JObject
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
    def DasaForLife(cls, birthTime, levels=3, precisionHours=24, scanYears=100):
        """
        Empty sample text
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
    def DasaAtRangeString(cls, birthTime, startTime, endTime, levels=3, precisionHours=100):
        """
        Empty sample text
        :return: String
         """
        endpoint = "DasaAtRangeString"
        params = {
            "birthTime": birthTime.to_json(),
            "startTime": startTime.to_json(),
            "endTime": endTime.to_json(),
            "levels": levels,
            "precisionHours": precisionHours,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def DasaForLifeString(cls, birthTime, levels=3, precisionHours=24, scanYears=100):
        """
        Empty sample text
        :return: String
         """
        endpoint = "DasaForLifeString"
        params = {
            "birthTime": birthTime.to_json(),
            "levels": levels,
            "precisionHours": precisionHours,
            "scanYears": scanYears,
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
         Returns all event definitions grouped by their cEventTagc formatted as a JSON object. The method 1. loops through every value in the cEventTagc enum 2. gets the matching event definitions for that tag 3. converts each event definition into JSON 4. stores the results under the tag name 5. returns an empty JSON array for tags that currently have no event definitions. This is mainly intended for UI or API consumers that need to show users all available event types grouped by category. 
        :return: JObject
         """
        endpoint = "GetAllEventDataGroupedByTag"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetAllEventsChartAlgorithms(cls, ):
        """
         Returns the full list of supported beventchart algorithmsb. This is a simple passthrough helper intended for website or API use when showing users which eventcalculation algorithms are available for selection. 
        :return: JArray
         """
        endpoint = "GetAllEventsChartAlgorithms"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def GetHouseTags(cls, house):
        """
         Returns a plainEnglish keyword summary for a house. Each house is mapped to a compact descriptive string covering its main life themes such as health family children profession losses marriage longevity and related subjects. This helper is used when converting technical house references into more readable interpretation text. 
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
         Returns a plainEnglish keyword summary for a zodiac sign. The descriptions include traditional sign characteristics such as modality odd or even nature gender elemental quality temperament fertility ascensional type and rising style. This helper is intended to support signbased delineation especially for character and mentaldisposition interpretation. 
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
         Builds one combined descriptive string for a list of planets by concatenating the tag text of each planet. This is a convenience helper that repeatedly calls cGetPlanetTags...c and joins the results into a single string. 
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
         Returns a traditional keyword summary for a planet. The returned description may include themes such as relationships represented by the planet benefic or malefic nature color temperament responsibilities symbolic domains or other interpretive associations. This helper is used to translate a technical planet reference into plainEnglish interpretive keywords. 
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
         Returns the traditional bhousetype classification labelsb for a given house. Depending on the house number the returned string may include one or more of the following categories bQuadrants Kendrasb bTrines Trikonasb bCadent Panaparasb bSucceedent Apoklimasb bUpachayasb The method builds the result by checking the input house against multiple classification groups and concatenating the matching labels. 
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
         Returns traditional bDasa interpretation guidance for a given ascendantb. The method 1. selects the list of generally favorable planets for the ascendant 2. selects the list of generally unfavorable planets 3. retrieves a narrative description explaining how those planets behave for that Lagna 4. packages the result into an cAscendantDasaInfoc object. This helper is meant to support Dasa interpretation by giving quick signspecific guidance on which planets are broadly auspicious inauspicious or capable of producing yoga or maraka effects. 
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
         Returns the full cSignPropertiesc object for a zodiac sign. This is a simple convenience wrapper that constructs and returns the signproperties model for the requested sign. 
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
    def SignToNakshatra(cls, sign):
        """
        NO DESC FOUND!! ERROR
        :return: ConstellationName
         """
        endpoint = "SignToNakshatra"
        params = {
            "sign": sign.value,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def NakshatraToZodiacSign(cls, constellation):
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        endpoint = "NakshatraToZodiacSign"
        params = {
            "constellation": constellation,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsPlanetDefeatedInPlanetaryWar(cls, planet, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetDefeatedInPlanetaryWar"
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
    def IsPlanetAspectingOwnHouse(cls, planetName, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsPlanetAspectingOwnHouse"
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
    def PlanetChestaBala(cls, planetName, time, useSpecialSunMoon=False):
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
    def IsEarthquakeNearEclipse(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeNearEclipse"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMoonMercuryExactConjunction(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMoonMercuryExactConjunction"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeJupiterSaturnOpposition(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeJupiterSaturnOpposition"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeJupiterSaturnConjunction(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeJupiterSaturnConjunction"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeNearNewMoon(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeNearNewMoon"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeNearFullMoon(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeNearFullMoon"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeSaturnMarsInKendras(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeSaturnMarsInKendras"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMarsJupiterInKendras(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMarsJupiterInKendras"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMoonMercuryConjunction(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMoonMercuryConjunction"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMajorPlanetsInMutualKendras(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMajorPlanetsInMutualKendras"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakePlanetsClusteredInNarrowArc(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakePlanetsClusteredInNarrowArc"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMajorPlanetsInEarthySigns(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMajorPlanetsInEarthySigns"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMajorPlanetsInAirySigns(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMajorPlanetsInAirySigns"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakePrithviMandalaRuling(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakePrithviMandalaRuling"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeVayuMandalaRuling(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeVayuMandalaRuling"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeJupiterInKendraFromAscendant(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeJupiterInKendraFromAscendant"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMoonNearPerigee(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMoonNearPerigee"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMaleficsNearMeridian(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMaleficsNearMeridian"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def IsEarthquakeMercurySaturnConjunction(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        endpoint = "IsEarthquakeMercurySaturnConjunction"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def CalculateEarthquakeRiskScore(cls, time):
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        endpoint = "CalculateEarthquakeRiskScore"
        params = {
            "time": time.to_json(),
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
    def Chapter5Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter5Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
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
    def Chapter9Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter9Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter10Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter10Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter11Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter11Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter12Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter12Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter13Predictions(cls, birthTime, queryTime, firstLetterOfQuery=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter13Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
            "firstLetterOfQuery": firstLetterOfQuery,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter14Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter14Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter15Predictions(cls, birthTime, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter15Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter16Predictions(cls, birthTime, queryTime, thamBoolaLeafCount=None, firstLetterOfQuery=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter16Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "queryTime": queryTime.to_json(),
            "thamBoolaLeafCount": thamBoolaLeafCount,
            "firstLetterOfQuery": firstLetterOfQuery,
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
    def Chapter19Predictions(cls, birthTime, partnerBirthTime=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter19Predictions"
        params = {
            "birthTime": birthTime.to_json(),
            "partnerBirthTime": partnerBirthTime,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter20Predictions(cls, birthTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter20Predictions"
        params = {
            "birthTime": birthTime.to_json(),
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
    def Chapter25Predictions(cls, queryTime, firstLetterOfQuery=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter25Predictions"
        params = {
            "queryTime": queryTime.to_json(),
            "firstLetterOfQuery": firstLetterOfQuery,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter26Predictions(cls, queryTime, firstLetterOfQuery=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter26Predictions"
        params = {
            "queryTime": queryTime.to_json(),
            "firstLetterOfQuery": firstLetterOfQuery,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter27Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter27Predictions"
        params = {
            "queryTime": queryTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter28Predictions(cls, queryTime):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter28Predictions"
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
    def Chapter30Predictions(cls, queryTime, personsPresent=None, bodyPartTouched=None):
        """
        NO DESC FOUND!! ERROR
        :return: JObject
         """
        endpoint = "Chapter30Predictions"
        params = {
            "queryTime": queryTime.to_json(),
            "personsPresent": personsPresent,
            "bodyPartTouched": bodyPartTouched,
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def Chapter31Predictions(cls, queryTime, dreamDescription=None, isDaytimeDream=False, wasDreamForgotten=False, dreamBeforeMidnight=False, sleptAfterDream=False, hadGoodDreamAfterBad=False, yamaOfNight=0, isQuerentSick=False, querentBackground="ordinary"):
        """
        NO DESC FOUND!! ERROR
        :return: Task`1
         """
        endpoint = "Chapter31Predictions"
        params = {
            "queryTime": queryTime.to_json(),
            "dreamDescription": dreamDescription,
            "isDaytimeDream": isDaytimeDream,
            "wasDreamForgotten": wasDreamForgotten,
            "dreamBeforeMidnight": dreamBeforeMidnight,
            "sleptAfterDream": sleptAfterDream,
            "hadGoodDreamAfterBad": hadGoodDreamAfterBad,
            "yamaOfNight": yamaOfNight,
            "isQuerentSick": isQuerentSick,
            "querentBackground": querentBackground,
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
    def AIGenerateNames(cls, nameDescription, numberOfNames=20, excludeNames=None):
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


