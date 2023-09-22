# AUTO GENERATED ON 10:42 22/09/2023 +08:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any

class Object:
    pass
class Type:
    pass
class DateTimeOffset:
    pass
class DateTime:
    pass
class Boolean:
    pass
class Int32:
    pass
class TimeSpan:
    pass
class Double:
    pass
class String:
    pass
class Time:
    pass
class Angle:
    pass
class ZodiacSign:
    pass
class ZodiacName:
    pass
class ConstellationName:
    pass
class ConstellationAnimal:
    pass
class PlanetToSignRelationship:
    pass
class PlanetToPlanetRelationship:
    pass
class HouseSubStrength:
    pass
class PlanetName:
    pass
class PlanetConstellation:
    pass
class HouseName:
    pass
class GeoLocation:
    pass
class Person:
    pass
class PanchakaName:
    pass
class EventNature:
    pass
class Varna:
    pass
class PlanetMotion:
    pass
class Shashtiamsa:
    pass
class Dasas:
    pass
class Tools:
    pass

class Calculate:
    def PlanetAvasta(planetName: PlanetName, time: Time) -> Any:
        """
         Gets all the Avastas for a planet Lajjita Garvita Kshudita etc... 
        :return: List`1
         """
        ...
    def IsPlanetInLajjitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInGarvitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKshuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInTrashitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInMuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKshobhitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def AllPlanetData(planetName: PlanetName, time: Time) -> Any:
        """
         Wrapper function for open API
        :return: List`1
         """
        ...
    def AllHouseData(houseName: HouseName, time: Time) -> Any:
        """
         Wrapper function for open API
        :return: List`1
         """
        ...
    def AllPlanetHouseData(planetName: PlanetName, houseName: HouseName, time: Time) -> Any:
        """
         Wrapper function for open API
        :return: List`1
         """
        ...
    def AllZodiacSignData(zodiacName: ZodiacName, time: Time) -> Any:
        """
         Wrapper function for open API
        :return: List`1
         """
        ...
    def YoniKutaAnimal(person: Person) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def YoniKutaAnimal(sign: ConstellationName) -> ConstellationAnimal:
        """
         Given a constellation will give animal with sex used for yoni kuta calculations and body appearance prediction 
        :return: ConstellationAnimal
         """
        ...
    def SkyChartGIF(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Task`1
         """
        ...
    def SkyChart(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Task`1
         """
        ...
    def IsPlanetInWaterySign(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def ResidentialStrength(planetName: PlanetName, time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def TimeToLongitude(time: TimeSpan) -> Angle:
        """
         Converts time back to longitude it is the reverse of GetLocalTimeOffset in Time Exp 5h. 10m. 20s. E. Long. to 77 35 E. Long 
        :return: Angle
         """
        ...
    def TimeToEphemerisTime(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetNirayanaLongitude(time: Time, planetName: PlanetName) -> Angle:
        """
         Gets planet longitude used vedic astrology Nirayana Longitude Sayana Longitude corrected to Ayanamsa Number from 0 to 360 represent the degrees in the zodiac as viewed from earth Note Since Nirayana is corrected in actuality 0 degrees will start at Taurus not Aries 
        :return: Angle
         """
        ...
    def LunarDay(time: Time) -> LunarDay:
        """
        Empty sample text
        :return: LunarDay
         """
        ...
    def MoonConstellation(time: Time) -> PlanetConstellation:
        """
         Gets constellation behind the moon shortcut function 
        :return: PlanetConstellation
         """
        ...
    def PlanetConstellation(time: Time, planet: PlanetName) -> PlanetConstellation:
        """
         Gets the constellation behind a planet at a given time 
        :return: PlanetConstellation
         """
        ...
    def Tarabala(time: Time, person: Person) -> Tarabala:
        """
        Empty sample text
        :return: Tarabala
         """
        ...
    def Chandrabala(time: Time, person: Person) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def MoonSignName(time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def LagnaSignName(time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def NithyaYoga(time: Time) -> NithyaYoga:
        """
        Empty sample text
        :return: NithyaYoga
         """
        ...
    def Karana(time: Time) -> Karana:
        """
        Empty sample text
        :return: Karana
         """
        ...
    def SunSign(time: Time) -> ZodiacSign:
        """
        Empty sample text
        :return: ZodiacSign
         """
        ...
    def TimeSunEnteredCurrentSign(time: Time) -> Time:
        """
        Find time when Sun was in 0.001 degrees in current sign just entered sign
        :return: Time
         """
        ...
    def TimeSunLeavesCurrentSign(time: Time) -> Time:
        """
        Find time when Sun was in 29 degrees in current sign just about to leave sign Note 2 possible ways leaving time is calculated 1. degrees Sun is in sign is more than 29.999 degrees very very close to leaving sign 2. accuracy limit is hit
        :return: Time
         """
        ...
    def AllHouseLongitudes(time: Time) -> Any:
        """
         Calculates creates all houses as list 
        :return: List`1
         """
        ...
    def ConvertLmtToJulian(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetsInConjuction(time: Time, inputedPlanetName: PlanetName) -> Any:
        """
         Gets all the planets that are in conjunction with the inputed planet Note 1.The planet inputed is not included in return list 2. Theory behind conjunction Conjunction Two heavenly bodies in the same longitude. The effect of an aspect is felt even if the planets are not exactly in the mutual distances mentioned above. Therefore a socalled orb of aspect and this varies in each aspect is allowed. The orbs of aspects are Conjunction 8 degrees Planets can be in same sign but not conjunct There are also other variations of aspects brought about by two planets remaining in the same sign and not in conjunction but another planet occupying a trine in respect of the two. 
        :return: List`1
         """
        ...
    def DistanceBetweenPlanets(planet1: PlanetName, planet2: PlanetName, time: Time) -> Angle:
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for. Calculation in Nirayana longitudes Calculates longitudes for you 
        :return: Angle
         """
        ...
    def DistanceBetweenPlanets(planet1: Angle, planet2: Angle) -> Angle:
        """
         Gets longitudinal space between 2 planets Note Longitude of planet after 360 is 0 degrees when calculating difference this needs to be accounted for Expects you to calculate longitude 
        :return: Angle
         """
        ...
    def PlanetsInHouse(houseNumber: HouseName, time: Time) -> Any:
        """
         Gets the planets in the house 
        :return: List`1
         """
        ...
    def PlanetsInSign(signName: ZodiacName, time: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def AllPlanetSigns(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def AllPlanetLongitude(time: Time) -> Any:
        """
         Gets longitude positions of all planets 
        :return: List`1
         """
        ...
    def AllPlanetFixedLongitude(time: Time) -> Any:
        """
         Gets longitude positions of all planets Sayana Fixed zodiac 
        :return: List`1
         """
        ...
    def HousePlanetIsIn(time: Time, planetName: PlanetName) -> HouseName:
        """
         Gets the House number a given planet is in at a time 
        :return: HouseName
         """
        ...
    def LordOfHouse(houseNumber: HouseName, time: Time) -> PlanetName:
        """
         The lord of a bhava is the Graha planet in whose Rasi sign the Bhavamadhya falls 
        :return: PlanetName
         """
        ...
    def LordOfHouseList(houseList: Any, time: Time) -> Any:
        """
         The lord of a bhava is the Graha planet in whose Rasi sign the Bhavamadhya falls List overload to GetLordOfHouse above method 
        :return: List`1
         """
        ...
    def IsHouseSignName(house: HouseName, sign: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def HouseSignName(houseNumber: HouseName, time: Time) -> ZodiacName:
        """
         Gets the zodiac sign at middle longitude of the house. 
        :return: ZodiacName
         """
        ...
    def HouseConstellation(houseNumber: HouseName, time: Time) -> PlanetConstellation:
        """
         Gets the zodiac sign at middle longitude of the house. 
        :return: PlanetConstellation
         """
        ...
    def NavamsaSignNameFromLongitude(longitude: Angle) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def SignCountedFromInputSign(inputSign: ZodiacName, countToNextSign: Int32) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def SignCountedFromMoonSign(countToNextSign: Int32, inputTime: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def SignCountedFromPlanetSign(countToNextSign: Int32, inputTime: Time, startPlanet: PlanetName) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def SignCountedFromLagnaSign(countToNextSign: Int32, inputTime: Time) -> ZodiacName:
        """
        NO DESC FOUND!! ERROR
        :return: ZodiacName
         """
        ...
    def HouseCountedFromInputHouse(inputHouseNumber: Int32, countToNextHouse: Int32) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def PlanetSignName(planetName: PlanetName, time: Time) -> ZodiacSign:
        """
         Get zodiac sign planet is in. 
        :return: ZodiacSign
         """
        ...
    def IsPlanetInSign(planetName: PlanetName, signInput: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetNavamsaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         Get navamsa sign of planet 
        :return: ZodiacName
         """
        ...
    def SignsPlanetIsAspecting(planetName: PlanetName, time: Time) -> Any:
        """
         All their location with a quarter sight the 5th and the 9th houses with a half sight the 4th and the 8th houses with threequarters of a sight and the 7th house with a full sight. 
        :return: List`1
         """
        ...
    def HouseNavamsaSign(house: HouseName, time: Time) -> ZodiacName:
        """
         Get navamsa sign of house mid point TODO Checking for correctness needed 
        :return: ZodiacName
         """
        ...
    def PlanetThrimsamsaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def PlanetDwadasamsaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         When a sign is divided into 12 equal parts each is called a dwadasamsa and measures 2.5 degrees. The Bhachakra can thus he said to contain 12x12144 Dwadasamsas. The lords of the 12 Dwadasamsas in a sign are the lords of the 12 signs from it i.e. the lord of the first Dwadasamsa in Mesha is Kuja that of the second Sukra and so on. 
        :return: ZodiacName
         """
        ...
    def PlanetSaptamsaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def PlanetDrekkanaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def IsPlanetInMoolatrikona(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetRelationshipWithSign(planetName: PlanetName, zodiacSignName: ZodiacName, time: Time) -> PlanetToSignRelationship:
        """
         Gets a planets relationship to a sign based on the relation to the lord Note Moolatrikona Debilited Exalted is not calculated heres Rahu ketu not accounted for 
        :return: PlanetToSignRelationship
         """
        ...
    def PlanetCombinedRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName, time: Time) -> PlanetToPlanetRelationship:
        """
         In order to find the strengths of planets we have to mix the temporary relations and the permanent relations. Thus a temporary enemy plus a permanent or natural enemy becomes a bitter enemy. 
        :return: PlanetToPlanetRelationship
         """
        ...
    def PlanetRelationshipWithHouse(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
        """
         Gets a planets relationship with a house Based on the relation between the planet and the lord of the sign of the house Note needs verification if this is correct 
        :return: PlanetToSignRelationship
         """
        ...
    def PlanetTemporaryRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName, time: Time) -> PlanetToPlanetRelationship:
        """
         Temporary Friendship Planets found in the 2nd 3rd 4th 10th 11th and 12th signs from any other planet becomes the latters temporary friends. The others are its enemies. 
        :return: PlanetToPlanetRelationship
         """
        ...
    def PlanetInSign(signName: ZodiacName, time: Time) -> Any:
        """
         Gets all the planets in a sign 
        :return: List`1
         """
        ...
    def PlanetTemporaryFriendList(planetName: PlanetName, time: Time) -> Any:
        """
         The planets in the 2nd 3rd 4th 10th 11th and 12th signs from any other planet becomes his Tatkalika friend. 
        :return: List`1
         """
        ...
    def GreenwichApparentInJulianDays(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def LocalApparentTime(time: Time) -> DateTime:
        """
        Empty sample text
        :return: DateTime
         """
        ...
    def LocalMeanTime(time: Time) -> DateTimeOffset:
        """
         This method exists mainly for testing internal time calculation of LMT Important that this method passes the test at all times so much depends on this 
        :return: DateTimeOffset
         """
        ...
    def House(houseNumber: HouseName, time: Time) -> House:
        """
        Empty sample text
        :return: House
         """
        ...
    def Panchaka(time: Time) -> PanchakaName:
        """
        Empty sample text
        :return: PanchakaName
         """
        ...
    def LordOfWeekday(time: Time) -> PlanetName:
        """
        Empty sample text
        :return: PlanetName
         """
        ...
    def LordOfWeekday(weekday: DayOfWeek) -> PlanetName:
        """
        Empty sample text
        :return: PlanetName
         """
        ...
    def LmtToStd(lmtDateTime: DateTimeOffset, stdOffset: TimeSpan) -> DateTimeOffset:
        """
        Empty sample text
        :return: DateTimeOffset
         """
        ...
    def HoraAtBirth(time: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def PlanetHoraSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
        Empty sample text
        :return: ZodiacName
         """
        ...
    def SunriseTime(time: Time) -> Time:
        """
         get sunrise time for that day 
        :return: Time
         """
        ...
    def SunsetTime(time: Time) -> Time:
        """
         Get actual sunset time for that day at that place 
        :return: Time
         """
        ...
    def NoonTime(time: Time) -> DateTime:
        """
         Get actual noon time for that day at that place Returned in apparent time DateTime Note This is marked when the centre of the Sun is exactly on the meridian of the place. The apparent noon is almost the same for all places. Center of disk is not actually used for now future implementation 
        :return: DateTime
         """
        ...
    def IsPlanetInGoodAspectToPlanet(receivingAspect: PlanetName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInGoodAspectToHouse(receivingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetSthanaBalaNeutralPoint(planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetShadvargaBalaNeutralPoint(planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def IsPlanetInKendra(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKendra(planetList: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInKendraFromPlanet(kendraFrom: PlanetName, kendraTo: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def SignDistanceFromPlanetToPlanet(startPlanet: PlanetName, endPlanet: PlanetName, time: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsHouseLordInHouse(lordHouse: HouseName, occupiedHouse: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithMaleficPlanets(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInSign(sign: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def MaleficPlanetListInSign(sign: ZodiacName, time: Time) -> Any:
        """
         Gets list of evilmalefic planets in a sign 
        :return: List`1
         """
        ...
    def IsBeneficPlanetInSign(sign: ZodiacName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def BeneficPlanetListInSign(sign: ZodiacName, time: Time) -> Any:
        """
         Gets any goodbenefic planets in a sign 
        :return: List`1
         """
        ...
    def IsMaleficPlanetAspectHouse(house: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficPlanetAspectHouse(house: HouseName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByMaleficPlanets(lord: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByBeneficPlanets(lord: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def ArudhaLagnaSign(time: Time) -> ZodiacName:
        """
         Gets the Arudha Lagna Sign Reference Note Arudha Lagna and planetary dispositions in reference to it have a strong bearing on the financial status of the person. In my own humble experience Arudha Lagna should be given as much importance as the usual Janma Lagna. Arudha Lagna is the sign arrived at by counting as many signs from lord of Lagna as lord of Lagna is removed from Lagna. Thus if Aquarius is ascendant and its lord Saturn is in the 4th Taurus then the 4th from Taurus viz. Leo becomes Arudha Lagna. 
        :return: ZodiacName
         """
        ...
    def CountFromSignToSign(startSign: ZodiacName, endSign: ZodiacName) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def CountFromConstellationToConstellation(start: PlanetConstellation, end: PlanetConstellation) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsPlanetInHouse(time: Time, planet: PlanetName, houseNumber: HouseName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAllPlanetInHouse(time: Time, planetList: Any, houseNumber: HouseName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAnyPlanetInHouse(time: Time, planetList: Any, houseNumber: HouseName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetDebilitated(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetExalted(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def LunarMonth(time: Time) -> LunarMonth:
        """
        Empty sample text
        :return: LunarMonth
         """
        ...
    def IsFullMoon(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsWaterSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsFireSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsEarthSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsAirSign(moonSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetAntaramNature(person: Person, planet: PlanetName) -> EventNature:
        """
         WARNING MARKED FOR DELETION ERONEOUS RESULTS NOT SUITED FOR INTENDED PURPOSE METHOD NOT VERIFIED This methods perpose is to define the final good or bad nature of planet in antaram. For now only data from chapter Keyplanets for Each Sign If this proves to be inacurate add more checks in this method. bindu points Similar to method GetDasaInfoForAscendant Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology TODO meant to determine nature of antram 
        :return: EventNature
         """
        ...
    def IsPlanetBeneficToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetMaleficToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetYogakarakaToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetMarakaToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInOwnHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInEnemyHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetInFriendHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def SwissEphemeris(time: Time, planetName: PlanetName) -> Object:
        """
        NO DESC FOUND!! ERROR
        :return: Object
         """
        ...
    def IsPlanetSameHouseWithHouseLord(birthTime: Time, houseNumber: Int32, planet: PlanetName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def TimeHouseCalcs(cls) -> Any:
        """
        Empty sample text
        :return: IEnumerable`1
         """
        ...
    def HouseNatureScore(personBirthTime: Time, inputHouse: HouseName) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def HouseNatureScoreMK4(personBirthTime: Time, inputHouse: HouseName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetNatureScoreMK4(personBirthTime: Time, inputPlanet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetNatureScore(personBirthTime: Time, inputPlanet: PlanetName) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def BirthVarna(birthTime: Time) -> Varna:
        """
         Get a persons varna or color character A persons varna can be observed in real life 
        :return: Varna
         """
        ...
    def PlanetIshtaKashtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetKashtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetIshtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def AllPlanetsSignsFromMoon(signsFromMoon: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromLagna(signsFromLagna: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromMoon(signsFromList: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromList: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromMoon: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def IsPlanetsInSignsFromMoon(signsFromList: Int32, planetList: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetsInSignsFromPlanet(signsFromList: Int32, planetList: PlanetName, startPlanet: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetsInSignsFromLagna(signsFromList: Int32, planetList: PlanetName, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromMoon(signsFromList: Int32, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def Ayanamsa(time: Time) -> Angle:
        """
         The distance between the Hindu First Point and the Vernal Equinox measured at an epoch is known as the Ayanamsa in Varahamihiras time the summer solistice coincided with the first degree of Cancer and the winter solistice with the first degree of Capricorn whereas at one time the summer solistice coincided with the middle of the Aslesha 
        :return: Angle
         """
        ...
    def PlanetSayanaLongitude(time: Time, planetName: PlanetName) -> Angle:
        """
         NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def NextLunarEclipse(time: Time) -> DateTime:
        """
         find time of next lunar eclipse 
        :return: DateTime
         """
        ...
    def NextSolarEclipse(time: Time) -> DateTime:
        """
         finds the next solar eclipse globally 
        :return: DateTime
         """
        ...
    def PlanetEphemerisLongitude(time: Time, planetName: PlanetName) -> Angle:
        """
         NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def PlanetSayanaLatitude(time: Time, planetName: PlanetName) -> Angle:
        """
        Empty sample text
        :return: Angle
         """
        ...
    def PlanetSpeed(time: Time, planetName: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def ConstellationAtLongitude(planetLongitude: Angle) -> PlanetConstellation:
        """
         Converts Planet Longitude to Constellation equivelant Gets info about the constellation at a given longitude ie. Constellation Name Quarter Degrees in constellation etc. 
        :return: PlanetConstellation
         """
        ...
    def ZodiacSignAtLongitude(longitude: Angle) -> ZodiacSign:
        """
         Converts Planet Longitude to Zodiac Sign equivalent 
        :return: ZodiacSign
         """
        ...
    def LongitudeAtZodiacSign(zodiacSign: ZodiacSign) -> Angle:
        """
         Converts Zodiac Sign to Planet Longitude equivalent 
        :return: Angle
         """
        ...
    def DayOfWeek(time: Time) -> DayOfWeek:
        """
        Empty sample text
        :return: DayOfWeek
         """
        ...
    def LordOfHora(hora: Int32, day: DayOfWeek) -> PlanetName:
        """
        NO DESC FOUND!! ERROR
        :return: PlanetName
         """
        ...
    def HouseJunctionPoint(previousHouse: Angle, nextHouse: Angle) -> Angle:
        """
         Gets the junction point sandhi between 2 consecutive houses where one house begins and the other ends. 
        :return: Angle
         """
        ...
    def LordOfZodiacSign(signName: ZodiacName) -> PlanetName:
        """
        Empty sample text
        :return: PlanetName
         """
        ...
    def NextZodiacSign(inputSign: ZodiacName) -> ZodiacName:
        """
         Gets next zodiac sign after input sign 
        :return: ZodiacName
         """
        ...
    def NextHouseNumber(inputHouseNumber: Int32) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def PlanetExaltationPoint(planetName: PlanetName) -> ZodiacSign:
        """
         Gets the exact longitude where planet is ExaltedExaltation NOTE Rahu ketu have exaltation points ref Astroloy for Beginners pg. 12 Exaltation Each planet is held to be exalted when it is in a particular sign. The power to do good when in exaltation is greater than when in its own sign. Throughout the sign ascribed the planet is exalted but in a particular degree its exaltation is at the maximum level. 
        :return: ZodiacSign
         """
        ...
    def PlanetDebilitationPoint(planetName: PlanetName) -> ZodiacSign:
        """
         Gets the exact longitude where planet is DebilitatedDebility TODO method needs testing Note Rahu ketu have debilitation points ref Astroloy for Beginners pg. 12 planet to sign relationship is the whole sign this is just a point The 7th house or the 180th degree from the place of exaltation is the place of debilitation or fall. The Sun is debilitated in the 10th degree of Libra the Moon 3rd of Scorpio and so on. The debilitation or depression points are found by adding 180 to the maximum points given above. While in a state of fall planets give results contrary to those when in exaltation. ref Astroloy for Beginners pg. 11 
        :return: ZodiacSign
         """
        ...
    def IsEvenSign(planetSignName: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsOddSign(planetSignName: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsFixedSign(sunSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMovableSign(sunSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsCommonSign(sunSign: ZodiacName) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetPermanentRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName) -> PlanetToPlanetRelationship:
        """
         Gets a planets permenant relationship. Based on Hindu Predictive Astrology pg. 21 Note Rahu Ketu are not mentioned in any permenant relatioship by Raman. But some websites do mention this. As such Ramans take is taken as final. Since theres so far no explanation by Raman on Rahu Ketu permenant relation it is assumed that such relationship is not needed and to make them up for conveniece sake could result in wrong prediction down the line. But temporary relationship are mentioned by Raman for Rahu Ketu so explicitly use Temperary relationship where needed. 
        :return: PlanetToPlanetRelationship
         """
        ...
    def ConvertJulianTimeToNormalTime(julianTime: Double) -> DateTime:
        """
        NO DESC FOUND!! ERROR
        :return: DateTime
         """
        ...
    def GreenwichTimeFromJulianDays(julianTime: Double) -> DateTimeOffset:
        """
        NO DESC FOUND!! ERROR
        :return: DateTimeOffset
         """
        ...
    def GreenwichLmtInJulianDays(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def GetHouse1And10Longitudes(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double[]
         """
        ...
    def LmtToUtc(time: Time) -> DateTimeOffset:
        """
        Empty sample text
        :return: DateTimeOffset
         """
        ...
    def GocharaHouse(birthTime: Time, currentTime: Time, planet: PlanetName) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsGocharaObstructed(planet: PlanetName, gocharaHouse: Int32, birthTime: Time, currentTime: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetsInGocharaHouse(birthTime: Time, currentTime: Time, gocharaHouse: Int32) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def Vedhanka(planet: PlanetName, house: Int32) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def IsGocharaOccurring(birthTime: Time, time: Time, planet: PlanetName, gocharaHouse: Int32) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetGocharaBindu(birthTime: Time, nowTime: Time, planet: PlanetName, bindu: Int32) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetAshtakvargaBindu(planet: PlanetName, signToCheck: ZodiacName, time: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def AllBhinnashtakavargaChart(birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def PlanetBhinnashtakavargaChart(mainPlanet: PlanetName, birthTime: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def GetPlanetBeneficHouseAshtakvarga(mainPlanet: String, minorPlanet: String) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32[]
         """
        ...
    def GetPlanetDasaMajorPlanetAndMinorRelationship(majorPlanet: PlanetName, minorPlanet: PlanetName) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: ValueTuple`2
         """
        ...
    def CurrentDasaCountFromBirth(birthTime: Time, currentTime: Time) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...
    def CurrentPlanetDasas(birthTime: Time, currentTime: Time) -> Dasas:
        """
         The main method that starts all Dasa Calculations Gets the occuring Planet Dasas PD1 PD2... for a person at the given time 
        :return: Dasas
         """
        ...
    def DasaCountedFromInputDasa(startDasaPlanet: PlanetName, years: Double) -> Dasas:
        """
        NO DESC FOUND!! ERROR
        :return: Dasas
         """
        ...
    def NextDasaPlanet(planet: PlanetName) -> PlanetName:
        """
         Gets next planet in Dasa order This order is also used for Bhukti Antaram RefHindu Predictive Astrology pg. 54 
        :return: PlanetName
         """
        ...
    def TimeLeftInBirthDasa(birthTime: Time, startConstellation: PlanetConstellation) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def YearsTraversedInBirthDasa(birthTime: Time, startConstellation: PlanetConstellation) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def DasaTimePerMinute(constellationName: ConstellationName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def ConstellationDasaPlanet(constellationName: ConstellationName) -> PlanetName:
        """
         Gets the related lord Dasa planet for a given constellation Used to find the ruling Dasa Planet RefHindu Predictive Astrology pg. 54 
        :return: PlanetName
         """
        ...
    def PD1PlanetFullYears(planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD2PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD3PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD4PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD5PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD6PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD7PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName, pd7Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PD8PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName, pd7Planet: PlanetName, pd8Planet: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def IsMercuryAfflicted(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMercuryMalefic(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsMoonBenefic(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetBenefic(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def BeneficPlanetList(time: Time) -> Any:
        """
         Gets all planets that are benefics at a given time since moon mercury changes Benefics on the other hand tend to do good but sometimes they also become capable of doing harm. 
        :return: List`1
         """
        ...
    def IsPlanetMalefic(planetName: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def MaleficPlanetList(time: Time) -> Any:
        """
         Gets list of permanent malefic planets for moon mercury it is based on changing factors Malefics are always inclined to do harm but under certain conditions the intensity of the mischief is tempered. 
        :return: List`1
         """
        ...
    def PlanetsInAspect(inputPlanet: PlanetName, time: Time) -> Any:
        """
         Gets all planets the inputed planet is transmitting aspect to 
        :return: List`1
         """
        ...
    def PlanetsAspectingPlanet(time: Time, receivingAspect: PlanetName) -> Any:
        """
         Gets all planets the transmitting aspect to inputed planet 
        :return: List`1
         """
        ...
    def HousesInAspect(planet: PlanetName, time: Time) -> Any:
        """
         Gets houses aspected by the inputed planet 
        :return: List`1
         """
        ...
    def PlanetsAspectingHouse(inputHouse: HouseName, time: Time) -> Any:
        """
         Gets all planets aspecting inputed house 
        :return: List`1
         """
        ...
    def IsPlanetAspectedByPlanet(receiveingAspect: PlanetName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsHouseAspectedByPlanet(receiveingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithPlanet(planetA: PlanetName, planetB: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def AllPlanetOrderedByStrength(time: Time) -> Any:
        """
         Returns an array of all planets sorted by strenght 0 index being strongest to 8 index being weakest Note Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. 
        :return: List`1
         """
        ...
    def IsPlanetBeneficInShadbala(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def IsHouseBeneficInShadbala(house: HouseName, birthTime: Time, threshold: Double) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def AllPlanetStrength(time: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def GetAllHousesOrderedByStrength(time: Time) -> HouseName:
        """
         Returns an array of all houses sorted by strength 0 index being strongest to 11 index being weakest 
        :return: HouseName[]
         """
        ...
    def PlanetShadbalaPinda(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         THE FINAL TOTAL STRENGTH Shadbala the six sources of strength and weakness the planets The importance of and the part played by the Shadbalas in the science of horoscopy are manifold In order to obtain the total strength of the Shadbala Pinda of each planet we have to add together its Sthana Bala Dik Bala Kala Bala. Chesta Bala and Naisargika Bala. And the Grahas Drik Bala must be added to or subtracted from the above sum according as it is positive or negative. The result obtained is the Shadbala Pinda of the planet in Shashtiamsas. Note Rahu Ketu supported via house lord 
        :return: Shashtiamsa
         """
        ...
    def PlanetStrength(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         get total combined strength of the inputed planet input birth time to get strength in horoscope note an alias method to GetPlanetShadbalaPinda strength is easier to remember 
        :return: Shashtiamsa
         """
        ...
    def PlanetDrikBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Aspect strength This strength is gained by the virtue of the aspect Graha Dristi of different planets on other planet. The aspect of benefics is considered to be strength and the aspect of malefics is considered to be weaknesses. Drik Bala.This means aspect strength. The Drik Bala of a Gqaha is onefourth of the Drishti Pinda on it. It is positive or negative according as the Drishti Pinda is positive or negative. See the formula given on page 85. There is special aspect for Jupiter Mars and Saturn on the 5th and 9th 4th and 8th and 3rd and 10th signs respectively. 
        :return: Shashtiamsa
         """
        ...
    def FindViseshaDrishti(dk: Double, p: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def FindDrishtiValue(dk: Double) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetNaisargikaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Nalsargika Bala.This is the natural strength that each Graha possesses. The value assigned to each depends upon its luminosity. Ravi the brightest of all planets has the greatest Naisargika strength while Sani the darkest has the least Naisargika Bala. This is the natural or inherent strength of a planet. 
        :return: Shashtiamsa
         """
        ...
    def PlanetChestaBala(planetName: PlanetName, time: Time, includeSunMoon: Boolean) -> Shashtiamsa:
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        ...
    def SunMoonChestaBala(planetName: PlanetName) -> Shashtiamsa:
        """
         special function to get chesta score for IshtaKashta score Bala book pg. 108 
        :return: Shashtiamsa
         """
        ...
    def Madhya(epochToBirthDays: Double, time1: Time) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: Dictionary`2
         """
        ...
    def EpochInterval(time1: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetMotionName(planetName: PlanetName, time: Time) -> PlanetMotion:
        """
         Gets the planets motion name can be Retrograde Direct Stationary a name version of Chesta Bala 
        :return: PlanetMotion
         """
        ...
    def PlanetCirculationTime(planetName: PlanetName) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetSaptavargajaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Sapthavargajabala This is the strength of a planet due to its residence in the seven subdivisions according to its relation with the dispositor. Saptavargaja bala means the strength a planet gets by virtue of its disposition in a friendly neutral or inimical Rasi Hora Drekkana Sapthamsa Navamsa Dwadasamsa and Thrimsamsa. 
        :return: Shashtiamsa
         """
        ...
    def PlanetShadvargaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Shadvarga bala This is the strength of a planet due to its residence in the 6 subdivisions according to its relation with the dispositor. They are 1 Rasi 2 Hora 3 Drekkana 4 Navamsa 5 Dwadasamsa and 6 Trimsamsa. 
        :return: Shashtiamsa
         """
        ...
    def IsPlanetStrongInShadvarga(planet: PlanetName, time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetSthanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Positonal strength A planet occupies a certain sign in a Rasi and friendly neutrai or inimical varga. It is either exalted or debilitated lt ocupies its Moolathrikona or it has its own varga. All these states refer to the position or residence of the planet and as such a certain degree of strength or weakness attends on it. This strength or potency is known as the Sthanabala. 1.Uccha Bala Uccha means exaltation. When a planet is placed in its highest exaltation point it is of full strength and when it is in its deepest debilitation point it is devoid of any strength. When in between the strength is calculated proportionately dependent on the distance these planets are placed from the highest exaltation or deepest debilitation point. 2.Sapta Vargiya Bala Rashi Hora Drekkana Saptamsha Navamsha Dwadasamsha and Trimsamsha constitute the Sapta Varga. The strength of the planets in these seven divisional charts based on their placements in Mulatrikona own sign friendly sign etc. constitute the Sapta vargiya bala. 3.OjaYugma RashiAmsha Bala Oja means odd signs and Yugma means even signs. Thus as the name imply this strength is derived from a planets placement in the odd or even signs in the Rashi and Navamsha. 4.Kendradi Bala The name itself implies how to compute this strength. A planet in a Kendra 14710 gets full strength while one in Panapara 25811 gets half and the one in Apoklimas 12369 gets quarter strength. 5.Drekkana Bala Due to placement in first second or third Drekkana of a sign male female and hermaphrodite planets respectively get a quarter strength according to placements in the first second and third Drekkana. 
        :return: Shashtiamsa
         """
        ...
    def PlanetDrekkanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Drekkanabala The Sun Jupiter and Mars in the lst Saturn and Mercury in the 2nd and the Moon and Venus in the last Drekkana get full strength of 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        ...
    def PlanetKendraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Kendrtzbala Planets in Kendras get 60 shashtiamsas in Panapara 30 and in Apoklima 15. 
        :return: Shashtiamsa
         """
        ...
    def PlanetOjayugmarasyamsaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Ojayugmarasyamsa In odd Rasi and Navamsa the Sun Mars Jupiter Mercury and Saturn get strength and the rest in even signs 
        :return: Shashtiamsa
         """
        ...
    def PlanetKalaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
        Empty sample text
        :return: Shashtiamsa
         """
        ...
    def PlanetYuddhaBala(inputedPlanet: PlanetName, preKalaBalaValues: Any, time: Time) -> Shashtiamsa:
        """
        NO DESC FOUND!! ERROR
        :return: Shashtiamsa
         """
        ...
    def PlanetAyanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Ayanabala All planets get 30 shasbtiamsas at the equator. For the Sun Jupiter Mars and Venus add proportionately when they are in northern course and for the Moon and Saturn when in southern course. Deduct proportionately when they are in the opposite direction. Unit of strength is 60 shashtiamsas. TODO some values for calculation with standard hooscope out of whack it seems small differences in longitude seem magnified at final value not 100 sure need further testing for confirmation but final values seem ok so far 
        :return: Shashtiamsa
         """
        ...
    def PlanetDeclination(planetName: PlanetName, time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def EclipticObliquity(time: Time) -> Double:
        """
        NO DESC FOUND!! ERROR
        :return: Double
         """
        ...
    def PlanetHoraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         AKA Horadhipathi Bala 
        :return: Shashtiamsa
         """
        ...
    def PlanetAbdaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         The planet who is the king of the year of birth is assigned a value of 15 Shashtiamsas as his Abdabala. 
        :return: Shashtiamsa
         """
        ...
    def PlanetMasaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
        Empty sample text
        :return: Shashtiamsa
         """
        ...
    def PlanetVaraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
        Empty sample text
        :return: Shashtiamsa
         """
        ...
    def YearAndMonthLord(time: Time) -> Object:
        """
        NO DESC FOUND!! ERROR
        :return: Object
         """
        ...
    def PlanetTribhagaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Thribhagabala Mercury the Sun and Saturn get 60 shashtiamsas each during the lst 2nd and 3rd onethird positions of the day respectively. The Moon Venus and Mars govern the lst 2nd and 3rd onethird portion of the night respectively. Jupiter is always strong and gets 60 shashtiamsas of strength. 
        :return: Shashtiamsa
         """
        ...
    def PlanetOchchaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Oochchabala The distance between the planets longitude and its debilitation point divided by 3 gives its exaltation strength or oochchabaJa. 
        :return: Shashtiamsa
         """
        ...
    def IsDayBirth(time: Time) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def PlanetPakshaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Pakshabala When the Moon is waxing take the distance from the Sun to the Moon and divide it by 3. The quotient is the Pakshabala. When the Moon is waning take the distance from the Moon to the Sun and divide it by 3 for assessing Pakshabala. Moon Jupiter Venus and Mercury are strong in Sukla Paksba and the others in Krishna Paksha. Note Mercury is benefic or malefic based on planets conjunct with it 
        :return: Shashtiamsa
         """
        ...
    def PlanetNathonnathaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Nathonnathabala Midnight to midday the Sun Jupiter and Venus gain strength proportionately till they get maximum at zenith. The other planets except Mercury. are gaining strength from midday to midnight proportionately. In the same way Mercury is always strong and gets 60 shashtiamsas. 
        :return: Shashtiamsa
         """
        ...
    def PlanetDigBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Jupiter and Mercury are strong in Lagoa Ascendant the Sun and Mars in the 10th Saturn in the 7th and the Moon and Venus in the 4th. The opposite houses are weak points. Divide the distance between the longitude of the planet and its depression point by 3. Quotient is the strength. 
        :return: Shashtiamsa
         """
        ...
    def HouseStrength(inputHouse: HouseName, time: Time) -> Shashtiamsa:
        """
         Bhava Bala.Bhava means house and Bala means strength. Bhava Bala is the potency or strength of the house or bhava or signification. We have already seen that there are 12 bhavas which comprehend all human events. Each bhava signifies or indicates certain events or functions. For instance the first bhava represents Thanu or body the appearance of the individual his complexion his disposition his stature etc. If it attains certain strength the native will enjoy the indications of the bhava fully otherwise he will not sufficiently enjoy them. The strength of a bhava is composed of three factors viz. 1 Bhavadhipathi Bala 2 Bhava Digbala 3 Bhava Drishti Bala. 
        :return: Shashtiamsa
         """
        ...
    def BhavaDrishtiBala(time: Time) -> HouseSubStrength:
        """
         Bhavadrishti Bala.Each bhava in a horoscope remains aspected by certain planets. Sometimes the aspect cast on a bhava will be positive and sometimes it will be negative according as it is aspected by benefics or malefics. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def CalcBhavaDigBala(time: Time) -> HouseSubStrength:
        """
         Bhava Digbala.This is the strength acquired by the different bhavas falling in the different groups or types of signs. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BhavaAdhipathiBala(time: Time) -> HouseSubStrength:
        """
         Bhavadhipatbi Bala.This is the potency of the lord of the bhava. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BeneficPlanetListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def BeneficPlanetListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def BeneficHouseListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def BeneficHouseListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def MaleficPlanetListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def MaleficPlanetListByShadbala(personBirthTime: Time) -> Any:
        """
         0 index is most malefic 
        :return: List`1
         """
        ...
    def MaleficHouseListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
        NO DESC FOUND!! ERROR
        :return: List`1
         """
        ...
    def MaleficHouseListByShadbala(personBirthTime: Time) -> Any:
        """
        Empty sample text
        :return: List`1
         """
        ...
    def GetHouseTags(house: HouseName) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def GetSignTags(zodiacName: ZodiacName) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def GetPlanetTags(lordOfHouse: PlanetName) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def GetHouseType(houseNumber: HouseName) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def GetDasaInfoForAscendant(ascendantName: ZodiacName) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def GetType(cls) -> Type:
        """
        NO DESC FOUND!! ERROR
        :return: Type
         """
        ...
    def ToString(cls) -> String:
        """
        NO DESC FOUND!! ERROR
        :return: String
         """
        ...
    def Equals(obj: Object) -> Boolean:
        """
        NO DESC FOUND!! ERROR
        :return: Boolean
         """
        ...
    def GetHashCode(cls) -> Int32:
        """
        NO DESC FOUND!! ERROR
        :return: Int32
         """
        ...

