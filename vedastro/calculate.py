# AUTO GENERATED ON 20:44 23/06/2026 +08:00
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
         Rectifies finds an unknown birth time using machine learning over physical and personality traits. Scans candidate time slices across the birth day and returns the TimeRange the model judges most consistent with the supplied appearance and temperament body heightshape hair lips nose complexion face shape constitution personality. Uses the RAMAN ayanamsa to match the trained rule set model and precision are configurable. 
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
         Allinone agentic entrypoint. Takes a plainEnglish query plus up to two Times a birth Time andor a checkcurrent Time semanticsearches the bestmatching Calculate methods autobinds their parameters invokes them in parallel and returns the results with metadata showing which methods were routed to and which Time each parameter was bound from. Replaces handpicking from 640 Calculate methods. Binding rules inside SmartInvokeAsync a methods FIRST Time parameter receives birthTime falling back to checkTime if birthTime is null a methods SECOND Time parameter receives checkTime falling back to birthTime. At least one of the two Times must be supplied if both are null the method returns an error JObject instead of throwing. 
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

    # NOTE: overload 'SearchEvents(TimebirthTime,TimestartTime,TimeendTime,List<EventTag>eventTagList,intprecisionHours)' not exposed - Python has no method
    #       overloading; the API resolves 'SearchEvents' to its first definition only.

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
         Returns the Vimshottari Dasa periods operating right now current system time at the birth location for the given birth chart nested down to the requested number of levels Maha Dasa Bhukti Antaram .... Handy for what planetary period am I in today. 
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
         Returns the Vimshottari Dasa periods operating at a specific moment for the given birth chart nested down to the requested number of levels Maha Dasa Bhukti Antaram .... 
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
         Returns the sequence of Vimshottari Dasa periods across a time range for the given birth chart sampling the range at the given precision and nesting down to the requested number of levels. Use this to build a Dasa timeline between two dates. 
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
         Returns the full Vimshottari Dasa timeline for an entire life starting at birth and scanning forward the given number of years nested down to the requested number of levels. A convenience wrapper over DasaAtRange covering birth to birth scanYears. 
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
         Same as DasaAtRange but returns the Dasa timeline as a compact JSON string instead of a JObject. Useful for callers that want the raw serialized payload directly. 
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
         Same as DasaForLife but returns the wholelife Dasa timeline as a compact JSON string instead of a JObject. Useful for callers that want the raw serialized payload directly. 
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
    def PredictMedicalHealthConditions(cls, birthTime):
        """
         Predicts a persons likely health conditions and bodily vulnerabilities from their birth chart. Computes the fundamental chart data once then maps afflicted and weak planets to the body parts and organs they rule to highlight areas of medical concern. Returns a structured report of predicted conditions grouped by organ and ruling planet based on Vedic medical astrology. 
        :return: JObject
         """
        endpoint = "PredictMedicalHealthConditions"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PlanetMotionName(cls, planetName, time):
        """
         Determines the motion state Gati of a planet according to classical Vedic astrology rules. The method uses different logic depending on the planet Sun and Moon are always treated as Sama or normal motion. Rahu and Ketu are always treated as Vakra or retrograde. Mars Jupiter and Saturn are classified by their sign distance from the Sun. Mercury and Venus are classified using Chesta Bala and actual motion speed. 
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
         Checks whether a planet aspects a specific house at the given time. The method gets all houses currently aspected by the planet checks whether the target house is included in that list. 
        :return: Boolean
         """
        endpoint = "IsPlanetAspectingHouse"
        params = {
            "planet": planet.value,
            "house": house.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'IsPlanetAspectingHouse(PlanetNameplanet,inthouseNumber,Timetime)' not exposed - Python has no method
    #       overloading; the API resolves 'IsPlanetAspectingHouse' to its first definition only.

    @classmethod
    def IsWaxingMoon(cls, birthTime):
        """
         Checks whether the Moon is in the waxing phase also called Shukla Paksha or the bright half of the lunar month. The method calculates the lunar day and checks whether its moon phase is BrightHalf. 
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
         Checks whether the Moon is in the waning phase also called Krishna Paksha or the dark half of the lunar month. The method calculates the lunar day and checks whether its moon phase is DarkHalf. 
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
         Returns the start time of the Vedic day containing the supplied time. A Vedic day begins at sunrise not at midnight. The method calculates sunrise for the supplied date returns that sunrise when the input time is after sunrise otherwise moves back roughly one day and returns the previous sunrise. 
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
         Calculates the total Kuja Dosha Manglik Dosha score for a chart. The method evaluates the dosha contribution of Mars Saturn Rahu Ketu Sun. It checks each planets house placement applies classical cancellation rules evaluates sign relationship and dignity then assigns a weighted score. The total score is the sum of all relevant planet scores. 
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
         Classifies a planet as benefic malefic or neutral for Kartari Yoga calculations. The method uses natural benefic and malefic groups then applies two special rules If both benefics and malefics are present with the planet the classification becomes neutral. Mercury is benefic when alone or with benefics but malefic when joined with any malefic. 
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
         Finds planets in Shubha Kartari Yoga meaning planets hemmed between benefic influences. For each planet the method finds the planets signbased house checks the 2nd and 12th houses from that planet classifies the planets in those surrounding houses returns the planet when benefics are present and no malefics are present. 
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
         Finds planets in Paapa Kartari Yoga meaning planets hemmed between malefic influences. For each planet the method finds the planets signbased house checks the 2nd and 12th houses from that planet classifies the planets in those surrounding houses returns the planet when malefics are present and no benefics are present. 
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
         Finds houses in Shubha Kartari Yoga meaning houses hemmed between benefic planets. For each house the method checks the adjacent 2nd and 12th houses classifies the planets found there and returns the house when benefics are present and malefics are absent. 
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
         Finds houses in Paapa Kartari Yoga meaning houses hemmed between malefic planets. For each house the method checks the adjacent 2nd and 12th houses classifies the planets found there and returns the house when malefics are present and benefics are absent. 
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
         Calculates the distance between a planets dispositor and each sign owned by that dispositor. The method finds the dispositor of the input planet gets the signs owned by that dispositor gets the dispositors current sign counts from each owned sign to the dispositors current sign. 
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
         Calculates the house distance of a planets dispositor from Lagna. The method finds the planets dispositor gets the Lagna sign gets the dispositors current sign and counts from Lagna to that sign. 
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
         Calculates the house distance of a planets dispositor from the Moon sign. The method finds the planets dispositor gets the Moon sign gets the dispositors current sign and counts from the Moon to that sign. 
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
         Returns all planets conjunct with the dispositor of the given planet. 
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
         Returns all planets aspecting the dispositor of the given planet. 
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
         Returns all houses owned by a planet at a given time. The method gets the zodiac signs ruled by the planet gets the sign assigned to every house using Bhava Chalit signs returns the houses whose signs are ruled by the input planet. 
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
         Finds the house that contains a given zodiac sign using Rasistyle house mapping. 
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
         Calculates the length of the daylight period in hours. The method subtracts sunrise time from sunset time for the supplied date and location. 
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
         Checks whether the supplied birth time occurs during the night period. Night is treated as the inverse of day birth. 
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
         Checks whether the supplied birth time occurs between sunrise and sunset. The method treats sunrise as included and sunset as excluded. 
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
         Checks the Ghataka Chakra for potentially harmful or adverse indicators at a given time. The method gets the natives birth Moon sign loads the Ghataka rule row for that Moon sign compares the current Moon sign Tithi group weekday Moon constellation and Lagna against that row returns the names of the matching harmful indicators. 
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
         Returns the planetary lord of a constellation Nakshatra. The method maps the 27 constellations to the standard repeating planetary ruler sequence Ketu Venus Sun Moon Mars Rahu Jupiter Saturn Mercury. 
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
         Checks whether a planet is currently in a water sign. The method gets the planets Rasi sign and tests whether that sign is Cancer Scorpio or Pisces. 
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
         Calculates the lunar day or Tithi from the angular distance between the Moon and Sun. The method gets the Nirayana longitudes of the Sun and Moon measures the forward MoonSun separation divides the separation by 12 rounds up to the next whole Tithi number. 
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
         Checks whether the supplied time falls in Shukla Paksha the bright or waxing half of the lunar month. 
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
         Returns the constellation occupied by a planet. The method gets the planets Nirayana longitude and maps that longitude to a constellation. 
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
         Gets the constellation behind a planet at a given time 
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
         Returns the Nakshatra that begins at the starting degree of a zodiac sign. The method converts the signs starting longitude into a constellation. 
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
         Returns the zodiac sign in which a Nakshatra begins. The method calculates the starting longitude of the constellation and maps that longitude to a zodiac sign. 
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
         Checks whether a planet is defeated in Graha Yuddha planetary war. The method applies the planetarywar rules documented in the source comments Only the five Tara Grahas can participate Mars Mercury Jupiter Venus Saturn Sun Moon Rahu and Ketu are excluded. A planetary war occurs only when two eligible planets are within 1 degree of each other. The planet with the lesser longitude is treated as the victor. The planet with the greater longitude is treated as defeated. A special wraparound check handles cases near the 0 360 boundary. 
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
         Calculates Tarabala the birthstar strength used in personal Muhurtha. The method gets the Moon constellation number at the selected time gets the persons birth Moon constellation number counts from the birth constellation to the current constellation reduces the count into the standard 9fold Tara cycle returns the Tara number and cycle. 
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
         Calculates Chandrabala the Moon strength used in personal Muhurtha. The method gets the Moon sign at the selected time gets the persons birth Moon sign counts from the birth Moon sign to the current Moon sign returns the resulting sign distance. 
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
         Returns the zodiac sign occupied by the Moon at the given time. The method calculates the Moons Rasi sign and returns only the sign name. 
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
         Returns the zodiac sign of the Lagna Ascendant at the given time. The method reads the sign of House 1 and returns only the sign name. 
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
         Calculates the Nithya Yoga for the given time. The method gets the Nirayana longitudes of the Sun and Moon adds them together normalizes the result to the zodiac circle divides the combined longitude by 800 minutes of arc rounds up to the next Yoga number returns the matching NithyaYoga. 
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
         Calculates the Karana which is half of a lunar day or Tithi. The method calculates the angular separation between the Moon and Sun converts that separation into a raw lunarday value determines the current Tithi checks whether the time is in the first or second half of the Tithi maps that position to the correct Karana. 
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
         Returns the zodiac sign occupied by the Sun at the given time. The method calculates the Suns Rasi sign and returns the full ZodiacSign including both sign name and degree within the sign. 
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
         Finds the approximate time when the Sun entered its current zodiac sign. The method starts from the supplied time identifies the Suns current sign scans backward in time reduces the scan step whenever it overshoots into the previous sign stops when the Sun is very close to the beginning of the current sign or when the accuracy limit is reached. 
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
         Finds the approximate time when the Sun will leave its current zodiac sign. The method starts from the supplied time identifies the Suns current sign scans forward in time reduces the scan step whenever it overshoots into the next sign stops when the Sun is very close to the end of the current sign or when the accuracy limit is reached. 
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
         Returns all planets located in a specific house using house longitude boundaries. The method gets all house longitude ranges selects the requested house gets the Nirayana longitude of all planets checks which planetary longitudes fall inside that houses range. 
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
         Returns all planets located in a specific house using signbased house mapping. The method gets the zodiac sign assigned to the requested house finds all planets currently occupying that sign returns the matching planets. 
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
         Returns all planets currently occupying a given zodiac sign. The method checks all nine planets and collects those whose Rasi sign matches the requested sign. 
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
         Returns the Nirayana longitudes of all nine planets at the given time. The method calculates and packages the longitude of Sun Moon Mars Mercury Jupiter Venus Saturn Ketu Rahu 
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
         Returns the Sayana fixedzodiac longitudes of all nine planets at the given time. The method calculates and packages the Sayana longitude for the same nineplanet set used by AllPlanetLongitude.... 
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
         Finds the house occupied by a planet using house longitude ranges. The method gets the planets Nirayana longitude loads all house longitude ranges checks which house range contains the planet returns that house. 
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
         Finds the house occupied by a planet using signbased house assignment. The method gets the planets Rasi sign gets the Rasi sign assigned to every house returns the house whose sign matches the planets sign. 
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
         Returns the longitudebased house placement of all nine planets. The method loops through all nine planets calculates each planets house using HousePlanetOccupiesBasedOnLongitudes... and stores the result in a dictionary. 
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
         Returns the lord of a house. The method gets the zodiac sign assigned to the requested house returns the planetary lord of that sign. 
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
         Returns the lord of the zodiac sign occupied by a planet. The method calculates the planets Nirayana longitude converts that longitude to a zodiac sign returns the lord of that sign. 
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
         Returns the lord of the constellation occupied by a planet. The method calculates the planets Nirayana longitude finds the constellation at that longitude returns the planetary lord of that constellation. 
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
         Returns the planetary lords for a list of houses. The method loops through each requested house calculates that houses lord using LordOfHouse... and adds the result to a return list. 
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
         Returns the constellation lord for every house at the given time. The method loops through all twelve houses finds the constellation at the middle longitude of each house gets the lord of that constellation stores the result in a dictionary keyed by house. 
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
         Returns the constellation lord of a specific house. The method gets the constellation at the middle longitude of the requested house and then returns that constellations planetary lord. 
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
         Returns the constellation located at the middle longitude of a house. The method gets all house longitude ranges finds the requested house reads the houses middle longitude converts that longitude into a Constellation. 
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
         Returns all planets occupying each house using signbased house placement. The method loops through every house finds the planets in that house using PlanetsInHouseBasedOnSign... and stores the result in a dictionary. 
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
         Counts forward from a starting zodiac sign and returns the sign reached after the requested count. For example this can answer questions like Which sign is the 4th from Cancer The starting sign is counted as 1. 
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
         Counts forward from the zodiac sign occupied by a planet and returns the sign reached after the requested count. For example this can answer questions like Which sign is the 4th from the Moon 
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
         Counts forward from the Lagna Ascendant sign and returns the sign reached after the requested count. This is a convenience wrapper around SignCountedFromInputSign.... 
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
         Counts forward from a starting house number and returns the house reached after the requested count. For example this can answer questions like Which house is the 4th from the 5th house The starting house is counted as 1. 
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
         Checks whether a planet is currently in a specific zodiac sign. The method calculates the planets Rasi sign at the given time and compares it with the requested sign. 
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
         Returns the zodiac signs aspected by a planet at the given time. The method begins from the planets current sign and applies the supported Vedic aspect rules all planets aspect the 7th sign from themselves Saturn additionally aspects the 3rd and 10th signs Jupiter additionally aspects the 5th and 9th signs Mars additionally aspects the 4th and 8th signs Maandi and Gulika additionally aspect the 2nd 7th and 12th signs from their sign of occupation. 
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
         Checks whether a planet is in its Moolatrikona zone. Moolatrikona is similar to exaltation but it applies to a sign range rather than only a single point. The method checks the planets sign and degree against the supported ranges Sun Leo 020 Moon Taurus 430 Mercury Virgo 1620 Jupiter Sagittarius 013 Mars Aries 018 Venus Libra 010 Saturn Aquarius 020 
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
         Returns all planets currently located in the requested zodiac sign. The method explicitly calculates the sign of each of the nine planets and adds every matching planet to the return list. 
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
         Returns the longitude data for a specific house. The method checks the cache gets all house longitudes selects the requested house returns the corresponding House object. 
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
         Calculates the Panchaka classification for a given time. The method gets the lunar day number gets the Moon constellation number gets the weekday number gets the rising sign number adds them together divides the total by 9 maps the remainder to a Panchaka name. 
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
         Returns the planetary lord of the weekday for a given time. The method first calculates the Vedic weekday and then maps it to its ruling planet. 
        :return: PlanetName
         """
        endpoint = "LordOfWeekday"
        params = {
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'LordOfWeekday(DayOfWeekweekday)' not exposed - Python has no method
    #       overloading; the API resolves 'LordOfWeekday' to its first definition only.

    @classmethod
    def IshtaKaala(cls, birthTime):
        """
         Calculates Ishta Kaala also known as Suryodayadi Jananakala Ghatika. This is the number of ghatis elapsed from sunrise to the moment of birth. The method checks whether the birth time is before sunrise uses the previous days sunrise when needed measures the time elapsed from the relevant sunrise converts hours into ghatis using the rule 1 hour 2.5 ghatis returns the result as an Angle. 
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
         Checks whether a given time occurs before sunrise on that same date and location. 
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
         Calculates which Hora of the Vedic day contains the supplied time. The method gets the birth time in local mean time gets sunrise for the current date uses the previous days sunrise if the time occurs before sunrise measures the hours elapsed since the relevant sunrise rounds up to the next whole Hora clamps the result to the range 124. 
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
         Calculates the sunrise time for the date and location of the supplied Time. The method checks the cache prepares Swiss Ephemeris risetransit parameters for the Sun starts the search from local midnight calculates sunrise using the configured geographic coordinates converts the Swiss Ephemeris Julian result back into the original standardtime offset returns the final Time. 
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
         Calculates the sunset time for the date and location of the supplied Time. The method follows the same Swiss Ephemeris risetransit pattern as SunriseTime... but requests the Suns setting time instead of rising time. 
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
         Returns the apparent noon for the date of the supplied time. The method converts the input time into local apparent time takes that apparent date creates a DateTime at 1200 PM preserves the DateTimeKind from the local apparent time. 
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
         Checks whether a planet is in a Trikona house from Lagna. The Trikona houses are 1st 5th 9th 
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
         Checks whether a planet is in a Kendra house from Lagna. The method checks only 4th house 7th house 10th house 
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
         Checks whether a planet is in an Upachaya house. The Upachaya houses are 3rd 6th 10th 11th 
        :return: Boolean
         """
        endpoint = "IsPlanetInUpachaya"
        params = {
            "planet": planet.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'IsPlanetInKendra(PlanetName[]planetList,Timetime)' not exposed - Python has no method
    #       overloading; the API resolves 'IsPlanetInKendra' to its first definition only.

    @classmethod
    def IsPlanetInKendraFromPlanet(cls, kendraFrom, kendraTo, time):
        """
         Checks whether one planet is in a Kendra position from another planet. The method counts the sign distance between the two planets checks whether the distance is one of the Kendra positions 1 4 7 10 
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
         Counts the zodiacsign distance from one planet to another. The method gets the Rasi sign of the starting planet gets the Rasi sign of the ending planet counts inclusively from the starting sign to the ending sign. 
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
         Checks whether the lord of one house is located in another specified house using longitudebased house placement. The method finds the lord of lordHouse finds which house that lord occupies using house longitude boundaries compares the occupied house with the requested occupiedHouse. 
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
         Checks whether the lord of one house is located in another specified house using signbased house placement. The method finds the lord of lordHouse finds which house that lord occupies by sign compares the result with occupiedHouse. 
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
         Calculates the Arudha Lagna sign. The method follows the source rule find the Janma Lagna sign find the sign occupied by the Lagna lord count from the Lagna sign to the Lagna lords sign count the same distance again from the Lagna lords sign return the resulting sign as the Arudha Lagna. 
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
         Counts inclusively from one zodiac sign to another. For example counting from Aquarius to Taurus returns 4 Aquarius Pisces Aries Taurus. 
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
         Counts inclusively from one constellation to another. The method reads the constellation number of the start and end constellations counts forward through the 27constellation cycle wraps around when the end constellation is earlier in the sequence. 
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
         Checks whether a planet is in a specified house using longitudebased house boundaries. The method calculates the planets house through HousePlanetOccupiesBasedOnLongitudes... and compares it with the requested house. 
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
         Checks whether a planet is in a specified house using signbased house placement. The method calculates the planets house through HousePlanetOccupiesBasedOnSign... and compares it with the requested house. 
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
         Checks whether a planet falls inside a house using a KPstyle cusp boundary method. The method reads the cusp longitude for the requested house compares the planets Nirayana longitude with the current and next cusp handles wraparound when the next cusp longitude is numerically smaller than the current cusp returns whether the planet falls inside that cusp interval. 
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
         Checks whether every planet in a supplied list is in the same requested house. The method tests each planet using signbased house placement and returns false as soon as one planet is outside the requested house. 
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
         Checks whether at least one planet in a supplied list is in the requested house. The method tests each planet using signbased house placement and returns true as soon as one match is found. 
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
         Checks whether a planet is at its exact debilitation degree. The method gets the planets Nirayana longitude converts it into a zodiac sign and degree gets the planets debilitation point compares both the sign and wholedegree position. 
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
         Checks whether a planet is at its exact exaltation degree. The method gets the planets Nirayana longitude converts it into a zodiac sign and degree gets the planets exaltation point compares both the sign and wholedegree position. 
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
         Checks whether a planet is anywhere in its exaltation sign. The method calculates the planets Rasi sign gets the planets exaltation point compares only the sign names. 
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
         Checks whether the Moon is at the fullmoon Tithi for the supplied time. The method calculates the lunar day and returns true when the lunarday number is 15. 
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
         Checks whether the Moon is at the newmoon Tithi for the supplied time. The method calculates the lunar day and returns true when the lunarday number is 1 or 0. 
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
         Checks whether a zodiac sign is treated as Nara Rasi or a human sign. The implementation returns true for Gemini Virgo Libra Aquarius Sagittarius 
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
         Checks whether a zodiac sign belongs to the water element. Water signs are Cancer Scorpio Pisces 
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
         Checks whether a zodiac sign belongs to the fire element. Fire signs are Aries Leo Sagittarius 
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
         Checks whether a zodiac sign belongs to the earth element. Earth signs are Taurus Virgo Capricorn 
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
         Checks whether a zodiac sign belongs to the air element. Air signs are Gemini Libra Aquarius 
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
         Checks whether a planet is a Yogakaraka for the charts Lagna. The method gets the Lagna sign applies a fixed LagnatoYogakaraka lookup table returns whether the supplied planet appears in that favorable list. 
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
         Checks whether a planet is a Maraka for the charts Lagna. The method gets the Lagna sign applies a fixed LagnatoMaraka lookup table returns whether the supplied planet appears in that Maraka list. 
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
         Checks whether a planet is placed in a house whose sign it owns. The method excludes Rahu and Ketu finds the planets current house using signbased placement checks the planets relationship to that house returns true when the relationship is OwnVarga. 
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
         Checks whether a planet aspects any house that it owns. The method excludes Rahu and Ketu gets all houses currently aspected by the planet checks the lord of each aspected house returns true if any aspected house is ruled by the planet itself. 
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
         Checks whether a planet is placed in its own sign. The method uses the same relationship check as IsPlanetInOwnHouse... excludes Rahu and Ketu finds the planets signbased house checks whether the planets relationship with that house is OwnVarga. 
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
         Checks whether a planet is placed in a friendly sign. The method gets the planets current Rasi sign determines the relationship between the planet and that sign returns true for FriendVarga or BestFriendVarga. 
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
         Checks whether a planet is placed in an enemy sign. The method gets the planets current Rasi sign determines the relationship between the planet and that sign returns true for EnemyVarga or BitterEnemyVarga. 
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
         Checks whether a planet is in a house whose sign is ruled by an enemy. The method excludes Rahu and Ketu finds the planets signbased house determines the planets relationship to that house returns true for EnemyVarga or BitterEnemyVarga. 
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
         Checks whether a planet is in a house whose sign is ruled by a friend. The method excludes Rahu and Ketu finds the planets signbased house determines the planets relationship to that house returns true for FriendVarga or BestFriendVarga. 
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
         Calculates the natives birth Varna from the Moon sign. The method gets the Moons Rasi sign at birth maps that sign to one of the traditional Varna groups returns the matching Varna. 
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
         Returns all planets located in a sign counted from a reference planet. The method finds the sign that is the requested count from startPlanet returns all planets currently occupying that sign. 
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
         Returns all planets located in a sign counted from the Lagna Ascendant. The method finds the sign that is the requested count from Lagna returns all planets in that sign. 
        :return: List`1
         """
        endpoint = "AllPlanetsInASignFromLagna"
        params = {
            "signsFromLagna": signsFromLagna,
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'AllPlanetsSignsFromPlanet(int[]signsFromList,PlanetNamestartPlanet,TimebirthTime)' not exposed - Python has no method
    #       overloading; the API resolves 'AllPlanetsSignsFromPlanet' to its first definition only.

    # NOTE: overload 'AllPlanetsSignsFromPlanet(int[]signsFromList,TimebirthTime,PlanetNamestartPlanet)' not exposed - Python has no method
    #       overloading; the API resolves 'AllPlanetsSignsFromPlanet' to its first definition only.

    # NOTE: overload 'AllPlanetsSignsFromPlanet(intsignsFromMoon,TimebirthTime,PlanetNamestartPlanet)' not exposed - Python has no method
    #       overloading; the API resolves 'AllPlanetsSignsFromPlanet' to its first definition only.

    @classmethod
    def AllPlanetsInSignsFromLagna(cls, signsFromList, birthTime):
        """
         Returns all planets located in any of several signs counted from Lagna. The method loops through the requested sign counts gathers planets from each counted sign removes duplicate planets returns the final list. 
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
         Checks whether any planet from a supplied list is located in any of the requested signs counted from a reference planet. The method gathers all planets found in the counted signs from startPlanet checks whether any of those planets appear in planetList returns true on the first match. 
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
         Checks whether any planet from a supplied list is located in any of the requested signs counted from Lagna. The method gathers all planets found in the counted signs from Lagna checks whether any of those planets appear in planetList returns true on the first match. 
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
         Returns the Nirayana middle longitudes of the twelve houses using Swiss Ephemeris. The method gets the chart location converts the time to Julian Universal Time sets the sidereal ayanamsa mode calculates house cusps using Swiss Ephemeris returns the cusp array. 
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
         Calculates and returns the full longitude ranges for all twelve houses. The method checks the cache gets the house cusp data derives the angular house points constructs House objects containing beginning middle and ending longitudes returns the complete list. 
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
         Returns all planets in conjunction with a given planet. The method sets an 8degree conjunction orb gets the longitude of the input planet gets the longitudes of all nine planets excludes the input planet itself adds every planet within the conjunction orb. 
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
         Returns the target planets signbased house if the target is meaningfully connected to the reference planet. The method checks two possible connections whether the target is in a Kendra from the reference planet whether the target aspects the reference planet. If either condition is true the targets signbased house is returned. Otherwise the default HouseName value is returned. 
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
         Checks whether a planet is in a Drekkana whose lord is friendly to that planet. The method finds the planets D3 Drekkana sign gets the lord of that Drekkana sign calculates the combined planettoplanet relationship returns true when the relationship is Friend or BestFriend. 
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
         Checks whether a planet is Vargottama. A planet is treated as Vargottama when it occupies the same zodiac sign in the Rasi chart D1 and the Navamsha chart D9. 
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
         Calculates the Arudha of a given house. The method gets the sign of the input house finds the lord of that house gets the sign occupied by the house lord counts from the house sign to the lords sign counts the same distance again from the lords sign converts the resulting sign back into a house. 
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
         Checks whether a planet has attained Gopura Amsha Gopuramsa. The method excludes Rahu and Ketu checks the planets sign in several divisional charts counts how many times each sign appears returns true if any sign appears in at least four of those divisional placements. The divisional charts checked are D1 Rasi D2 Hora D3 Drekkana D7 Saptamsha D9 Navamsha D12 Dwadashamsha D30 Trimshamsha 
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
         Builds a prioritized list of potential Maraka planets for the chart. The method groups planets into rough strength tiers Strong Marakas planets occupying the 2nd and 7th houses. Medium Marakas lords of the 2nd and 7th houses planets conjunct those lords Sun or Venus when they are Kendra lords. Weak Marakas fallback planets conjunct the 12th lord fallback lords of the 3rd and 8th houses if no stronger candidates are found. The final list is assembled in priority order and deduplicated. 
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
         Checks whether a Navamsha sign is considered cruel. The method returns true for signs ruled by Mars or Saturn Aries Scorpio Capricorn Aquarius 
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
         Checks whether any classical Balarishta cancellation or exception is present in the birth chart. The method tests multiple protective combinations including Moon full exalted Vargottama or in a friendly sign strong Lagna lord in Kendra with benefic support and no malefic aspect Jupiter Venus or Mercury in Kendra without malefic aspects Rahu in the 3rd 6th or 11th house strong Jupiter in Kendra specific daynight and Paksha conditions involving the Moon Lagna lord in Kendra or Trikona benefics in Kendras strong Moon in favorable house positions strong natural benefic influence on Lagna. 
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
         Returns the lagnaspecific malefic planets that aspect a given planet. The method gets the list of malefic planets for the charts Lagna filters that list to only planets aspecting receivingAspect returns the matching planets. 
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
         Checks whether a planet receives any aspect from lagnaspecific malefic planets. The method delegates to MaleficPlanetsAspectingPlanet... and returns whether any matching aspect exists. 
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
         Checks whether a planet is in its exaltation sign. The method gets the planets current Rasi sign looks up the planets classical exaltation sign compares the two signs. 
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
         Checks whether Mercury is malefic for the specific Lagna at the given time. The method requires both conditions to be true Mercury must be a malefic lord for the current Lagna. Mercury must be afflicted by association with malefics. 
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
         Gets the nutation value from Swiss Ephemeris for the supplied time. The method converts the time to Julian Day in UT calls Swiss Ephemeris with SE_ECL_NUT returns the nutationrelated value stored in the result array. 
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
         Converts a tropical ascendant degree into an ARMC value. The method is intended to calculate right ascension calculate declination derive oblique ascension convert that into ARMC based on the ascendant quadrant. 
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
         Returns the ayanamsa value for the supplied time. The method checks the cache uses a manual Raman ayanamsa calculation when Ayanamsa is set to Raman otherwise retrieves the ayanamsa from Swiss Ephemeris. 
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
         Returns a planets Sayana tropical longitude at the supplied time. The method checks the cache converts the time to Julian Ephemeris Time maps the VedAstro planet name to a Swiss Ephemeris planet ID calculates the tropical longitude using Swiss Ephemeris adjusts Ketu by adding 180 to Rahus longitude. 
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
         Returns a planets Nirayana sidereal longitude at the supplied time. The method checks the cache handles Upagrahas separately by routing to their special longitude methods uses the manual Raman path when the selected ayanamsa is Raman otherwise uses Swiss Ephemeris sidereal calculation adjusts Ketu by adding 180 to Rahus longitude where needed. 
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
         Finds the next lunar eclipse after the supplied time. The method checks the cache converts the time to Julian form asks Swiss Ephemeris to search forward for the next lunar eclipse reads the time of maximum eclipse from the result array converts that Julian value back into a normal UTC DateTime. 
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
         Finds the next solar eclipse after the supplied time and returns the global UTC time of maximum eclipse. The method checks the cache converts the input time to Julian time asks Swiss Ephemeris to search forward for the next solar eclipse reads the maximum eclipse time from the result array converts that Julian result back into a normal UTC DateTime. 
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
         Returns a planets raw ephemeris longitude from Swiss Ephemeris. The method acts as a lowerlevel bridge between VedAstro planet names and Swiss Ephemeris planet IDs. It calculates the requested planets longitude at the given time and returns it as an Angle. 
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
         Returns a planets Sayana tropical latitude at the supplied time. The method checks the cache converts the time to Julian Ephemeris Time maps the planet to a Swiss Ephemeris planet ID calculates the planets tropical position returns the latitude component as an Angle. 
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
         Returns the planets longitudinal speed at the supplied time. The method checks the cache converts the time to Julian Ephemeris Time calls Swiss Ephemeris with speed flags enabled returns the longitudespeed component from the result. 
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
         Returns the constellation located at a given zodiac longitude. The method normalizes the longitude into the zodiac circle divides it by one Nakshatra span of 1320 rounds up to the constellation number builds and returns the corresponding Constellation. 
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
         Returns the zodiac sign and degreeinsign for a given longitude. The method normalizes the longitude divides the zodiac circle into 30degree signs determines the sign number calculates the degree position inside that sign returns a ZodiacSign. 
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
         Converts a ZodiacSign object back into an absolute zodiac longitude. The method takes the sign number multiplies the sign offset by 30 adds the degree within the sign returns the result as an Angle. 
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
         Returns the Vedic weekday for the supplied time. The method bases the weekday on the Vedic day calculation rather than simply using the civil midnightbased date. 
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
         Returns the planetary lord of a given Hora number for a supplied weekday. The method uses a fixed 24Hora lookup table for each weekday. The first Hora is ruled by the lord of the weekday and the sequence continues through the classical planetary Hora order. 
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
         Returns the planetary lord of the Hora active at the supplied time. The method calculates the Vedic weekday calculates the Hora number at the time looks up the Hora lord using LordOfHoraFromWeekday.... 
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
         Calculates the junction point between two house longitudes. The method finds the midpoint between a previous and next house longitude normalizes the result to the 360degree circle and returns it as an Angle. 
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
         Returns the planetary lord of a zodiac sign. The method maps each sign to its classical ruler Aries Scorpio Mars Taurus Libra Venus Gemini Virgo Mercury Cancer Moon Leo Sun Sagittarius Pisces Jupiter Capricorn Aquarius Saturn 
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
         Returns all zodiac signs ruled by a planet. The method maps the standard planetary rulers to their signs and also includes mappings for supported Upagrahas where defined in the source. 
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
         Returns the zodiac sign immediately after the supplied sign. The method advances one sign forward and wraps from Pisces back to Aries. 
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
         Returns the next house number after the supplied house. The method checks the cache increments the house number wraps from 12 back to 1. 
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
         Returns the classical exaltation point for a planet. The result includes both the exaltation sign the exact exaltation degree inside that sign. 
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
         Returns the classical debilitation point for a planet. The result includes both the debilitation sign the exact debilitation degree inside that sign. 
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
         Checks whether a zodiac sign is evennumbered. Even signs are Taurus Cancer Virgo Scorpio Capricorn Pisces 
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
         Checks whether a zodiac sign is oddnumbered. Odd signs are Aries Gemini Leo Libra Sagittarius Aquarius 
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
         Checks whether a zodiac sign is fixed. Fixed signs are Taurus Leo Scorpio Aquarius 
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
         Checks whether a zodiac sign is movable. Movable signs are Aries Cancer Libra Capricorn 
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
         Checks whether a zodiac sign is common dual. Common signs are Gemini Virgo Sagittarius Pisces 
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
         Returns the permanent natural relationship between two planets. The method uses fixed classical friendship neutrality and enmity tables for the seven classical planets. 
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
         Converts a Julian Day value into a normal UTC DateTime. The method checks the cache uses Swiss Ephemeris to convert Julian UT into calendar date parts builds a DateTime from those parts. 
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
         Converts a Julian Day value at Greenwich into a DateTimeOffset. The method checks the cache converts the Julian Day into date and time components using Swiss Ephemeris creates a DateTime wraps it in a DateTimeOffset with a 0000 offset. 
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
         Converts the input times Local Mean Time into Greenwichbased Julian Day format. The method gets the input time as LMT converts it to universal time extracts the UTC date and fractional hour calls Swiss Ephemeris swe_julday.... 
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
         Converts the supplied Time from Local Mean Time to UTC. The method returns the input times LMT DateTimeOffset converted to universal time. 
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
         Returns the complete list of functional malefic planets for the charts Lagna. The method delegates to MaleficPlanetListForLagna... which includes lagnaspecific malefic lordship conditional Moon behavior conditional Mercury behavior Rahu and Ketu as malefics. 
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
         Checks whether a planet is conjunct with any functional malefic planet for the charts Lagna. The method gets the lagnaspecific malefic planet list gets the planets conjunct the input planet returns whether any conjunct planet appears in the malefic list. 
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
         Returns all functional malefic planets that aspect the specified planet. The method gets the complete malefic list for the charts Lagna checks which of those malefics aspect the input planet returns the matching planets. 
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
         Checks whether a planet is malefic for the charts specific Lagna. This method is a naming alias that delegates to the comprehensive lagnaspecific malefic check IsPlanetMaleficForLagna.... 
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
         Checks whether Mercury is afflicted by malefic association. This method is an alias for IsMercuryAfflictedByMalefics... retained to match naming patterns used elsewhere in the codebase. 
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
         Checks whether a planet is benefic for the charts specific Lagna. This method is a naming alias that delegates to the complete benefic check IsPlanetBenefic.... 
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
         Checks whether a planet is a functional or temporal malefic for the charts Lagna. The method delegates to IsPlanetMaleficForLagna... which includes lagnaspecific house lordship waning Moon logic afflicted Mercury logic Rahu and Ketu as malefics. 
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
         Checks whether any lagnaspecific malefic planet aspects a given house. The method gets the complete malefic planet list for the charts Lagna checks whether any of those planets aspect the requested house returns the result. 
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
         Checks whether a planet is a natural malefic. The implementation treats the following planets as natural malefics Mars Saturn Rahu Ketu 
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
         Returns the fixed list of natural malefic planets. The returned list contains Mars Saturn Rahu Ketu 
        :return: List`1
         """
        endpoint = "NaturalMaleficPlanetList"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def PapaGrahasList(cls, time):
        """
         Returns the list of Papa Grahas used for Shadbala and physicalaffliction calculations. The method always includes Sun Mars Saturn Rahu Ketu It conditionally adds Moon when the Moon is not benefic Mercury when Mercury is afflicted by malefics. 
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
         Checks whether a planet is a natural benefic. The implementation treats the following planets as natural benefics Jupiter Venus 
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
         Returns the fixed list of natural benefic planets. The returned list contains Jupiter Venus 
        :return: List`1
         """
        endpoint = "NaturalBeneficPlanetList"
        params = {
        }
        return cls._make_request(endpoint, params)

    @classmethod
    def SubhaGrahasList(cls, time):
        """
         Returns the list of Subha Grahas used for benefic strength and aspect calculations. The method always includes Jupiter Venus It conditionally adds Moon when the Moon is benefic Mercury when Mercury is not afflicted by malefics. 
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
         Returns the complete list of planets that are malefic for the charts specific Lagna. The method checks the seven classical planets against lagnaspecific malefic lordship treats Moon as malefic only when it is both malefic for the Lagna and not benefic by lunar phase treats Mercury as malefic only when it is both malefic for the Lagna and afflicted by malefics always includes Rahu and Ketu. 
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
         Returns the list of planets considered physically harmful through aspects conjunctions combustionlike influence or harsh rays. The method delegates directly to PapaGrahasList.... 
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
         Checks whether a planet appears in the complete lagnaspecific malefic list. The method simply tests whether MaleficPlanetListForLagna... contains the requested planet. 
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
         Checks whether a planet appears in the physically harmful planet list. The method delegates to PhysicallyHarmfulPlanetList.... 
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
         Checks whether a planet is a benefic lord for the charts Lagna based on fixed Lagnaspecific lordship rules. The method determines the Lagna sign applies the corresponding B. V. Ramanstyle beneficlord table returns whether the planet is listed as favorable for that Lagna. 
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
         Checks whether a planet is a malefic lord for the charts Lagna based on fixed Lagnaspecific lordship rules. The method determines the Lagna sign applies the corresponding B. V. Ramanstyle maleficlord table returns whether the planet is listed as unfavorable for that Lagna. 
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
         Checks whether a planet is neutral for the charts Lagna. The method determines the Lagna sign applies a fixed Lagnaspecific neutralplanet table returns whether the planet is listed as neutral. 
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
         Checks whether Mercury is afflicted through conjunction with malefic planets. The method checks whether Mercury is conjunct with any relevant malefic returns true immediately if such a conjunction exists checks whether Mercury is conjunct with benefics returns false if Mercury is protected by benefic association returns false when Mercury is not conjunct any planet. 
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
         Checks whether the Moon is benefic based on its lunarday position. The method calculates the lunar day number returns true when the lunar day falls from 8 through 23 returns false otherwise. 
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
         Returns the complete list of planets that are benefic for the charts Lagna. The method checks the seven classical planets against benefic lordship treats Moon as benefic only when it is both benefic for the Lagna and benefic by lunar phase treats Mercury as benefic only when it is both benefic for the Lagna and not afflicted by malefics excludes planets that are neutral or conditionally unfavorable. 
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
         Checks whether a planet appears in the complete lagnaspecific benefic list. The method delegates to BeneficPlanetList... and checks whether the requested planet is included. 
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
         Checks whether all lagnaspecific malefic planets are placed in Upachaya houses. The method gets the complete malefic list for the charts Lagna checks each planets house placement returns false if any malefic is outside an Upachaya house returns true only when all malefics are in Upachayas. 
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
         Returns all lagnaspecific malefic planets located in a given sign. The method gets all planets in the requested sign gets the complete malefic list for the charts Lagna returns only the planets that appear in both lists. 
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
         Checks whether any lagnaspecific malefic planet is located in a given sign. The method delegates to MaleficPlanetListInSign... and checks whether the result contains any planets. 
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
         Returns all physically harmful planets that aspect a given house. The method gets the physically harmful planet list checks which of those planets aspect the requested house returns the matching planets. 
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
         Checks whether any physically harmful planet aspects a given house. The method delegates to PhysicallyHarmfulPlanetsAspectingHouse... and checks whether any matching planets exist. 
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
         Returns all physically harmful planets that aspect a specified planet. The method gets the physically harmful planet list checks which harmful planets aspect the target planet returns the matching planets. 
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
         Checks whether a planet receives an aspect from any physically harmful planet. The method delegates to AllPhysicallyHarmfulPlanetsAspecting... and returns whether that list is nonempty. 
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
         Returns all physically harmful planets conjunct with a specified planet. The method gets all planets conjunct with the input planet gets the physically harmful planet list returns the conjunct planets that also appear in the harmful list. 
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
         Checks whether a planet is conjunct with any physically harmful planet. The method delegates to AllPhysicallyHarmfulPlanetsConjunctWith... and returns whether that list contains any matching planets. 
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
         Checks whether any lagnaspecific malefic planet occupies a given house. The method gets all planets in the requested house using signbased placement gets the complete malefic list for the charts Lagna checks whether any planet in the house appears in that malefic list. 
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
         Checks whether a planet is hemmed between malefic planets. The method finds the planets signbased house identifies the previous and next houses checks whether both adjacent houses contain lagnaspecific malefics. 
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
         Checks whether a planet is placed in a sign ruled by a benefic planet. The method gets the planets current Rasi sign finds the lord of that sign checks whether that sign lord is benefic for the chart. 
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
         Checks whether a planet is weak by the two simple conditions used in this helper. The method returns true if the planet is either debilitated or combust. 
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
         Performs an enhanced affliction check for a planet. The method treats a planet as afflicted when any of the following are true the planet is combust except for the Sun the planet is debilitated the planet is in an enemy sign the planet is aspected by a natural malefic the planet is aspected by the Sun the planet is aspected by a planet with an enemy or bitterenemy relationship the planet is conjunct with a natural malefic the planet is conjunct with the Sun the planet is conjunct with a planet that has an enemy or bitterenemy relationship. 
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
         Checks whether a planet is afflicted specifically by a supplied list of damaging planets. For each damaging planet the method verifies the damaging planet is not the afflicted planet itself the damaging planet is either in the same signbased house or aspecting the afflicted planet the damaging planet is harmful by one of these standards natural malefic Sun enemy or bitterenemy relationship. If any damaging planet fails the required conditions the method returns false. 
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
         Returns the planets that are temporary friends of a given planet based on sign position. The method gets the planets current sign identifies the signs in the 2nd 3rd 4th 10th 11th and 12th positions from it collects planets placed in those signs removes Rahu and Ketu from the result. 
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
         Checks whether one planet casts a good aspect onto another planet. The method confirms that the transmitting planet aspects the receiving planet calculates the combined relationship between the two planets returns true only when the relationship is Friend or BestFriend. 
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
         Returns all planets casting bad aspects onto a given planet. The method gets all planets aspecting the receiving planet automatically includes natural malefics for all other planets checks whether the combined relationship is enemy or bitter enemy returns the resulting badaspect list. 
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
         Checks whether a planet is receiving any bad aspects. The method delegates to AllPlanetsInBadAspectToPlanet... and returns whether any bad aspectors are found. 
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
         Checks whether a planet casts a good aspect onto a house. The method confirms that the transmitting planet aspects the requested house evaluates the planets relationship to the house sign returns true when the relationship is own varga friend varga best friend varga. 
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
         Returns all planets casting bad aspects onto a house. The method gets all planets aspecting the requested house automatically includes natural malefics for all other planets checks the relationship between the planet and the house sign returns planets whose aspect is harmful by nature or relationship. 
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
         Checks whether a house receives any bad aspects. The method delegates to AllPlanetsInBadAspectToHouse... and checks whether the returned list is nonempty. 
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
         Checks whether any lagnaspecific benefic planet is present in selected signs counted from a reference planet. The method gets the complete benefic planet list for the chart checks the requested counted signs from the reference planet returns whether any benefic appears there. 
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
         Checks whether any lagnaspecific benefic planet is present in selected signs counted from Lagna. The method gets the complete benefic planet list for the chart checks the requested counted signs from the Ascendant returns whether any benefic appears there. 
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
         Checks whether both the Sun and Moon are sufficiently strong and receive netbenefic aspect influence. The method requires both conditions Sun and Moon must each have positive Drik Bala. Sun and Moon must meet minimum Shadbala Pinda thresholds Sun must be at least 5 rupas or 300 shashtiamsas Moon must be at least 6 rupas or 360 shashtiamsas. 
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
         Checks whether any lagnaspecific benefic planet is placed in a Kendra house. The method gets the complete benefic planet list checks whether any benefic is in a Kendra returns true on the first match. 
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
         Returns all lagnaspecific benefic planets located in a given sign. The method gets all planets in the requested sign gets the complete benefic list for the chart returns the intersection of those two lists. 
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
         Checks whether any lagnaspecific benefic planet is located in a given sign. The method delegates to BeneficPlanetListInSign.... 
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
         Returns all lagnaspecific benefic planets aspecting a given house. The method gets the complete benefic planet list filters it to planets aspecting the requested house. 
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
         Checks whether any lagnaspecific benefic planet aspects a given house. The method delegates to BeneficPlanetsAspectingHouse.... 
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
         Returns all lagnaspecific benefic planets aspecting a given planet. The method gets the complete benefic planet list filters it to planets aspecting the requested planet. 
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
         Checks whether a planet receives an aspect from any lagnaspecific benefic planet. The method delegates to BeneficPlanetsAspectingPlanet.... 
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
         Checks whether a planet receives an aspect from any planet that is an enemy by combined relationship. The method gets all planets aspecting the input planet evaluates each aspecting planets combined relationship to the input planet returns true if any aspecting planet is an enemy or bitter enemy. 
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
         Checks whether a planet receives an aspect from any planet that is friendly by combined relationship. The method gets all planets aspecting the input planet evaluates each aspecting planets combined relationship to the input planet returns true if any aspecting planet is a friend or best friend. 
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
         Returns all planets conjunct with the input planet that are enemies by combined relationship. The method gets all planets conjunct with the input planet evaluates each conjunct planets combined relationship to the input planet returns planets whose relationship is enemy or bitter enemy. 
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
         Checks whether a planet is conjunct with any enemy planet. The method delegates to AllPlanetsInEnemyConjunctionWith.... 
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
         Returns all planets conjunct with the input planet that are friends by combined relationship. The method gets all planets conjunct with the input planet evaluates each conjunct planets combined relationship to the input planet returns planets whose relationship is friend or best friend. 
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
         Checks whether a planet is conjunct with any friendly planet. The method delegates to AllPlanetsInFriendConjunctionWith.... 
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
         Checks whether any complete lagnaspecific benefic planet occupies a given house. The method gets all planets in the requested house using signbased placement gets the complete benefic planet list for the chart checks whether any planet in the house appears in that benefic list. 
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
         Returns a planets relationship to a zodiac sign based on the planets relationship with that signs lord. The method excludes Rahu and Ketu from the calculation gets the lord of the requested sign returns OwnVarga when the planet itself rules the sign otherwise calculates the combined relationship between the planet and the sign lord converts that planettoplanet relationship into a planettosign relationship. 
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
         Calculates the combined relationship between two planets by merging permanent and temporary relationships. The method excludes Rahu and Ketu from the calculation returns SamePlanet when both inputs are the same gets the permanent natural relationship gets the temporary positional relationship combines them according to the classical relationship table. 
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
         Returns a planets relationship with a house based on the sign occupying that house. The method gets the zodiac sign assigned to the house evaluates the planets relationship to that sign returns the resulting planettosign relationship. 
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
         Returns the temporary relationship between two planets based on their relative sign positions. The method returns SamePlanet when both inputs are the same gets the temporary friend list of the main planet returns Friend if the secondary planet is in that list otherwise returns Enemy. 
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
         Checks whether a planet is fortified meaning strong and well supported. The method requires the planet to be strong by Shadbala either excellent placement or beneficial support no active affliction. Excellent placement means the planet is in its own sign exalted or in Moolatrikona. Beneficial support means the planet has benefic aspects or benefic conjunctions. 
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
         Returns all planets that receive aspects from the input planet. The method calculates the signs aspected by the input planet finds all planets located in those signs returns the combined planet list. 
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
         Calculates the aspect strength or aspect value between two planets. The method calculates the longitudinal difference from the transmitting planet to the receiving planet normalizes the difference to the zodiac circle calculates the basic Drishti value adds any special Vishesha Drishti value for Mars Jupiter or Saturn returns the final aspect value. 
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
         Returns all planets that aspect a given planet. The method checks all nine planets and keeps those for which IsPlanetAspectedByPlanet... returns true. 
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
         Returns all houses aspected by a planet. The method calculates the signs aspected by the planet checks the sign assigned to each house returns the houses whose signs are included in the aspectedsign list. 
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
         Returns all planets that aspect a given house. The method loops through all nine planets gets the houses aspected by each planet adds planets whose aspectedhouse list contains the requested house. 
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
         Checks whether one planet aspects another planet. The method gets all planets aspected by the transmitting planet checks whether the receiving planet appears in that list. 
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
         Checks whether a planet aspects a given house. The method gets all houses aspected by the transmitting planet checks whether the requested house appears in that list. 
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
         Checks whether two planets are conjunct. The method gets the conjunction list for planetA gets the conjunction list for planetB confirms that each planet appears in the others conjunction list. 
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
         Returns all natural benefic planets that are in genuinely beneficial conjunction with the input planet. The method requires both conditions the conjunct planet must be a natural benefic in the current context the conjunct planet must have a friendly or bestfriend relationship with the input planet. The natural benefic set starts with Jupiter Venus. It conditionally adds Moon when the Moon is benefic Mercury when Mercury is not afflicted. 
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
         Checks whether a planet is conjunct with any natural benefic that also has a beneficial relationship to it. The method delegates to AllBeneficPlanetsInGoodConjunctionWith.... 
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
         Returns all planets that form genuinely harmful conjunctions with the input planet. The method gets the physically harmful planet list checks which harmful planets are conjunct with the input planet always counts natural malefics as harmful checks relationship for Sun weak Moon and afflicted Mercury includes those conditional harmful planets only when their relationship is enemy or bitter enemy. 
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
         Checks whether a planet receives any harmful conjunctions. The method delegates to AllHarmfulPlanetsInBadConjunctionWith.... 
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
         Converts a planets Shadbala strength into a relative percentage score. The method calculates the strength of all planets finds the strength of the requested planet identifies the weakest and strongest planet values remaps the requested planets strength onto a 0100 scale. 
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
         Selects the strongest planet from a supplied list based on Shadbala. The method returns immediately if the list contains only one planet calculates Shadbala strength for each planet selects the planet with the highest strength value. 
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
         Returns all nine planets ordered by Shadbala strength strongest first. The method checks the cache calculates Shadbala Pinda for every planet sorts the planets by descending strength returns only the planet names. 
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
         Checks whether a planet meets its classical minimum Shadbala threshold. The method compares the planets Shadbala Pinda in Rupas against a planetspecific threshold Sun 5 Moon 6 Mars 5 Mercury 7 Jupiter 6.5 Venus 5.5 Saturn 5 Rahu 5 Ketu 5 
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
         Checks whether a house belongs to the strongest third of all houses by housestrength score. The method delegates to HouseStrengthCategory.... 
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
         Checks whether a house belongs to the weakest third of all houses by housestrength score. The method delegates to HouseStrengthCategory.... 
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
         Classifies a houses strength relative to the other houses in the same chart. The method calculates the strength of all twelve houses sorts the houses by strength splits the list into three tiers bottom third Weak middle third Average top third Strong returns the category for the requested house. 
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
         Returns the Shadbala strength of all nine planets. The method calculates PlanetShadbalaPinda... for each planet and returns a list of strengthandplanet tuples. 
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
         Returns all houses ordered by strength strongest first. The method checks the cache calculates strength for every house sorts by descending strength returns only the house names. 
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
         Calculates the final total Shadbala Pinda for a planet. The method adds the six main planetary strength components Sthana Bala positional strength Dig Bala directional strength Kala Bala temporal strength Chesta Bala motional strength Naisargika Bala natural strength Drik Bala aspect strength added or subtracted depending on sign For Rahu and Ketu the method uses the strength of the lord of the house occupied by the node. 
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
         Alias for PlanetShadbalaPinda.... This method exists as a simpler easiertoremember name for retrieving a planets total Shadbala strength. 
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
         Calculates Drik Bala the aspect strength of a planet. The method excludes Rahu and Ketu loops through the seven classical planets calculates the angular distance from each aspecting planet to the target calculates the basic Drishti value adds special Vishesha Drishti for Mars Jupiter or Saturn treats Mercury as benefic for Drik Bala treats other planets as positive or negative depending on benefic status divides the accumulated Drishti Pinda by 4. 
        :return: Shashtiamsa
         """
        endpoint = "PlanetDrikBala"
        params = {
            "target": target.value,
            "time": time.to_json(),
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'DistanceBetweenPlanets(Anglea,Angleb)' not exposed - Python has no method
    #       overloading; the API resolves 'DistanceBetweenPlanets' to its first definition only.

    @classmethod
    def FindViseshaDrishti(cls, dk, p):
        """
         Calculates the special aspect value Vishesha Drishti for Mars Jupiter or Saturn. The method checks the angular distance dk and applies additional specialaspect strength when the planet is Saturn special strength over the 3rd and 10th aspect zones. Jupiter special strength over the 5th and 9th aspect zones. Mars special strength over the 4th and 8th aspect zones. 
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
         Calculates the ordinary Drishti or aspect value from an angular distance. The method maps different angular ranges to different aspectstrength formulas. This produces a graduated aspect value rather than a simple yesorno aspect. 
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
         Returns the planets Naisargika Bala or natural strength. Naisargika Bala is the inherent brightnessbased strength of a planet. In this implementation the values are fixed constants Sun 60 Moon 51.43 Venus 42.85 Jupiter 34.28 Mercury 25.70 Mars 17.14 Saturn 8.57 
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
         Calculates Chesta Bala the motional strength of a planet. The method supports three different calculation paths Sun and Moon Normally return zero. When useSpecialSunMoon is true special IshtaKashta formulas are used. Rahu and Ketu Return zero in this implementation. Mars Mercury Jupiter Venus and Saturn Use the mean longitude true longitude and Seeghrochcha aphelionstyle value. The resulting Chesta Kendra is folded into a 0180 range. The final Chesta Bala is calculated by dividing by 3. 
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
         Calculates the mean longitudes of planets from the interval between the epoch and the birth date. The method estimates where each planet would be if it moved at a uniform mean rate without applying orbital corrections. 
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
         Calculates the number of days between the configured epoch and the supplied chart time. The method converts the time into the needed date representation and returns the day interval used by meanmotion calculations. 
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
         Checks whether a planet is retrograde at the supplied time. The method handles special fixed cases calculates the planets speed or motion condition returns whether the planet is moving in reverse zodiacal direction. 
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
         Determines whether a planet is combust because it is too close to the Sun. The method excludes planets that are not evaluated for combustion in this implementation gets the longitudes of the planet and Sun calculates the shortest angular distance between them compares that distance against the planetspecific combustion limit. 
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
         Returns the circulation or orbital period used by Chesta Bala support calculations. 
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
         Calculates Saptavargaja Bala the strength a planet receives from its dignity across seven divisional placements. The method evaluates the planets condition in the following charts Rasi Hora Drekkana Saptamsha Navamsha Dwadashamsha Trimshamsha For each divisional placement strength is assigned according to whether the planet is in a favorable neutral own exalted or hostile placement. 
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
         Calculates Sthana Bala the positional strength of a planet. The method combines the major subcomponents of positional strength Ochcha Bala exaltation strength. Saptavargaja Bala dignity across seven divisions. Ojayugmarasyamsa Bala oddeven sign and Navamsha strength. Kendra Bala strength from Kendra Panapara or Apoklima placement. Drekkana Bala strength from position in the correct Drekkana for the planets gender class. 
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
         Calculates Drekkana Bala a positionalstrength component based on where a planet falls within a sign. The method follows these rules Masculine planets receive strength in the first Drekkana 010. Hermaphrodite planets receive strength in the second Drekkana 1020. Feminine planets receive strength in the third Drekkana 2030. 
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
         Calculates Kendra Bala the strength a planet receives from its house category. The method assigns strength based on the planets house placement Kendras 1 4 7 10 60 Panaparas 2 5 8 11 30 Apoklimas 3 6 9 12 15 
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
         Calculates Ojayugmarasyamsa Bala strength from oddeven placement in Rasi and Navamsha. The method checks whether the planet is in the sign parity favored by its class Sun Mars Jupiter Mercury and Saturn gain strength in odd signs. Moon and Venus gain strength in even signs. The same idea is applied to both Rasi and Navamsha positions. 
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
         Calculates Kala Bala the temporal strength of a planet. The method combines several timebased substrengths including Nathonnatha Bala Paksha Bala Tribhaga Bala Abda Bala Masa Bala Vara Bala Hora Bala Ayana Bala Yuddha Bala 
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
         Calculates Yuddha Bala the strength adjustment from planetary war. The method checks whether the target planet is eligible for Graha Yuddha searches for nearby eligible planets within the war threshold determines the victorious and defeated planets calculates the strength difference using prewar Kala Bala values adjusts the result according to the planetarywar rule. 
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
         Calculates Ayana Bala the strength based on a planets declination and northern or southern course. The method gets the planets declination applies the planetspecific northsouth rule scales the result into Shashtiamsas. 
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
         Calculates the declination of a planet. Declination is the planets angular distance north or south of the celestial equator. The method gets the planets ecliptic position uses obliquity of the ecliptic converts the ecliptic position into declination. 
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
         Returns the true obliquity of the ecliptic for the supplied time. The method gets the obliquity value through Swiss Ephemeris including nutation effects where available. 
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
         Calculates Hora Bala also called Horadhipathi Bala. The method awards strength when the planet is the lord of the Hora active at the supplied time. 
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
         Calculates Abda Bala the yearly lord strength. The method awards strength to the planet that rules the year of birth. 
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
         Calculates Masa Bala the monthly lord strength. The method awards strength to the planet that rules the month of birth. 
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
         Calculates Vara Bala the weekday lord strength. The method awards strength to the planet that rules the day of birth. 
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
         Calculates the lords of the year and month for the supplied time. The method uses the day interval from the epoch and derives the year and month lord according to the counting logic used by the Kala Bala calculations. 
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
         Calculates Tribhaga Bala strength from the onethird division of day or night. The method follows these rules During the day Mercury gains strength in the first third. Sun gains strength in the second third. Saturn gains strength in the third third. During the night Moon gains strength in the first third. Venus gains strength in the second third. Mars gains strength in the third third. Jupiter always receives full Tribhaga Bala. 
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
         Calculates Ochcha Bala the planets exaltation strength. The method gets the planets current longitude gets the planets debilitation point measures the angular distance from the debilitation point folds the result into the shortest valid arc when needed divides the distance by 3. 
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
         Calculates Paksha Bala strength based on the Moons phase. The method measures the angular distance between the Moon and Sun derives separate base values for Subha and Papa planets classifies the Moon by waxing or waning phase classifies Mercury by whether it is malefic applies the appropriate base value to the requested planet doubles the Moons Paksha Bala. 
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
         Calculates Nathonnatha Bala also called Divaratri Bala. The method returns full strength for Mercury converts the birth time to local apparent time finds apparent noon measures the distance from apparent noon converts that distance into ghatis applies dayplanet or nightplanet rules. Planet groups Sun Jupiter and Venus gain day strength. Moon Mars and Saturn gain night strength. Mercury always receives 60. 
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
         Calculates Dig Bala the directional strength of a planet. The method assigns each planet a direction of maximum strength Jupiter and Mercury House 1 Sun and Mars House 10 Saturn House 7 Moon and Venus House 4 It then finds the opposite powerless house measures the shortest arc from the planet to that powerlesshouse midpoint divides the arc by 3 to get the Shashtiamsa value. 
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
         Calculates the total Bhava Bala or house strength for a specific house. The method combines three housestrength components Bhavadhipathi Bala strength of the house lord. Bhava Dig Bala directional or signtype strength of the house. Bhava Drishti Bala aspect strength received by the house. The method calculates each component for all houses adds the three values together for each house and returns the total strength of the requested house. 
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
         Calculates Bhava Drishti Bala the aspect strength received by each house. The method determines whether each of the seven classical planets contributes a positive or negative influence treats Mercury as a full benefic for this specific Bhava Drishti Bala calculation calculates each planets aspect value toward every house midpoint adds special aspect strength where applicable reduces the aspect value for planets other than Jupiter and Mercury combines all planetary contributions into one score per house. 
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
         Calculates Bhava Dig Bala the strength a house receives based on the type of sign containing its midpoint. The method checks the midpoint longitude of every house maps that midpoint into a sign group applies the corresponding directional subtraction rule folds large differences back into the 06 range multiplies the final difference by 10. 
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
         Calculates Bhavadhipathi Bala the strength contributed by the lord of each house. For every house the method finds the lord of the house calculates that planets total Shadbala Pinda uses the planets Shadbala as the houselord strength. 
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
         Returns planets whose Shadbala strength is above a supplied threshold. The method calculates the strength of all planets checks each planets strength value returns planets whose strength is greater than threshold. 
        :return: List`1
         """
        endpoint = "BeneficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'BeneficPlanetListByShadbala(TimepersonBirthTime)' not exposed - Python has no method
    #       overloading; the API resolves 'BeneficPlanetListByShadbala' to its first definition only.

    @classmethod
    def BeneficHouseListByShadbala(cls, personBirthTime, threshold):
        """
         Returns houses whose total house strength is above a supplied threshold. The method calculates HouseStrength... for every house compares each house strength against the threshold returns houses whose strength is greater than the threshold. 
        :return: List`1
         """
        endpoint = "BeneficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'BeneficHouseListByShadbala(TimepersonBirthTime)' not exposed - Python has no method
    #       overloading; the API resolves 'BeneficHouseListByShadbala' to its first definition only.

    @classmethod
    def MaleficPlanetListByShadbala(cls, personBirthTime, threshold):
        """
         Returns planets whose Shadbala strength is below a supplied threshold. The method calculates the strength of all planets checks each planets strength value returns planets whose strength is less than threshold. 
        :return: List`1
         """
        endpoint = "MaleficPlanetListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'MaleficPlanetListByShadbala(TimepersonBirthTime)' not exposed - Python has no method
    #       overloading; the API resolves 'MaleficPlanetListByShadbala' to its first definition only.

    @classmethod
    def MaleficHouseListByShadbala(cls, personBirthTime, threshold):
        """
         Returns houses whose total house strength is below a supplied threshold. The method calculates HouseStrength... for every house compares each house strength against the threshold returns houses whose strength is less than the threshold. 
        :return: List`1
         """
        endpoint = "MaleficHouseListByShadbala"
        params = {
            "personBirthTime": personBirthTime.to_json(),
            "threshold": threshold,
        }
        return cls._make_request(endpoint, params)

    # NOTE: overload 'MaleficHouseListByShadbala(TimepersonBirthTime)' not exposed - Python has no method
    #       overloading; the API resolves 'MaleficHouseListByShadbala' to its first definition only.

    @classmethod
    def ResidentialStrength(cls, planetName, time):
        """
         Calculates the residential strength of a planet inside the house it occupies. The method finds the planets house using longitudebased house boundaries gets the beginning middle and end longitudes of that house gets the planets actual longitude determines whether the planet lies in the first half or second half of the house returns a proportional strength value based on its position within that half. 
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
         Converts a planets Ishta and Kashta scores into a compact beneficversusmalefic scale. The method calculates the planets Ishta score calculates the planets Kashta score compares the two scores as a percentage of total strength maps the result from 100..100 into a final 4..4 range rounds the final value to three decimal places. 
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
         Calculates Kashta Phala the difficult or unfavorable strength of a planet. The method returns 0 for Rahu and Ketu calculates the planets Ochcha Bala calculates the planets Chesta Bala using the special SunMoon path subtracts both values from 60 multiplies the adjusted values returns the square root of that product. 
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
         Calculates Ishta Phala the favorable or beneficial strength of a planet. The method returns 0 for Rahu and Ketu calculates the planets Ochcha Bala calculates the planets Chesta Bala using the special SunMoon path multiplies those two values returns the square root of the product. 
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
         Earthquakes generally occur at the times of eclipses p.66 rule 1 p.61 p.6871 Eclipse proximity is one of the most frequently cited indicators in the book. Solar eclipse Sun near RahuKetu near New Moon Lunar eclipse Sun near RahuKetu near Full Moon. Charts Argentina 1887 annular solar eclipse on 22nd Manila 1887 total lunar eclipse June 1 Java 1882 annular solar eclipse Nov 10 Japan 1923 lunar eclipse Aug 26 Iran 1978. 
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
         The most important feature is again the closeness of the Moon and Mercury p.65 EXACT conjunction within 3 degrees strongest form of MoonMercury indicator. Appears in virtually every major earthquake chart in BV Ramans study. Charts China 1976 p.65 Assam 1950 p.72 Agadir 1960 p.74 Iran 1990 p.80. 
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
         Jupiter and Saturn are in opposite signs p.73 Assam earthquake 1950 JupiterSaturn opposition is associated with the strongest earthquakes. 
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
         Two of the worst earthquakes occurred in 1960 perhaps due to JupiterSaturn remaining in the same sign p.73 
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
         Earthquakes generally occur at the times of eclipses and near new Moon days p.66 New Moon Amavasya lunar day 30 or 1. Checks within 3 tithis. Charts Bihar 1934 Chart 1 China 1976 Chart 2 Agadir 1960 Chart 9 Iran 1990 Chart 14. 
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
         Earthquakes generally occur near full Moon days p.66 Full Moon Purnima lunar day 15. Checks within 3 tithis. Chart Iran 1978 Chart 13 occurred just after full Moon p.79. 
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
         Not only were the major planets Saturn and Mars in mutual angles p.67 SaturnMars in Kendras is a classic earthquake indicator. Kendras houses 1 4 7 10 from each other. Charts Calcutta 1737 Chart 3 Java 1882 Chart 6. 
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
         Jupiter and Mars are in mutual square Kendra China 1976 p.65 Mars and Jupiter are in mutual trines Assam 1950 p.73 Jupiter and Mars are in square Iran 1978 p.79 Iran 1990 p.80 MarsJupiter angular relationship is cited in MORE earthquake charts than SaturnMars. 
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
         The most important feature is again the closeness of the Moon and Mercury p.65 MoonMercury conjunction appears in nearly every earthquake chart in the book. Wider orb version within 10 degrees for general conjunction tracking. 
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
         The major planets Mars Saturn Rahu and Jupiter will be in mutual angles Kendras or trines Trikonas p.66 rule 3 Checks if at least 3 of these 4 major planets are in KendraTrikona from each other. 
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
         Except Jupiter and RahuKetu the rest were all clustered within an arc of 38 p.65 Checks if 5 planets fall within a 40degree arc. China 1976. 
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
         Major planets generally occupy earthy signs p.66 rule 5 Earthy signs Taurus Virgo Capricorn. Threshold 2 of Mars Saturn Rahu Jupiter in earthy signs lowered from 3 per audit. 
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
         Major planets generally occupy airy signs p.66 rule 5 Airy signs Gemini Libra Aquarius. Seven bodies are disposed in mutual Trikona Rasis in airy signs p.68 Threshold 2 of Mars Saturn Rahu Jupiter in airy signs lowered from 3 per audit. 
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
         The asterism of the day belongs to Prithvi Earth Mandala p.66 rule 6 Using BV Ramans Indra Mandala nakshatras p.28 which he associates with terrestrial disturbances fear from fire poverty crops fail. Nakshatras Rohini Anuradha Jyeshta Uttarashadha Sravana Dhanishta. 
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
         The asterism of the day belongs to Vayu Wind Mandala p.66 rule 6 Vayu Mandala nakshatras per BV Raman p.28 fear from kings storms and scarcity. Nakshatras Aswini Mrigasira Punarvasu Uttara Hasta Chitta Swathi. 
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
         At the times of severe earthquakes Jupiter is placed in an angle Kendra from the rising sign at the time of the earthquake occurrence p.59 Jupiter in houses 1 4 7 or 10 from the ascendant. NOTE Locationdependent requires geographic location for ascendant calculation. 
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
         Moon was in perigee Manila 1887 p.69 Moon was near perigee Assam 1950 p.73. Moon at perigee closest to Earth amplifies gravitational stress on tectonic plates. Moons average daily motion is 13.2 degday. At perigee it exceeds 14.5 degday. Uses Moons speed as a proxy for perigee proximity. 
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
         Mars was exactly in the 10th house Japan 1923 p.71 Both Jupiter and Saturn are near the lower meridian Persia 1960 p.75 The locality is indicated in places where Saturn or Jupiter is on the meridian p.62 Checks if Saturn Mars or Jupiter are in houses 4 or 10 meridiannadir. NOTE Locationdependent requires geographic location for house calculation. 
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
         Mercury is in conjunction with both the Moon and Saturn Assam 1950 p.73 MercurySaturn conjunction appears alongside MoonMercury in several earthquake charts. Orb of 15 degrees since Saturn moves slowly. 
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
         Calculates weighted earthquake risk score 035 scale. Weight 3 Critical max 12 points Eclipse MoonMercury exact JupiterSaturn aspect Weight 2 Strong max 14 points NewFull Moon planetary Kendras clustering Weight 1 Supporting max 9 points Sign positions nakshatras Moon perigee Based on frequency of appearance in BV Ramans 200 historical earthquake charts. Maximum possible score 35 if every indicator fires simultaneously. In practice scores above 12 are extremely rare. Risk levels Score 8 HIGH RISK critical mass of indicators Score 47 MODERATE RISK several supporting indicators Score 03 LOW RISK few or no indicators 
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
         Computes the Ashtamangala Number used in cowrieshell Ashtamangala Prasna divination. Supports both the original 108shell system and the reduced 9shell system selected by totalShells turning the three counted piles of shells into a threedigit number whose digits each range 1 to 8. The resulting number feeds Chapter7Predictions for interpretation. 
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
         Chapter5Predictions Prasna Marga Chapter V Mathematical Foundations SOURCE Prasna Marga Chapter V Stanzas 1750 WHAT THIS METHOD COMPUTES 1. Trisphuta Stanza 17 Lagna Moon Gulika 2. Chatusphuta Stanza 18 Trisphuta Sun 3. Panchasphuta Stanza 18 Chatusphuta Rahu 4. Pranasphuta Stanza 19 Lagna 5 Gulika primary 5. Dehasphuta Stanza 19 Moon 8 Gulika primary 6. Mrityusphuta Stanza 19 Gulika 7 Sun primary 7. Alt. Pranasphuta Stanza 2022 ghatibased research method 8. Alt. Mrityu Stanza 23 ghati weekdayoffset method 9. Kalasphuta Stanza 23 same as above subtracted 10. Sukshma TrisphutaStanza 4647 Prana Deha Mrityu summed 11. PranaDehaMrityu x9 method Stanza 44 12. Arudha Sphuta Stanza 32 Arudha Rasi start Lagna degrees 13. Stanza 48 sphuta prasna vighatikas 6 562 Gulika 14. Trisphuta Navamsa disease onset Stanza 38 15. Mrityu Nakshatra from Trisphuta Stanza 41 ALL INTERPRETIVE RULES covered Stanzas 2830 3134 CancerScorpioPisces trouble Samhara zone Stanzas 3738 planetary diseases from Trisphuta signNavamsa Stanza 40 evilgood indicators around Trisphuta Stanzas 4143 Mrityu Nakshatra SunMoon transit Panchasphuta death test Stanza 44 x9 PranaDehaMrityu aspect check Stanza 45 Navamsa triad LagnaMoonGulika Navamsas Stanza 46 Sukshma Trisphuta who is greater Mrityu in deadly nakshatra Stanza 47 planets in Sukshma Trisphuta sign family danger Stanzas 4849 additional death tests Stanza 50 longevity Srishti factors 
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
         Comprehensive Ashtamangala algorithm found in Chapter 7 of Prasna Marga returns all prediction steps and factors with Janma Rasi and Nakshatra derived from the birth time. 
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
         Chapter 8 Effects of Arudha and Related Factors Prasna Marga Comprehensive implementation covering stanzas 165 Analyzes Arudha Avasthas PranaDehaMrityu RahuChakra KalaHora Chandra Navamsa Chandra Kriya 
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
         Prasna Marga Chapter 9 Longevity Determination Ayur Prasna Integrates horary and natal chart methods for assessing life span. Classifies life into Alpayus short 032 yrs Madhyayus medium 3264 yrs or Purnayus long 64100 yrs via Yogayus yogabased and Dasayus Dasabased systems. Per Stanza 3 Longevity must be examined FIRST before all other predictions. 
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
         Prasna Marga Chapter 10 Timing Death Implements Maraka planet identification DasaAntardasa evil periods Kalachakra Dasa junctions Niryana deathtransit Rasis for SaturnJupiterSunMoon Pramana Gulika Ashtakavarga selection of the critical Niryana Rasi Marana Lagna deathdealing ascendant and Prasnabased timing of death. ETHICAL NOTE This chapter identifies windows of elevated risk not certainties. Use only when directly relevant hospitalised patient welfare assessment of missing person and never volunteer death predictions unsolicited. A multilayer convergence of Dasa transit Ashtakavarga and Prasna factors is the only basis for a strong conclusion. Disagreement among layers indicates danger present but not conclusive. 
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
         Generates Prasna Marga Chapter 11 predictions on the nature and cause of death. Analyses the 8th house the 22nd Drekkana lord the Navamsa of Mandi Gulika signbased Doshas organ correlations and environmental omens at the query time to describe the likely nature cause and circumstances of death. Source Prasna Marga Chapter XI. 
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
         Prasna Marga Chapter 12 Diagnosis and Classification of Diseases Roga Prasna SOURCE Prasna Marga Chapter XII Stanzas 179 WHAT THIS METHOD COMPUTES BLOCK 1 General Health Status Stanzas 15 77 Malefics in houses other than 3 and 11 indicate disease planets in 6 8 12 identify the specific affliction. BLOCK 2 Disease Classification Nija vs Agantuka Stanzas 1824 Nija Sarirotha bodily VataPittaKaphaSannipatha Chittotha mental 5th8th lord relationship Agantuka Drishtanimittaja 6th house curses falls Adrishtanimittaja evil spirits Badhaka BLOCK 3 Tridosha Determination Stanzas 4 1015 Which humour is afflicted per the dustha planet. Two systems Varahamihira Stanza 4 and Sarasangraha Stanza 11. BLOCK 4 Dhatu Body Tissue Affected Stanzas 3 16 Sunbone Moonblood Marsmuscle Mercuryskin Jupiterfat Venusspermovum Saturnnerves. BLOCK 5 Season of Disease Onset Stanza 12 Each planet rules a Ritu disease appears in the season of the dustha planet Venusspring SunMarssummer Moonrainy Mercuryautumn Jupiterfall Saturnwinter. BLOCK 6 Dietary Remedies Six Tastes Shadrasas Stanzas 2729 MadhuraAmlaLavana remove Vata ThikthaUshnaKashaya remove Kapha Pitta is destroyed by Madhura Thiktha Kashaya. BLOCK 7 Madness Unmada Stanzas 3132 4649 Eight classical yogas for lunacy causes by house analysis treatment notes. BLOCK 8 Epilepsy Apasmara Stanzas 5057 Saturn in 8th malefics in trines SunMars in 12th twelve classical forms enumerated. BLOCK 9 Bhakta Virodha Anorexia Stanza 63 Malefics aspect Lagna Saturn aspects 8th weak 8th lord. BLOCK 10 Diabetes Madhumeha Stanza 64 Malefics aspect Lagna Lagna lord debilitatedenemy Venus occupies or aspects 8th. BLOCK 11 Diseases by Dustha Planet Stanzas 6774 Full classical catalogue per planet Sun through Gulika. BLOCK 12 Specific Planetary Combinations Stanza 75 Saturn in 10th GulikaRahu in Lagna8th Mars positions etc. BLOCK 13 Body Part Organ Affected Stanza 78 Limbs typified by signs aspected or occupied by malefics. 
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
         Prasna Marga Chapter 13 Timing of Illness Onset and Recovery Roga Kala Prasna SOURCE Prasna Marga Chapter XIII Stanzas 139 WHAT THIS METHOD COMPUTES BLOCK 1 ONSET NAKSHATRAS Stanzas 13 89 Stanza 1 Onset nakshatra from MoonLagna nakshatra distance method Stanza 2 Onset nakshatras from Mandi 9 Mandi 12 MoonMandi Stanza 3 Onset via mostmalefic planet transiting the sign of the querys first letter Stanza 8 Day vs. night onset lordoccupant of 6th diurnal vs. nocturnal Stanza 9 Duration in months three calculation methods via 6th lord BLOCK 2 DIRECTION OF ILLNESS Stanzas 46 Stanza 4 Direction faced by querent place of first attack Stanza 5 Direction number from East yamas from sunrise when illness began Stanza 6 Number of companions number of attendants at the sickbed BLOCK 3 DISEASE DURATION FROM 6TH LORD Stanza 7 Expired portion of 6th lords sign half long illness half near recovery BLOCK 4 RECOVERY INDICATORS Stanzas 1015 2728 Stanza 10 Disease began when Moon was in sign of 6th lord recovery when Moon enters 4th lords sign Stanza 11 Last malefic affliction of LagnalordMoon onset benefic contact recovery Stanza 12 Moon entering Lagna Rasi Navamsa Dwadasamsa Gulikas sign subsidence Stanza 13 Ashtama Rasi nakshatras relief after Moon exits that group Stanza 15 Worst dustha planets sign onset best sustha planets sign recovery Stanza 27 Full Moon in Lagna with Jupiter JupiterVenus in Kendras recovery Stanza 28 Moon in Upachayas with benefics in good places or Lagna aspected by benefics recovery BLOCK 5 RECOVERY TIMELINE BY ONSET NAKSHATRA Stanzas 1617 Specific recovery windows days mapped to each of the 27 onset nakshatras BLOCK 6 DEATH INDICATORS Stanzas 1822 Stanza 18 Fatal combo AshtamiParvaRiktha malefic weekday trijanmaVipatPratyakNaidhana Stanzas 1920 Soola Chakra fatal worsening recovery zones around Suns nakshatra Stanza 21 All coincident factors death certain Stanza 22 Child formula for patients under 12 Janmaonset distance 3 4 BLOCK 7 RECOVERY SPEED AND DIFFICULTY Stanzas 2324 Stanza 23 6th lord speed and sign quality fast or slow recovery Stanza 24 Malefichemmed Lagna weak lord waning Moon in 6812 prolonged or fatal BLOCK 8 CAUSES AND REMEDIES Stanzas 2639 Stanza 26 Two root causes Drishta physical and Adrishta karmic Stanza 29 Diseases as pastbirth karma remedy medicine gifts japa homa worship Stanzas 3135 Deity wrath from malefics in anishta places Karma Vipaka remedies Stanzas 3639 Mrityunjaya Homa universal panacea 8000 Japa for severe illness summary
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
         Generates Prasna Marga Chapter 14 predictions on house interpretation and the timing of events. Synthesises houselord and karaka dispositions allbhava strength bhava ruin periods the effects of malefics and benefics in each house Gulika and tertiaryplanet effects event fructification timing karma analysis and imprisonment indicators. Source Prasna Marga Chapter XIV. 
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
         Prasna Marga Chapter 15 Causes of Misery and Remedial Measures SOURCE Prasna Marga Chapter XV Stanzas 1120 OVERVIEW This chapter identifies the eleven root causes of human suffering and provides a complete diagnostic and remedial framework. WHAT THIS METHOD COMPUTES BLOCK 1 KARMA NATURE Stanzas 13 Jupiters disposition favorable or unfavorable destiny. Eleven enumerated causes of misery. BLOCK 2 PLANETARY DEITY MAPPINGS Stanzas 47 Which deity is signified by each planetsignDrekkana SunShivaSubrahmanyaGanesha MoonDurgaBhadrakaliChamundi MarsSubrahmanyaBhairava or ChamundiBhadrakali MercuryVishnu AvatarasKrishna JupiterVishnu VenusAnnapoornaLakshmiYakshi SaturnSasthaKiratha RahuSerpent God. SatwicRajasicTamasic nature of deity determined from sign. BLOCK 3 BADHAKA HOUSE OF HARM Stanzas 110112 Movable Lagna 11th house is Badhakasthana. Fixed Lagna 9th house is Badhakasthana. Common Lagna 7th house is Badhakasthana. BLOCK 4 IDENTIFY THE ANGRY PLANET Stanzas 89 Lord of Badhakasthana in a dusthana 6812 primary angry planet. Angry planets deity the offended deity. BLOCK 5 KARMA SOURCE NATURE DIAGNOSIS Stanzas 101105 Reference point for evil Karma Benefics in 6812 malefics in kendrastrines from Chatra Rasi divine wrath. Same from Arudha Brahmins curse. Same from Moon enemy black magic. Same from Lagna peoples hatred. Dridha deliberate vs Adridha accidental Karma indicator in Moons sign Dridha. Karma type malefic in 5th mental 2nd verbal 10th bodily. BLOCK 6 TEMPLE IDOL CONDITION Stanzas 1011 Malefic in 12th from angry planet idol disfigured. GulikaRahu joining idol polluted by Dundubha. Saturn joining temple worn outpolluted. Mars joining temple guards in dissension. Angry planet in Lagna Mars idol broken Saturn idol dirty. Angry planet in 4th house temple very old needs repairs. BLOCK 7 PALLIATIVES BY ANGRY PLANETS HOUSE POSITION Stanzas 1214 1stPratibimbadana 2ndJapa 3rdPuja 4thTemple construction 5thSantarpana feeding 6thPratheekara Bali 7thDivine dance Nrithya 8thBali 9thDevopasana 10thDantiskandha 11thTarpana 12thno harm. Also angry planet in MarsSun signs illumination MoonVenus signs milkgheepayasa Mercury sign sandal paste Jupiter sign garlands Saturn sign ornamentsdress. Badhaka in 8th10th pujaBali 12th musicdrums. BLOCK 8 PLANETSPECIFIC REMEDIES Stanzas 1518 Sun angry Devaradhana divine worship. Moon angry Sankabhisheka free ricewater distribution. Mars angry illumination and havanas. Mercury angry dance before deity. Jupiter angry homas and feeding Brahmins. Venus angry liberal feeding of all. Saturn angry feeding of backwardpoor classes. BLOCK 9 FAVORED DEITY NEGLECTED WORSHIP Stanza 19 Planet with benefic in Lagna favoring deity. Lord of 9th in harm house neglected worship. BLOCK 10 MISAPPROPRIATION OF DEITYS PROPERTY Stanzas 2021 Lord of harm house in 2nd or 11th misappropriation. Lagna movable Dhatu minerals taken fixed Moola plantsland common Jeeva living beings. BLOCK 11 INTENSITY OF DEITYS WRATH Stanzas 2830 Lord of harm in 4th or lord of 4th in harm house or crosssign occupancy active wrath. Sun Moon in harm house anger of family deities. BLOCK 12 ANGER OF THE SERPENT GOD Stanzas 3132 38 Jupiter as lord of harm in 6812 in kendras of Rahu superior serpents angry. Jupiter in kendras of Gulika inferior serpents. Rahu in harm house serpent trouble with Sun good serpents with Moon bad ones. Rahu remedies by house 6810harm Sarpa Bali 4th Chitra Kuta stone 12th singing Lagna milk siddhapayasa 7th devotional music. Gulika alone in Rahus kendra serpent abodes unclean. Saturn Gulika in kendras purify surroundings with trees and rites. BLOCK 13 PARENTAL CURSES Stanzas 3940 SunMoon in harm house in Mars signNavamsa fathersmothers curse. Malefic in LeoCancer in unfavorable house same. Evil planet in harm house Jupiters sign BrahminDeva curse Purva Sapa. Harm house Leo or Sun present ancestors curse Mars as evil planet very intense. BLOCK 14 CURSES OF ELDERS AND PRECEPTORS Stanza 41 Lord of 6th in 9th OR lord of 9th in 12th fatherpreceptorelder displeased. Sun in 6th or conjoining 6th lord fathers displeasure. Moon similarly mothers displeasure. BLOCK 15 TROUBLES FROM GHOSTS PRETAS Stanzas 4250 Gulika in harm house ghost trouble. Gulika Mars connection unnatural death fireweaponsdisease. Gulika Saturn died in miserypenury abroad. Gulika Rahu serpent bite death. Gulika evil in watery sign drowned. Sex of Preta from oddeven sign and Navamsa of Gulika. Caste of Preta from sign lords caste. Remedy Shraddhas kshetra pindas tilavahana feeding Brahmins. BLOCK 16 EVIL EYE DRISHTI BADHA Stanzas 5154 115120 Lord of harm aspecting Lagna or lord of Lagna Drishti Badha. Lord of 7th in harm house or lords mutually joinedaspecting Drishti Badha. Movable Lagna evil in Lagna Mars in 7th affliction from Devatas. Nonbenefics in Lagna Saturn in 7th Moon aspected by malefics Pisachas. Intent of Devata harm lord friendly with Lagna lord enjoyment inimical destruction neutral eatingdrinking. BLOCK 17 SPIRITS CATALOGUE Stanzas 6065 18 Mahagrahas Amara Asura Naga Yaksha Gandharva Rakshasa Heydra Kasmala Nistheja Bhasmaka Pitris Krisa Vinayaka Pralapa Pisacha Anthyaja Yonija Bhuta. 9 Laghu Grahas Apasmara Brahmana Brahma Rakshasa Kshatriya Vaisya Sudra Neecha Chandala Vyanthara. All originated from anger of Rudra categories Bali Kama Rati Kama Hanthu Kama. BLOCK 18 OVERALL SYNTHESIS AND RECOMMENDED REMEDIES 
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
         Prasna Marga Chapter 16 Miscellaneous Queries Final Chapter of Part I SOURCE Prasna Marga Chapter XVI Stanzas 1125 WHAT THIS METHOD COMPUTES BLOCK 1 WHEREABOUTS OF THE QUERIST Stanzas 17 Arudha Lagna sign quality movablefixedcommon distance from home Navamsa of Arudha Lagna living conditions of the absent person Planets in Arudha aspects what they encountered on the journey BLOCK 2 BRIGHT AND DARK FUTURE Stanzas 810 LibraPisces births beneficsmalefics in 6 houses from 4th future 6 houses from 10th past AriesVirgo births houses 410 past houses 104 future BLOCK 3 FOUR MEANS OF ACHIEVING OBJECTIVES Stanzas 1112 Jupiter Venus Sama gentle persuasion Moon Dana bribery gifts Saturn Rahu Mercury Bheda intimidation division Sun Mars Danda force war Determined by the strongest planet in Lagna Upachayas 361011 or Kendras BLOCK 4 TREASURE IN THE HOUSE referenced section Sign of Arudha and planets aspectingoccupying it reveal direction and depth of buried treasure element of sign gives material BLOCK 5 FIRST LETTER OF QUERY DEITY Stanza 42 Letter number modulo 9 mapped to planet ruling deity disease cause BLOCK 6 PREDICTING BY BETEL LEAVES THAMBOOLA LAGNA Stanzas 4750 Formula 2 leafCount 5 1 mod 7 remainder weekday planet Sign of that planet in Prasna chart Thamboola Lagna Housebyhouse leaf quality Bhava prosperity affliction Thamboola Lagna planet immediate prediction BLOCK 7 PERFORMING PARENTAL OBSEQUIES Stanzas 5560 Sun and 9th lord wellplaced obsequies completed successfully Affliction signals Sun combustdebilitated 9th lord in 6812 obstacles Venus in good position grateful children BLOCK 8 ACQUISITION OF POWER Stanzas 7880 Nakshatras of Sun Moon Mars Lagna lord 10th lord at query time 34 falling in Indra Nirithi Varuna direction groups imminent headship BLOCK 9 KALACHAKRA YOGINI AND MRITYU Stanzas 8192 28nakshatra timecycle diagram including Abhijit Prana count from Suns nak pos 1 to Moons nak Deha count from Janma nak to Prana position Mrityu count from Krittika pos 28 anticlockwise to query nak All three on same linepole death same pole DehaMrityu prolonged illness BLOCK 10 KANTAKASTHUNA RAKTASTHUNA STUNA Hell and Heaven Stanzas 116120 Kantakasthuna count from Suns nak to Moola same count from Moola star Raktasthuna Mars longitude subtracted from 138 position Stuna kantaka star sthuna star mod 27 count from Moola If these three afflict Lagna or Arudha hell life equivalent to death BLOCK 11 YUGA LONGEVITY SYSTEM Stanzas 122125 Krita Yuga signs Aries Leo Sagittarius full Dasa years Treta Yuga signs Taurus Virgo Capricorn half Dasa years Dwapara Yuga signs Gemini Libra Aquarius quarter Dasa years Kali Yuga signs Cancer Scorpio Pisces oneeighth Dasa years Apply to both Rasi and Navamsa of each planet for proportionate longevity 
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
         Prasna Marga Chapter 17 Vivaha Prasna Marriage Query SOURCE Prasna Marga Chapter XVII Stanzas 142 WHAT THIS METHOD COMPUTES BLOCK 1 MARRIAGE POSSIBILITY Stanzas 712 LagnaArudha7th house analysis malefic vs. benefic balance whether marriage negotiations will succeed or break down. BLOCK 2 DEATH OF THE COUPLE Stanzas 1718 Moon afflicted in 6th8th 8th year additionally Mars in 6th8th from Moon 9th year MoonMars in 7th 7th month. BLOCK 3 YAMA SUKRA ANALYSIS Stanza 19 Calculates Yama Sukra lagna at weekdayspecific ghati after sunrise flags dusthana placement and Yoga Sphuta affliction. BLOCK 4 EARLY MARRIAGE INDICATORS Stanzas 2732 Moon in Upachaya with benefic aspect VenusMoon in Lagna or 7th MercuryVenusJupiter in kendras female DrekkanaNavamsa aspected by MoonVenus benefics in 1st2nd7th full Stanza 32 horary happiness check. BLOCK 5 QUALITY OF WIFE Stanzas 2332 JupiterVenus in 7th owncaste wife strength of 7th lord Venus devoted chaste or vicious wife combinations beautiful bride kendrastrikonas benefic RahuKetu in 7th warnings. BLOCK 6 TIMING OF MARRIAGE Stanzas 5865 Early middle age after prime of youth logic parvatamsa and mridwamsa checks for preyouth marriage JupiterSunMoon transit triggers. BLOCK 7 CHANDRABHILASHA SPHUTA Stanza 41 Full calculation Moonminutes 800 remainder a Chandrabhilasha sign floora3200 Chandravela sign union of all four transit windows for the wedding date. BLOCK 8 SPOUSE DESCRIPTION Stanzas 2021 Physical complexion nature and caste from the stronger of the 7th lord its signNavamsa lord and Venus. BLOCK 9 HORARY OMENS GUIDE Stanzas 2026 Reference table of classical nimittas auspicious inauspicious signs for the astrologer to verify at query time. 
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
         Prasna Marga Chapter 18 Santhathi Prasna Children Comprehensive implementation covering the principles of predicting the birth of children pregnancy Garbha Prasna sex of the child adoption curses and Santana Tithi calculations. 
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
         Prasna Marga Chapter 19 Issues According to Birth Horoscope SOURCE Prasna Marga Chapter XIX Stanzas 130 and companion stanzas 147155 WHAT THIS METHOD COMPUTES BLOCK 1 MOON ANALYSIS Stanza 2 Moon in Upachaya vs. Anupachaya with benefic aspect fertility outlook. Crosschart husbandwife comparison when partnerBirthTime is supplied. BLOCK 2 BEEJA SPHUTA MALE FERTILITY Stanzas 46 11 Method A Stanza 5 ghati method contribution of each planet expired arc in nakshatra 27 equivalent to 5 30 on the ghatis Method B Stanza 11 direct sum Sun Venus Jupiter longitudes Strength test Stanza 6 Beeja strong if in odd sign odd Navamsa benefic contact. BLOCK 3 KSHETRA SPHUTA FEMALE FERTILITY Stanzas 4 7 11 Method A Moon Mars Jupiter contributions same ghati formula as Beeja. Method B Moon Mars Jupiter direct longitudes. Strength test Stanza 7 Kshetra strong if in even sign even Navamsa benefic contact. BLOCK 4 AFFLICTION DIAGNOSIS Stanza 8 Rahu serpentgod curse Gulika Preta trouble Saturn pastlife sin Mars enemydeity trouble. BLOCK 5 CHILDLESSNESS AND LOSS YOGAS Stanzas 816 10 classical combinations from Stanzas 816. BLOCK 6 CHILDREN BIRTH YOGAS Stanzas 1720 6 positive combinations for birth of children. BLOCK 7 SANTANA GRAHA SPHUTAS Stanza 18 Each Santana Sphuta planet longitude 5 mod 360. Santana Trisphuta Santana Sun Santana Moon Santana Jupiter mod 360. Checked against 3rd5th7th nakshatra from Janma 88th108th pada 6812 from Lagna. BLOCK 8 SANTANA YOGA SPHUTA Stanzas 147150 Formula Santana Jupiter Yamakantaka 9 mod 360. Number of children floordegreesinsign 5. Jupiter controlling 3 vargas more than 6 sons. Drekkana lord debilitatedenemy which child dies Stanza 149. Mercury Saturn in 3 vargas twins Stanza 150. BLOCK 9 DATTA SPHUTA ADOPTION Stanza 151 Mercury Saturn FifthLord 5 mod 360. Solar odd Rasi Lunar even Navamsa malefic contact adoption. BLOCK 10 TIMING AND SEX Stanzas 153155 Sex of child from Navamsa of Yoga Sphuta odd male even female. Birth timing Santana Guru Yamakantaka Santana Gulika 81 nakshatra. Moon transiting that nakshatra or trines time of birth. 
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
         Prasna Marga Chapter 20 Seventh House According to Birth Horoscope Spouse Analysis SOURCE Prasna Marga Chapter XX Stanzas 166 OVERVIEW This chapter analyses the natal birth chart to reveal all aspects of the spouse character appearance career longevity and the timing of marriage. It is the horoscopic complement to Chapter XVII Vivaha Prasna which uses the horary chart. Per Stanza 1 when Jataka natal and Prasna agree predictions gain great accuracy. WHAT THIS METHOD COMPUTES BLOCK 1 MARRIAGE POSSIBILITY Stanza 6 7th house affliction indicators probabilities of no marriage or shortlived spouse. BLOCK 2 CHARACTER OF WIFE FROM 7TH HOUSE SIGN Stanzas 45 The 12 signbased character descriptions for the wife. BLOCK 3 DEATH OF WIFE YOGAS Stanzas 716 Stanza 7 MarsSaturnspecific signplanet in 7th wife dies or separation. Stanza 8 Saturn in Pisces 7th Jupiter in Virgo 7th strong malefic in 4th 8th5th lord in 7th SunVenus in 579 wife defective of limbs. Stanza 9 Venus hemmed by malefics danger SunRahu in 7th wasteful. Stanzas 1012 Venus in MarsSaturn sign or Navamsa wifes character. Stanza 13 Venus Ashtakavarga 7th from Venus dominated by malefics Gulika in trine wife dies soon. Stanza 14 Venus in MarsSun sign wife dies by fire. Stanza 15 Venus Mandi Rahu in trinekendra snakebite death. Stanza 16 Venus Saturn malefic in 8th from Venus unnatural death death mode from quadrupedalbirdwatery sign. BLOCK 4 NATURE OF WIFE FROM VENUS CONJUNCTIONS Stanzas 1718 Stanza 17 VenusSun bhutaafflicted but distinguished VenusMoon superior VenusMars Rakshasaafflicted has paramour VenusJupiter virtuous VenusMercury educated handsome. Stanza 18 VenusSaturn Gandharva trouble deceptive VenusRahuKetu low company limb defect VenusGulika sudden accidental death. BLOCK 5 WIFES NATURE FROM VENUS ASHTAKAVARGA Stanza 19 Bindu contributor in 7th from Lagna in Venus Ashtakavarga specific quality. BLOCK 6 PHYSICAL DESCRIPTION AND CASTE OF WIFE Stanzas 2021 Strongest of lord of sign of 7th lord Navamsa lord of 7th lord and Venus appearance. Jupiter or Venus in 7th owncaste wife. BLOCK 7 QUALITY YOGAS FOR THE WIFE Stanzas 2232 Stanza 22 Benefic in 9th from Venus strong 9th lord spiritual lucky. Stanza 23 7th lord benefic beneficaspected loved by husband and children. Stanza 24 7th occupiedaspected by lord or benefics Venus welldisposed good wife. Stanza 25 7th lord strong rich family weak poor family. Stanza 26 7th lord withaspected byhemmed between benefics good wife. Stanza 27 7th lordVenus in benefic signNavamsa strong 10th lord good qualities. Stanza 28 7thlordVenus strong Jupiter aspect devoted wife. Stanza 29 7th lordSun aspected by VenusMercury 7th lord with Jupiter chaste. Stanza 30 7th lord in kendra benefic aspectsignNavamsa paragon of chastity. Stanza 31 7th lordSun in malefic sign malefic Navamsa inclined to vice. Stanza 32 RahuKetu in 7th malefic aspect malefic Navamsa sinful wife. BLOCK 8 HUSBANDS TENDENCIES Stanza 33 Planets in 7th reveal the husbands erotic inclinations. BLOCK 9 SOCIAL STANDING OF WIFES FAMILY Stanzas 3436 Stanza 34 Lagna7th lords friends wifes family friendly enemies inimical. Stanza 35 Lagna lord very strong 7th lord in benefic Navamsa highborn family. Stanza 36 Lagna lord weak 7th lord combustinimicaldebilitated lower family. BLOCK 10 MULTIPLE WIVES REMARRIAGE YOGAS Stanzas 3746 Full enumeration of 10 classical yogas for 2 3 or many wives. BLOCK 11 WIFES BIRTH STAR Nakshatra THREE METHODS Stanzas 4749 Stanza 47 Compatible Janma Rasis from 7 indicators. Stanza 48 Moons Chandra Kaksha lord sign Lagna lord sign. Stanza 49 Three Nakshatra calculations from planetary longitude sums. BLOCK 12 DIRECTION FROM WHICH WIFE COMES Stanzas 5052 13 directional indicators from 7th lord Venus and aspectors. Distance farnearintermediate from sign quality Stanza 52. BLOCK 13 TIMING OF MARRIAGE Stanzas 6566 Stanza 65 DasaBhukti of 7th house occupant aspector 7th lord sign lord of 7th lord Navamsa lord of 7th lord Venus Moon Navamsa lord of Lagna Rahus Dasa also recognised. Stanza 66 Transit of VenusLagna lord7th lord over 7th or its trines Jupiters transit of 7th lords sign or its Navamsa. 
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
         Prasna Marga Chapter 23 Vrishti Prasna Queries regarding Rain Comprehensive implementation covering the probability of rain quantity timing and nature windystormy based on Arudha Lagna and planetary positions. 
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
         Prasna Marga Chapter 24 Raja Prasna Yuddha Prasna Queries on Rulers and War Comprehensive implementation covering the future of the government soldiers fate enemy invasion peace treaties and war outcomes. 
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
         Prasna Marga Chapter 25 Vrishti Prasna Rainfall Prediction SOURCE Prasna Marga Chapter XXV Stanzas 197 WHAT THIS METHOD COMPUTES BLOCK 1 PLANETARY COMBINATIONS FOR HEAVY RAINFALL Stanzas 15 Solar ingress into Gemini conditions SunMoonMarsSaturnRahu in watery signs MercuryVenus conjoin fixed sign triple conjunctions combustion combos earthy Sun watery vargas rainbow directions. BLOCK 2 MOCK SUN AND RAINBOW GUIDE Stanzas 68 Rainbow direction rules for rainy and other seasons. Pratisurya mock Sun directional effects north rain south tempest both sides flood top danger to king below calamity to people. BLOCK 3 PAKSHAWISE RAINFALL FROM LUNAR PHASE Stanzas 911 Rain on New Moon Pratipada rain in Shukla Paksha Rain on Full Moon no rain in Krishna Paksha 15 ghatikas rule on Dwiteeya Pratipada for paksha forecast. BLOCK 4 ASHADHA LUNAR MONTH SIGNIFICANCE Stanzas 1214 Northeast winds at Ashadha Full Moon evening good rain year Rain on Ashadha Krishna Chaturthi with Poorvabhadra luxuriant vegetation Weekday of Ashadha Shukla Panchami annual rain quality Sun in Aquarius Rohini tithi combinations. BLOCK 5 VENUS MANDALAS Stanzas 1620 Venuss postcombustion nakshatra determines annual rain forecast. Six Mandalas Bharanigroup through Dhanishtagroup 4th and 6th Mandalas copious rain 3rd and 5th famine 1st and 2nd below average. Moon in 7th from Venus or 5th7th9th from Saturn heavy rain Stanza 21. BLOCK 6 SEASONAL PLANETARY TRIGGERS Stanzas 2223 Combustion startend Moon conjunctions Sun in CancerCapricornAridra MercuryJupiter MercuryVenus JupiterVenus rain MarsSaturn without benefic firelightningstorm. BLOCK 7 CLOUD SHAPES AND NATURE OMENS Stanzas 2437 Classical nimitta catalogue ant eggcarrying snake behavior cattle rushing home cat scratching chameleons cocks crowing rainbow at dawndusk thunder patterns cloud colors and shapes Moon disc color honey parroteye Pratichandra mock Moon. BLOCK 8 CHAITRA AND SOLAR INGRESS Stanzas 3866 Chaitra month 1st day by weekday annual rain forecast Solar ingress into AriesCapricorn by nakshatra crop and rain outlook Solar ingress into Aries by tithi and Karana Annual forecast from lagna at Solar Ingress chart. BLOCK 9 ANNUAL NAKSHATRA MANDALA Stanzas 6871 Indra Mandala Rohini group prosperity Agni Mandala Bharani group scarcity fire Vayu Mandala Mrigasira group storms wind Varuna Mandala Aridra group copious rain. Sankramana Purusha by Karana price levels. BLOCK 10 HORARY QUERY INDICATORS NIMITTAS Stanzas 7280 Physical omens at query time querent touching water wet clothes standing near water shedding tears sighting elephantspregnant women Halo round Sun or Moon great downpour Planet pairs SunMars no rain MoonVenus heavy rain MercuryJupiter moderate rain First letter classification ghoshalong vowels rain khara no rain. BLOCK 11 HORARY CHART ANALYSIS Stanzas 8197 Moon aspected by beneficmalefic MoonMercuryJupiterVenus in kendra aspected by benefics floods ArudhaChatra in watery sign with watery planet heavy rain 4th underground water 7th rivers 10th rain from sky Mercury associationaspect winds disperse rain MarsMercurySaturnRahu in kendras storms MoonVenus in watery Lagna Prishtodaya triple RahuSaturn in water signs Full classification of watery signs and aquatic planets. BLOCK 12 OVERALL SYNTHESIS Weighted count of positivenegative indicators verdict. 
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
         Prasna Marga Chapter 26 Koopa Prasna WellDigging and Water Location SOURCE Prasna Marga Chapter XXVI Stanzas 170 WHAT THIS METHOD COMPUTES BLOCK 1 WATER AVAILABILITY YOGAS Stanzas 715 Thirteen specific planetary combinations that confirm underground water. Stanza 15 Single nowater indicator Moon in Taurus Rahu in Scorpio. BLOCK 2 SPRING QUANTITY Stanza 37 Moveable Lagna small spring Fixed many springs Common two springs. BLOCK 3 OLD BURIED WELL YOGAS Stanzas 3850 Twelve classical combinations indicating a submerged well in the compound. BLOCK 4 DIRECTION FROM BODY TOUCH Stanzas 1618 Observational bodytouch indicators for direction of digging. Bony spot no water Fleshy spot mirymuddy Forehead rocky. BLOCK 5 CHANDRA GUPTI CHAKRA Stanzas 2036 Four methods for locating the exact spot in the compound. Primary method Stanzas 2427 Dinarsha Udaya Nakshatra Moons Nakshatra. The 28square grid maps compass direction to the wells location. BLOCK 6 WATER TASTE Stanzas 5153 From planet inaspecting 4th house or Lagna Navamsa lord. Sunacidhot Moonsaltish Marsbitter Jupitersweet Venussour Saturnpungent Mercurymixed Rahuinsipid. BLOCK 7 VASTU PURUSHA AND COMPOUND DIVISION Stanzas 5557 Head NE of Vastu Purusha is best for wells. Compound divided into 12 signs Aquarius zone best Virgo zone forbidden. BLOCK 8 DEPTH AND WATER CHARACTER Stanzas 5865 Planets in Lagna determine depth rocksandabundance. Rasmis planetary rays measure depth in cubits halfcubits or manheights. Sun16 Moon4 Mars10 Mercury9 Jupiter7 Venus5 Saturn21 rays. Sign rays Aries7 Taurus8 Gemini12 Cancer11 Leo12 Virgo6 Libra9 Scorpio7 Sagittarius13 Capricorn7 Aquarius8 Pisces27. BLOCK 9 PLANETSIGN WATER ABUNDANCE Stanza 68 Watery planets in watery signs water at surface. Watery planets in nonwatery low water table. Nonwatery in nonwatery dry. BLOCK 10 DINARSHA Stanza 70 Expired ghatikas 28 60 Nakshatra counted from Aswini. 
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
         Prasna Marga Chapter 27 Bhojana Prasna Food Meal Query and Proshithogamana Prasna Return of a Traveller. BHOJANA PRASNA Cast when someone asks about a recent meal its quality menu server codiners conversation and aftermeal rest. Each of the 12 horary houses carries a fixed meal signification Stanzas 139. PROSHITHOGAMANA PRASNA Cast when someone asks whether an absent person traveller exile person out of contact will return when and how Stanzas 4046. 
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
         Prasna Marga Chapter 28 Suratha Prasna Queries on Intimacy SOURCE Prasna Marga Chapter XXVIII Stanzas 119 WHAT THIS METHOD COMPUTES BLOCK 1 UNION OCCURRENCE Stanzas 12 Sun in Lagna7th or aspectingconjoining lords of 1st or 7th no union. Krishnacharya MoonVenus inaspecting 7th union. 7th beneficmalefic happy or unhappy union. BLOCK 2 CONSENT AND EMOTIONAL STATE Stanzas 23 MoonVenus Sun aspectjoin genuine passion. MoonVenus malefic not Sun aspect Lagna no real love. Moon with malefics forced union woman unwilling. Sun with malefics forced union man unwilling. BLOCK 3 PARTNER QUALITIES Stanza 4 Moon with Sun in Suns vargas man is handsome and educated. Moon withaspecting benefics in benefic vargas woman has good qualities. BLOCK 4 PARTNER IDENTITY AND AGE Stanzas 58 Planet aspecting Lagna and its dignity partner type social status caste. 7th house occupant wife another woman dancing girl etc. Moon phase age of partner. BLOCK 5 CHATHRA RASI ANALYSIS Stanza 9 Arudha Chathra wife friend sign Chathra related family enemy sign Chathra inimical family. BLOCK 6 FREQUENCY AND TIMING Stanza 10 Odd ascendant odd aspecting planet sign once. Even twice. MarsVenus vargas exclusively many times. Sun varga daytime Moon varga nighttime. BLOCK 7 INCIDENT DETAILS Stanzas 1113 MoonMars in 1579 quarrel and sleeplessness. MoonSaturn dreamt of union no actual union. MoonSun partial intimacy. MoonVenus private conversation. MoonJupiter union with accomplished woman pregnancy possible. MoonMercury another woman not wife. Mars in Lagna Saturn in 7th or vice versa fear of fire no sleep. BLOCK 8 PLACE OF UNION Stanzas 1418 From 7th house planet Saturnrepaired house Marsburnt Mercurycarpenters Moonnew Sunwooden Venusornamental Jupiterstrong. Alternative Sun in watery sign bath house Sun in other kitchen. Marskitchen Mercuryplayground SaturnSudracowshed Rahulowbornlatrine Moonpalacetemple weak Venusold house. When Lagna unaspected determined by Lagna sign itself Stanzas 1718. 
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
         Prasna Marga Chapter 29 Nashta Prasna Lost Article Queries Implements predictions for queries about lost or stolen articles based on horoscope analysis 
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
         Generates Prasna Marga Chapter 30 predictions for Nashta Jataka reconstructing an unknown birth chart. When the querent has no birth record the Prasna chart at query time is used to reverseengineer the Janma Nakshatra Janma Lagna birth Moon sign and the birth positions of Jupiter and the Sun. Several methods are provided and should be weighed against Nimittas omens the number of persons present any body part touched and the querents appearance. Source Prasna Marga Chapter XXX. 
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
         Prasna Marga Chapter 31 Swapna Prasna Dream Interpretation SOURCE Prasna Marga Chapter XXXI Stanzas 168 ARCHITECTURE Three targeted LLM calls Qwenflash are fused into pure chartcalculation blocks when a dreamDescription is provided. All LLM calls are grounded exclusively in verbatim stanza text the model performs semantic lookup not free interpretation. Pure chart blocks always run. LLM CALL 1 DoshaChart CrossValidation gates everything Determines whether the dream is Doshaja physiological nonprophetic or Bhavija prophetic by crosschecking chart dosha against dream imagery. Source Stanza 46 Doshaja dreams will not be effective Stanzas 25 planet in Lagna specific imagery type. Runs in parallel with Call 2. LLM CALL 2 Symbol Matching with Severity Tiers Semantic matching of dream description against verbatim stanza catalogues. Returns four severity tiers immediateDeathSymbols diseaseThenDeathSymbols dreadfulResultSymbols earlyDeathOmen auspiciousSymbols Bharata pattern Abhichara indicator. Source Stanzas 1129 bad and 3667 good. Runs in parallel with Call 1. LLM CALL 3 PersonAdjusted Synthesis Oracle Waits for Calls 1 and 2. Applies sickhealthy distinction Stanzas 3031 6667 varnaspecific symbols Stanzas 6061 Bharata severity escalation Stanzas 4859 and Yama timing. Every claim must cite a stanza number. DECISION TREE dreamDescription empty pure chart blocks only no LLM isDaytimeDream mark ineffective no LLM Stanza 32 wasDreamForgottenpreMidnight mark very weak skip all LLM Stanza 33 isDoshaja strong match skip Call 3 UNLESS critical symbols found hadGoodDreamAfterBad Call 2 analyses both flags accordingly otherwise Calls 12 parallel Call 3 
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
         Given 2 root numbers 19 returns their compatibility as Good Bad or Neutral 
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
         Numerology Your birth number denotes your ruling power the structure of the body and the character depend on that number. The birth number denotes a persons status and desires. let us take it as 17101931. Number 17 becomes 17 8. So 8 is your Birth number. 
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
         Numerology The events that occur in your life your relationship with others your future and the end of your life are all denoted by your destiny number. The destiny number denotes to what extent a person will come up in life as well as it determines his fate. 
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
         The numerical values given to the alphabets are based on the Chaldean System Numbers values denote the wave length of the sound and impact of letters. The powers of the nine planets in twelve star signs at different times are indicated in 108 numbers. 
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
         Shows numerology prediction for given name. At first the name number is calculated based on Chaldean System then prediction is matched with translation from Mantra Sutras. 
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
         Generates a batch of suggested names matching a plainlanguage description using AI. Sends the description to the language model with the numerology namegeneration prompt and returns a list of candidate names that vary in length and style. Optionally excludes a set of previously generated names so repeated calls keep producing fresh suggestions. Useful for picking auspicious baby names brand names or business names by theme. 
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
         Returns the main Pancha Pakshi bird activity Ruling Eating Walking Sleeping or Dying for a person at a given moment. Determines the persons stellar birthbird whether the Moon is waxing or waning day vs night the weekday and which of the five yamas the check time falls into then looks these up in the Pancha Pakshi master table. The activity indicates how favourable that moment is for the person under the South Indian Pancha Pakshi five birds system. 
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
         Calculates which of the five yamas equal time divisions a given moment falls into under the Pancha Pakshi system. Splits the relevant span daytime sunrisetosunset or the night span either side of it into five equal parts and returns the yama index 1 to 5 together with the exact start and end times of that yama. Used as a building block for Pancha Pakshi bird activity. 
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
         Returns the persons Pancha Pakshi birthbird one of the five birds Vulture Owl Crow Cock or Peacock from their birth time. The bird is assigned from the ruling Moon constellation nakshatra at birth choosing between the waxingMoon and waningMoon bird groupings. The birthbird is the foundation of all Pancha Pakshi timing predictions for that person. 
        :return: BirdName
         """
        endpoint = "PanchaPakshiBirthBird"
        params = {
            "birthTime": birthTime.to_json(),
        }
        return cls._make_request(endpoint, params)


