# AUTO GENERATED ON 04:14 24/09/2023 +08:00
# DO NOT EDIT DIRECTLY, USE STATIC TABLE GENERATOR IN MAIN REPO

from typing import Any

class Tarabala:
    pass
class Karana:
    pass
class NithyaYoga:
    pass
class House:
    pass
class DayOfWeek:
    pass
class LunarMonth:
    pass
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
class LunarDay:
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
         Lajjita humiliated Planet in the 5th house in conjunction with rahu or ketu Saturn or mars. 
        :return: Boolean
         """
        ...
    def IsPlanetInGarvitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Garvita proud Planet in exaltation sign or moolatrikona zone happiness and gains 
        :return: Boolean
         """
        ...
    def IsPlanetInKshuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Kshudita hungry Planet in enemys sign or conjoined with enemy or aspected by enemy Grief 
        :return: Boolean
         """
        ...
    def IsPlanetInTrashitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         Trashita thirsty Planet in a watery sign aspected by a enemy and is without the aspect of benefic Planets The Planet who being conjoined or aspected by a Malefic or his enemy Planet is situated without the aspect of a benefic Planet in the 4th House is Trashita. Another version If the Planet is situated in a watery sign is aspected by an enemy Planet and is without the aspect of benefic Planets he is called Trashita. A planet in a Water Sign and aspected by an enemy planet with no auspiscious Graha aspecting is said to be Trishita AvasthaThirsty State. This state is in effect whenever a planet is in a Water Sign and it gets aspected by an enemy planet. But if a Gentle Planet MercuryVenusMoon aspects here it strengthens the planet in Water Sign. This Avastha is only for the aspecting enemy planet that will cause TrishitaThirst. This state shows that a planet in a watery Rasi can still be productive even when aspected by enemies though it will not be happy. As the name Thirsty State implies it indicates the lack of emotional fulfillment that a planet experiences. 
        :return: Boolean
         """
        ...
    def IsPlanetInMuditaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         The Planet who is in his friends sign is in conjunction with Jupiter and is together with or is aspected by a friendly Planet is called Mudita Mudita sated happy Planet in a friends sign or aspected by a friend and conjoined with Jupiter Gains If a planet is in a friends sign or joined with a friend or aspected by a friend or that joined with Jupiter is called Mudita AvasthaDelighted State It is clear from explanation itself that a planet will feel delighted when it is in friendly sign or friendly planet conjunctsaspects or it is joined by the biggest benefic planet Jupiter. We can understand planets delight in such cases. Planet in friendly sign A planet in a friendly sign is productive and the stronger that friend planet the more productive it will be. 
        :return: Boolean
         """
        ...
    def IsPlanetInKshobhitaAvasta(planetName: PlanetName, time: Time) -> Boolean:
        """
         If a planet is conjunct by Sun or it is aspected by Enemy Malefic Planets then it should always be known as Kshobhita AvasthaAgitated State Kshobhita guilty repentant Planet in conjunction with sun and aspected by malefics and an enemy. Penury
        :return: Boolean
         """
        ...
    def AllPlanetData(planetName: PlanetName, time: Time) -> Any:
        """
         Gets all possible calculations for a Planet at a given Time
        :return: List`1
         """
        ...
    def AllHouseData(houseName: HouseName, time: Time) -> Any:
        """
         All possible calculations for a House at a given Time 
        :return: List`1
         """
        ...
    def AllPlanetHouseData(planetName: PlanetName, houseName: HouseName, time: Time) -> Any:
        """
         All possible calculations for a Planet and House at a given Time 
        :return: List`1
         """
        ...
    def AllZodiacSignData(zodiacName: ZodiacName, time: Time) -> Any:
        """
         All possible calculations for a Zodiac Sign at a given Time 
        :return: List`1
         """
        ...
    def YoniKutaAnimal(person: Person) -> String:
        """
         Given a person will give yoni kuta animal with sex 
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
         Get sky chart as animated GIF. URL can be used like a image source link 
        :return: Task`1
         """
        ...
    def SkyChart(time: Time) -> Any:
        """
         Get sky chart at a given time. SVG image file. URL can be used like a image source link 
        :return: Task`1
         """
        ...
    def IsPlanetInWaterySign(planetName: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is in a Watery or aqua sign 
        :return: Boolean
         """
        ...
    def ResidentialStrength(planetName: PlanetName, time: Time) -> Double:
        """
         Strength to judge the exact quantity of effect planet gives in a house Use of Residential Strength This will enable us to judge the exact quantity of effect that a pJanet in a Bhava gives which may find expression during its Dasa.Its application and usefulness will be explained on a subsequent occasion. This effect will materialize during his Dasa or Bhukti. This is only a general statement standing to be modified or qualified in the light of other important factors such as the strength or the weakness of the planets aspecting the Bhavas the strength of the Bhava itself and the disposition of planets towards particular signs the yogakarakas and such other factors. For instance in the Standard Horoscope Jupiter gives 0.48 units of the total effects of the 6th Bhava. 
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
         Gets the ephemris time that is consumed by Swiss Ephemeris Converts normal time to Ephemeris time shown as a number 
        :return: Double
         """
        ...
    def PlanetNirayanaLongitude(time: Time, planetName: PlanetName) -> Angle:
        """
         Planet longitude that has been corrected with Ayanamsa Gets planet longitude used vedic astrology Nirayana Longitude Sayana Longitude corrected to Ayanamsa Number from 0 to 360 represent the degrees in the zodiac as viewed from earth Note Since Nirayana is corrected in actuality 0 degrees will start at Taurus not Aries 
        :return: Angle
         """
        ...
    def LunarDay(time: Time) -> LunarDay:
        """
         Gets Moons position or day in lunar calendar 
        :return: LunarDay
         """
        ...
    def MoonConstellation(time: Time) -> PlanetConstellation:
        """
         Gets name of Constellation behind the moon at a given time 
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
         Tarabala or birth ruling constellation strength used for personal muhurtha 
        :return: Tarabala
         """
        ...
    def Chandrabala(time: Time, person: Person) -> Int32:
        """
         Chandrabala or lunar strength used for personal muhurtha Reference Chandrabala. As we have already said above the consideration of the Moon and his position are of much importance in Muhurtha. To be at its best the Moon should not occupy in the election chart a position that happens to represent the 6th 8th or 12th from the persons Janma Rasi. 
        :return: Int32
         """
        ...
    def MoonSignName(time: Time) -> ZodiacName:
        """
         Zodiac sign behind the Moon at given time 
        :return: ZodiacName
         """
        ...
    def LagnaSignName(time: Time) -> ZodiacName:
        """
         Zodiac sign at the LagnaAscendant at given time 
        :return: ZodiacName
         """
        ...
    def NithyaYoga(time: Time) -> NithyaYoga:
        """
         Nithya Yoga Longitude of Sun Longitude of Moon 1320 or 800 
        :return: NithyaYoga
         """
        ...
    def Karana(time: Time) -> Karana:
        """
         Used for auspicious activities part Panchang like Tithi Nakshatra Yoga etc. 
        :return: Karana
         """
        ...
    def SunSign(time: Time) -> ZodiacSign:
        """
         Zodiac sign behind the Sun at a time 
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
         Convert LMT to Julian Days used in Swiss Ephemeris 
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
         Gets list of all planets thats in a housebhava at a given time 
        :return: List`1
         """
        ...
    def PlanetsInSign(signName: ZodiacName, time: Time) -> Any:
        """
         Gets list of all planets thats in a sign at a given time 
        :return: List`1
         """
        ...
    def AllPlanetSigns(time: Time) -> Any:
        """
         Gets list of all planets and the zodiac signs they are in 
        :return: Dictionary`2
         """
        ...
    def AllPlanetLongitude(time: Time) -> Any:
        """
         Gets the Nirayana longitude of all 9 planets 
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
         Gets planet lord of given house at given time The lord of a bhava is the Graha planet in whose Rasi sign the Bhavamadhya falls 
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
         Checks if the inputed sign was the sign of the house during the inputed time 
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
         Gets Navamsa sign given a longitude 
        :return: ZodiacName
         """
        ...
    def SignCountedFromInputSign(inputSign: ZodiacName, countToNextSign: Int32) -> ZodiacName:
        """
         Exp Get 4th sign from Cancer 
        :return: ZodiacName
         """
        ...
    def SignCountedFromMoonSign(countToNextSign: Int32, inputTime: Time) -> ZodiacName:
        """
         Exp Get 4th sign from Moon 
        :return: ZodiacName
         """
        ...
    def SignCountedFromPlanetSign(countToNextSign: Int32, inputTime: Time, startPlanet: PlanetName) -> ZodiacName:
        """
         Exp Get 4th sign from Saturn 
        :return: ZodiacName
         """
        ...
    def SignCountedFromLagnaSign(countToNextSign: Int32, inputTime: Time) -> ZodiacName:
        """
         Exp Get 4th sign from LagnaAscendant 
        :return: ZodiacName
         """
        ...
    def HouseCountedFromInputHouse(inputHouseNumber: Int32, countToNextHouse: Int32) -> Int32:
        """
         Exp Get 4th house from 5th house input house 
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
         Checks if a given planet is in a given sign at a given time 
        :return: Boolean
         """
        ...
    def PlanetNavamsaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         Get Navamsa sign of planet at a given time 
        :return: ZodiacName
         """
        ...
    def SignsPlanetIsAspecting(planetName: PlanetName, time: Time) -> Any:
        """
         Gives a list of all zodiac signs a specified planet is aspecting All their location with a quarter sight the 5th and the 9th houses with a half sight the 4th and the 8th houses with threequarters of a sight and the 7th house with a full sight. 
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
         Get Thrimsamsa sign of house mid point 
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
         sign is divided into 7 equal parts each is called a Saptamsa and measures 4.28 degrees 
        :return: ZodiacName
         """
        ...
    def PlanetDrekkanaSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         Gets the Drekkana sign the planet is in 
        :return: ZodiacName
         """
        ...
    def IsPlanetInMoolatrikona(planetName: PlanetName, time: Time) -> Boolean:
        """
         Similar to Exaltation but covers a range not just a point Moolathrikonas these are positions similar to exaltation. NOTE No moolatrikone for Rahu Ketu no error will be raised 
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
         strengths of planets mix the temporary relations and the permanent In order to find the strengths of planets we have to mix the temporary relations and the permanent relations. Thus a temporary enemy plus a permanent or natural enemy becomes a bitter enemy. 
        :return: PlanetToPlanetRelationship
         """
        ...
    def PlanetRelationshipWithHouse(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
        """
         Relation between the planet and the lord of the sign of the house Gets a planets relationship with a house Based on the relation between the planet and the lord of the sign of the house Note needs verification if this is correct 
        :return: PlanetToSignRelationship
         """
        ...
    def PlanetTemporaryRelationshipWithPlanet(mainPlanet: PlanetName, secondaryPlanet: PlanetName, time: Time) -> PlanetToPlanetRelationship:
        """
         Planets found in the certain signs from any other planet becomes temporary friends Temporary Friendship Planets found in the 2nd 3rd 4th 10th 11th and 12th signs from any other planet becomes the latters temporary friends. The others are its enemies. 
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
         Get list of Temporary Tatkalika Friend for a planet The planets in the 2nd 3rd 4th 10th 11th and 12th signs from any other planet becomes his Tatkalika friend. 
        :return: List`1
         """
        ...
    def GreenwichApparentInJulianDays(time: Time) -> Double:
        """
         Greenwich Apparent In Julian Days 
        :return: Double
         """
        ...
    def LocalApparentTime(time: Time) -> DateTime:
        """
         Shows local apparent time from Swiss Eph 
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
         House start middle and end longitudes 
        :return: House
         """
        ...
    def Panchaka(time: Time) -> PanchakaName:
        """
         Gets Panchaka at a given time 
        :return: PanchakaName
         """
        ...
    def LordOfWeekday(time: Time) -> PlanetName:
        """
         Planet lord that governs a weekday 
        :return: PlanetName
         """
        ...
    def LordOfWeekday(weekday: DayOfWeek) -> PlanetName:
        """
         Planet lord that governs a weekday 
        :return: PlanetName
         """
        ...
    def LmtToStd(lmtDateTime: DateTimeOffset, stdOffset: TimeSpan) -> DateTimeOffset:
        """
         Convert Local Mean Time LMT to Standard Time STD 
        :return: DateTimeOffset
         """
        ...
    def HoraAtBirth(time: Time) -> Int32:
        """
         A hora is equal to 124th part of a day. The Hindu day begins with sunrise and continues till next sunrise. The first hora on any day will be the first hour after sunrise and the last hora the hour before sunrise the next day. 
        :return: Int32
         """
        ...
    def PlanetHoraSign(planetName: PlanetName, time: Time) -> ZodiacName:
        """
         Gets hora zodiac sign of a planet 
        :return: ZodiacName
         """
        ...
    def SunriseTime(time: Time) -> Time:
        """
         get sunrise time for that day at that place 
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
         Checks if planet A is in good aspect to planet B Note A is transmitter B is receiver An aspect is good or bad according to the relation between the aspecting and the aspected body 
        :return: Boolean
         """
        ...
    def IsPlanetInGoodAspectToHouse(receivingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
        Checks if a planet is in good aspect to a house Note An aspect is good or bad according to the relation between the planet and lord of the house sign 
        :return: Boolean
         """
        ...
    def PlanetSthanaBalaNeutralPoint(planet: PlanetName) -> Double:
        """
         To determine if sthana bala is indicating good position or bad position a neutral point is set anything above is good below is bad Note Neutral point is derived from all possible sthana bala values across 25 years 20002025 with 1 hour granularity Formula used maxmin2min max hightest possible value min lowest possible value 
        :return: Double
         """
        ...
    def PlanetShadvargaBalaNeutralPoint(planet: PlanetName) -> Double:
        """
         EXPERIMENTAL To determine if Shadvarga bala is strong or weak a neutral point is set anything above is strong below is weak Note Neutral point is derived from all possible Shadvarga bala values across 25 years 20002025 with 1 hour granularity Formula used maxmin2min add min to get exact neutral point from 0 range max hightest possible value min lowest possible value 
        :return: Double
         """
        ...
    def IsPlanetInKendra(planet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is in a kendra house 14710 
        :return: Boolean
         """
        ...
    def IsPlanetInKendra(planetList: PlanetName, time: Time) -> Boolean:
        """
         Checks if any given planet is in a kendra house 14710 
        :return: Boolean
         """
        ...
    def IsPlanetInKendraFromPlanet(kendraFrom: PlanetName, kendraTo: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is in a kendra house 14710 from another planet. Exp Is Jupiter is in a kendra from the Moon 
        :return: Boolean
         """
        ...
    def SignDistanceFromPlanetToPlanet(startPlanet: PlanetName, endPlanet: PlanetName, time: Time) -> Int32:
        """
         Counts number of sign between 2 planets. 
        :return: Int32
         """
        ...
    def IsHouseLordInHouse(lordHouse: HouseName, occupiedHouse: HouseName, time: Time) -> Boolean:
        """
         Checks if the lord of a house is in the specified house. Example question Is Lord of 1st house in 2nd house 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithMaleficPlanets(planetName: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is conjuct with an evilmalefic planet 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is conjunct with an enemy planet by combined relationship 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is conjunct with an Friend planet by combined relationship 
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
         Checks if any evilmalefic planets are in a house Note Planet to house relationship not account for TODO Account for planet to sign relationship find reference 
        :return: Boolean
         """
        ...
    def IsBeneficPlanetInHouse(houseNumber: HouseName, time: Time) -> Boolean:
        """
         Checks if any goodbenefic planets are in a house Note Planet to house relationship not account for TODO Account for planet to sign relationship find reference 
        :return: Boolean
         """
        ...
    def IsMaleficPlanetInSign(sign: ZodiacName, time: Time) -> Boolean:
        """
         Checks if any evilmalefic planets are in a sign 
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
         Checks if any goodbenefic planets are in a sign 
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
         Checks if any evilmalefic planet is transmitting aspect to a house Note This does NOT account for bad aspects where relationship with house lord is checked TODO relationship aspect should be added get reference for it firsts 
        :return: Boolean
         """
        ...
    def IsBeneficPlanetAspectHouse(house: HouseName, time: Time) -> Boolean:
        """
         Checks if any goodbenefic planet is transmitting aspect to a house Note This does NOT account for good aspects where relationship with house lord is checked TODO relationship aspect should be added get reference for it firsts 
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByMaleficPlanets(lord: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is receiving aspects from an evil planet 
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByBeneficPlanets(lord: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is receiving aspects from an benefic planet 
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByEnemyPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is receiving aspects from an enemy planet based on combined relationship 
        :return: Boolean
         """
        ...
    def IsPlanetAspectedByFriendPlanets(inputPlanet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is receiving aspects from a Friend planet based on combined relationship 
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
         Counts from start sign to end sign Example Aquarius to Taurus is 4 
        :return: Int32
         """
        ...
    def CountFromConstellationToConstellation(start: PlanetConstellation, end: PlanetConstellation) -> Int32:
        """
         Counts from start Constellation to end Constellation Example Aquarius to Taurus is 4 
        :return: Int32
         """
        ...
    def IsPlanetInHouse(time: Time, planet: PlanetName, houseNumber: HouseName) -> Boolean:
        """
         Checks if a planet is in a given house at a specified time 
        :return: Boolean
         """
        ...
    def IsAllPlanetInHouse(time: Time, planetList: Any, houseNumber: HouseName) -> Boolean:
        """
         Checks if a planet is in a given house at a specified time 
        :return: Boolean
         """
        ...
    def IsAnyPlanetInHouse(time: Time, planetList: Any, houseNumber: HouseName) -> Boolean:
        """
         Checks if any planet in list is at a given house at a specified time 
        :return: Boolean
         """
        ...
    def IsPlanetDebilitated(planet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is in a longitude where its in Debilitated Note Rahu ketu accounted for 
        :return: Boolean
         """
        ...
    def IsPlanetExalted(planet: PlanetName, time: Time) -> Boolean:
        """
         Checks if a planet is in a longitude where its in Exaltation NOTE Rahu ketu accounted for Exaltation Each planet is held to be exalted when it is in a particular sign. The power to do good when in exaltation is greater than when in its own sign. Throughout the sign ascribed the planet is exalted but in a particular degree its exaltation is at the maximum level. 
        :return: Boolean
         """
        ...
    def LunarMonth(time: Time) -> LunarMonth:
        """
         Gets name of vedic month 
        :return: LunarMonth
         """
        ...
    def IsFullMoon(time: Time) -> Boolean:
        """
         Checks if the moon is FULL moon day 15 
        :return: Boolean
         """
        ...
    def IsWaterSign(moonSign: ZodiacName) -> Boolean:
        """
         Check if it is a Water Aquatic sign Water Signs this category include Cancer Scorpio and Pisces. 
        :return: Boolean
         """
        ...
    def IsFireSign(moonSign: ZodiacName) -> Boolean:
        """
         Check if it is a Fire sign Fire Signs this sign encloses Aries Leo and Sagittarius. 
        :return: Boolean
         """
        ...
    def IsEarthSign(moonSign: ZodiacName) -> Boolean:
        """
         Check if it is a Earth sign Earth Signs it contains Taurus Virgo and Capricorn. 
        :return: Boolean
         """
        ...
    def IsAirSign(moonSign: ZodiacName) -> Boolean:
        """
         Check if it is a Air Windy sign Air Signs this sign include Gemini Libra and Aquarius. 
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
         Soumyas Source Astrology for beginners pg 30 
        :return: Boolean
         """
        ...
    def IsPlanetMaleficToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
         Kruras Malefics Source Astrology for beginners pg 30 
        :return: Boolean
         """
        ...
    def IsPlanetYogakarakaToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
         Yogakaraka Planets indicating prosperity Source Astrology for beginners pg 30 
        :return: Boolean
         """
        ...
    def IsPlanetMarakaToLagna(planetName: PlanetName, lagna: ZodiacName) -> Boolean:
        """
         Yogakaraka Planets indicating prosperity Source Astrology for beginners pg 30 
        :return: Boolean
         """
        ...
    def IsPlanetInOwnHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
         Checks if planet is placed in own house meaning house sign owned by planet note rahu and ketu return false always 
        :return: Boolean
         """
        ...
    def IsPlanetInEnemyHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
         True if a planet is in a house sign owned by an enemy. Rahu and Ketu is false always 
        :return: Boolean
         """
        ...
    def IsPlanetInFriendHouse(time: Time, planetName: PlanetName) -> Boolean:
        """
         True if a planet is in a house sign owned by a friend. Rahu and Ketu is false always 
        :return: Boolean
         """
        ...
    def SwissEphemeris(time: Time, planetName: PlanetName) -> Object:
        """
         Get planets Longitude Latitude DistanceAU SpeedLongitude SpeedLatitude... Swiss Ephemeris swe_calc wrapper for open API 
        :return: Object
         """
        ...
    def IsPlanetSameHouseWithHouseLord(birthTime: Time, houseNumber: Int32, planet: PlanetName) -> Boolean:
        """
         Checks if a planet is same house not nessarly conjunct with the lord of a certain house Example Is Sun joined with lord of 9th 
        :return: Boolean
         """
        ...
    def HouseNatureScore(personBirthTime: Time, inputHouse: HouseName) -> Int32:
        """
         Based on Shadvarga get nature of house for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary 
        :return: Int32
         """
        ...
    def HouseNatureScoreMK4(personBirthTime: Time, inputHouse: HouseName) -> Double:
        """
         Experimental Code 
        :return: Double
         """
        ...
    def PlanetNatureScoreMK4(personBirthTime: Time, inputPlanet: PlanetName) -> Double:
        """
         Experimental Code stand back 
        :return: Double
         """
        ...
    def PlanetNatureScore(personBirthTime: Time, inputPlanet: PlanetName) -> Int32:
        """
         Based on Shadvarga get nature of planet for a person nature in number form to for easy calculation into summary good 1 bad 1 neutral 0 specially made method for life chart summary 
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
         Used for judging dasa good or bad Bala book pg 110 if planet has more Ishta than good 1 else if more Kashta than bad 1 
        :return: Double
         """
        ...
    def PlanetKashtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
         Experimental Code stand back Kashta Phala Bad Strength of a Planet 
        :return: Double
         """
        ...
    def PlanetIshtaScore(planet: PlanetName, birthTime: Time) -> Double:
        """
         Ishta Phala Good Strength of a Planet 
        :return: Double
         """
        ...
    def AllPlanetsSignsFromMoon(signsFromMoon: Int32, birthTime: Time) -> Any:
        """
         Gets all planets in certain sign from the moon. Exp get planets 3rd from the moon 
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromLagna(signsFromLagna: Int32, birthTime: Time) -> Any:
        """
         Gets all planets in certain sign from the LagnaAscendant. Exp get planets 3rd from the LagnaAscendant 
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromMoon(signsFromList: Int32, birthTime: Time) -> Any:
        """
         Gets all planets in certain sign from the moon given list of signs. Exp get planets 3rd from the moon 
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromList: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
         Gets all planets in certain sign from a given planet given list of signs. Exp get planets 3rd from the Jupiter 
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromPlanet(signsFromMoon: Int32, birthTime: Time, startPlanet: PlanetName) -> Any:
        """
         Gets all planets in certain sign from the planet. Exp get planets 3rd from the Jupiter 
        :return: List`1
         """
        ...
    def AllPlanetsSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Any:
        """
         Gets all planets in certain sign from the LagnaAscendant given list of signs. Exp get planets 3rd from the LagnaAscendant 
        :return: List`1
         """
        ...
    def IsPlanetsInSignsFromMoon(signsFromList: Int32, planetList: PlanetName, birthTime: Time) -> Boolean:
        """
         Checks if a given list of planets are found in any inputed signs from moon Exp Is Sun or Moon in 6 or 7th from Moon 
        :return: Boolean
         """
        ...
    def IsPlanetsInSignsFromPlanet(signsFromList: Int32, planetList: PlanetName, startPlanet: PlanetName, birthTime: Time) -> Boolean:
        """
         Checks if a given list of planets are found in any inputed signs from another planet Exp Is Sun or Moon in 6 or 7th from Moon 
        :return: Boolean
         """
        ...
    def IsPlanetsInSignsFromLagna(signsFromList: Int32, planetList: PlanetName, birthTime: Time) -> Boolean:
        """
         Checks if a given list of planets are found in any inputed signs from LagnaAscendant Exp Is Sun or Moon in 6 or 7th from Lagna 
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromMoon(signsFromList: Int32, birthTime: Time) -> Boolean:
        """
         Checks if benefics are found in any inputed signs from moon Exp Is benefics in 6 7th from moon 
        :return: Boolean
         """
        ...
    def IsBeneficsInSignsFromLagna(signsFromList: Int32, birthTime: Time) -> Boolean:
        """
         Checks if benefics are found in any inputed signs from LagnaAscendant Exp Is benefics in 6 7th from moon 
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
         Get fixed longitude used in western systems connects SwissEph Library with VedAstro NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def NextLunarEclipse(time: Time) -> DateTime:
        """
         find time of next lunar eclipse UTC time 
        :return: DateTime
         """
        ...
    def NextSolarEclipse(time: Time) -> DateTime:
        """
         finds the next solar eclipse globally UTC time 
        :return: DateTime
         """
        ...
    def PlanetEphemerisLongitude(time: Time, planetName: PlanetName) -> Angle:
        """
         Get fixed longitude used in western systems aka Sayana longitude NOTE This method connects SwissEph Library with VedAstro Library 
        :return: Angle
         """
        ...
    def PlanetSayanaLatitude(time: Time, planetName: PlanetName) -> Angle:
        """
         Gets Swiss Ephemeris longitude for a planet 
        :return: Angle
         """
        ...
    def PlanetSpeed(time: Time, planetName: PlanetName) -> Double:
        """
         Speed of planet from Swiss eph 
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
         Get Day Of Week 
        :return: DayOfWeek
         """
        ...
    def LordOfHora(hora: Int32, day: DayOfWeek) -> PlanetName:
        """
         Gets hora lord based on hora number week day 
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
         Gets planet which is the lord of a given sign 
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
         Gets next house number after input house number goes to 1 after 12 
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
         Returns true if zodiac sign is an Even sign Yugma Rasis 
        :return: Boolean
         """
        ...
    def IsOddSign(planetSignName: ZodiacName) -> Boolean:
        """
         Returns true if zodiac sign is an Odd sign Oja Rasis 
        :return: Boolean
         """
        ...
    def IsFixedSign(sunSign: ZodiacName) -> Boolean:
        """
         Fixed signs Taurus Leo Scropio Aquarius. 
        :return: Boolean
         """
        ...
    def IsMovableSign(sunSign: ZodiacName) -> Boolean:
        """
         Movable signs Aries Cancer Libra Capricorn. 
        :return: Boolean
         """
        ...
    def IsCommonSign(sunSign: ZodiacName) -> Boolean:
        """
         Common signs Gemini Virgo Sagitarius Pisces. 
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
         Converts julian time to normal time normal time can be lmt lat utc 
        :return: DateTime
         """
        ...
    def GreenwichTimeFromJulianDays(julianTime: Double) -> DateTimeOffset:
        """
         Gets Greenwich time in normal format from Julian days at Greenwich Note Inputed time is Julian days at greenwich callers reponsibility to make sure 
        :return: DateTimeOffset
         """
        ...
    def GreenwichLmtInJulianDays(time: Time) -> Double:
        """
         Gets Local mean time LMT at Greenwich UTC in Julian days based on the inputed time 
        :return: Double
         """
        ...
    def GetHouse1And10Longitudes(time: Time) -> Double:
        """
         Gets the longitude of house 1 and house 10 using Swiss Epehemris swe_houses 
        :return: Double[]
         """
        ...
    def LmtToUtc(time: Time) -> DateTimeOffset:
        """
         Converts Local Mean Time LMT to Universal Time UTC 
        :return: DateTimeOffset
         """
        ...
    def GocharaHouse(birthTime: Time, currentTime: Time, planet: PlanetName) -> Int32:
        """
         Gets the Gochara House number which is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: Int32
         """
        ...
    def IsGocharaObstructed(planet: PlanetName, gocharaHouse: Int32, birthTime: Time, currentTime: Time) -> Boolean:
        """
         Check if there is an obstruction to a given Gochara obstructing housepoint Vedhanka 
        :return: Boolean
         """
        ...
    def PlanetsInGocharaHouse(birthTime: Time, currentTime: Time, gocharaHouse: Int32) -> Any:
        """
         Gets all the planets in a given Gochara House Note Gochara House number is the count from birth Moon sign janma rasi to the sign the planet is at the current time. Gochara Transits 
        :return: List`1
         """
        ...
    def Vedhanka(planet: PlanetName, house: Int32) -> Int32:
        """
         Gets the Vedhanka point of obstruction used for Gohchara calculations. The data returned comes from a fixed table. NOTE Planet exceptions are not accounted for here. Return 0 when no obstruction point exists Reference Hindu Predictive Astrology pg. 257 
        :return: Int32
         """
        ...
    def IsGocharaOccurring(birthTime: Time, time: Time, planet: PlanetName, gocharaHouse: Int32) -> Boolean:
        """
         Is SunGocharaInHouse1 Checks if a Gochara is occuring for a planet in a given house without any obstructions at a given time Note Basically a wrapper method for Gochra event calculations 
        :return: Boolean
         """
        ...
    def IsPlanetGocharaBindu(birthTime: Time, nowTime: Time, planet: PlanetName, bindu: Int32) -> Boolean:
        """
         SunTransit8Bindu Checks if a given planets with given number of bindu is transiting now Gochara 
        :return: Boolean
         """
        ...
    def PlanetAshtakvargaBindu(planet: PlanetName, signToCheck: ZodiacName, time: Time) -> Int32:
        """
         Give a planet and sign and ashtakvarga bindu can be calculated EXP In the Suns own Ashtakvarga there are 5 bindus in Aries NOTE ON USE Ashtakvarga System pg.128 For example in the Standard Horoscope the Suns transit of Aries 3rd from Moon should prove favourable. In the Suns own Ashtakvarga there are 5 bindus in Aries. Therefore the good effects produced should be to the extent of 62. The Suns transit of Capricorn 12th from the Moon should prove adverse. Capricorn has no bindus.Therefore the evil results to be produced by this transit are to the brim. 
        :return: Int32
         """
        ...
    def AllBhinnashtakavargaChart(birthTime: Time) -> Any:
        """
         Bhinnashtakavarga or individual Ashtakvarga charts Made on cold winter morning in July 
        :return: Dictionary`2
         """
        ...
    def PlanetBhinnashtakavargaChart(mainPlanet: PlanetName, birthTime: Time) -> Any:
        """
         Calculates full ashtakvarga chart for a given planet for all 12 signs Needed to compute final ashtakvarga 
        :return: Dictionary`2
         """
        ...
    def GetPlanetBeneficHouseAshtakvarga(mainPlanet: String, minorPlanet: String) -> Int32:
        """
         This a constant that does not change when calculating ashtakvarga this is the constant count used data from ashtakvarga table Ashtakvarga System pg.9 Code Once this data was memorized by human minds today it is programmed by human hands 
        :return: Int32[]
         """
        ...
    def GetPlanetDasaMajorPlanetAndMinorRelationship(majorPlanet: PlanetName, minorPlanet: PlanetName) -> Any:
        """
         Gets the relationship between a mojor period planet and minor period planet based solely on relationship between the planets and nothing to do with the signs yet based on cyclic relationship between planets 
        :return: ValueTuple`2
         """
        ...
    def CurrentDasaCountFromBirth(birthTime: Time, currentTime: Time) -> Int32:
        """
         Gets dasa counted from birth dasa 
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
         Counts from inputed dasa by years to dasa bhukti antaram Inputed planet is taken as birth dasa starting dasa to count from Note It is easier to calculate from start of Dasa so years already traversed at birth must be added into inputed years Exp Get dasa bhukti antaram planet 3.5 years from start of Sun dasa 
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
         Gets years left in birth dasa at birth Note Returned years can only be 0 or above Start constellation can be of moon or Lagna 
        :return: Double
         """
        ...
    def YearsTraversedInBirthDasa(birthTime: Time, startConstellation: PlanetConstellation) -> Double:
        """
         Gets the time in years traversed in Dasa at birth Start constellation can of Moons or Lagna lord 
        :return: Double
         """
        ...
    def DasaTimePerMinute(constellationName: ConstellationName) -> Double:
        """
         Gets the Dasa time period each longitude minute in a constellation represents based on the planet which is related lord to it. Note Returns the time in years exp 0.5 half year 
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
         Gets the full Dasa years for a given planet Note Returns double so that division down the road is accurate RefHindu Predictive Astrology pg. 54 
        :return: Double
         """
        ...
    def PD2PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName) -> Double:
        """
         Gets the full years of a bhukti planet in a dasa 
        :return: Double
         """
        ...
    def PD3PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName) -> Double:
        """
         Gets the full years of an antaram planet in a bhukti of a dasa 
        :return: Double
         """
        ...
    def PD4PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName) -> Double:
        """
         Gets the full time of an Sukshma planet Sukshma is a Sanskrit word meaning subtle or dormant. The presence of sukshma is felt but not seen. 
        :return: Double
         """
        ...
    def PD5PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName) -> Double:
        """
         Gets the full time of an Prana planet 
        :return: Double
         """
        ...
    def PD6PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName) -> Double:
        """
        Empty sample text
        :return: Double
         """
        ...
    def PD7PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName, pd7Planet: PlanetName) -> Double:
        """
        Empty sample text
        :return: Double
         """
        ...
    def PD8PlanetFullYears(pd1Planet: PlanetName, pd2Planet: PlanetName, pd3Planet: PlanetName, pd4Planet: PlanetName, pd5Planet: PlanetName, pd6Planet: PlanetName, pd7Planet: PlanetName, pd8Planet: PlanetName) -> Double:
        """
        Empty sample text
        :return: Double
         """
        ...
    def IsMercuryAfflicted(time: Time) -> Boolean:
        """
         Whenever an affiiction by way of a malefic occupying a certain house or joining with a certain planet is suggested by implication an aspect is also meant though an affliction caused by aspect.is comparatively less malevolent Note TODO presently not 100 sure if what is meant by affliction is solely only limited to aspects conjunction with bad planets. Or Located in enemy sign an affliction Low shadbala an affliction Low drikbala an affliction At present malefic aspects conjunctions are used becasue it seems based on texts that this is correct. But it seems mercury in enemny sign or position in a house should also play a role. There must be a corelation between shadbala or drikbala to aspects conjucntion A more precise way of mesurement it could be via the bala method. Needs testing for sure to find out what bala values determine an afflicted mercury 
        :return: Boolean
         """
        ...
    def IsMercuryMalefic(time: Time) -> Boolean:
        """
         Check if Mercury is malefic true returns false if benefic References Mercury by nature is called sournya or good. And if he is in conjunction with the Sun Saturn Mars Rahu or Ketu he will be a malefic. His conjunction with beneficial planets like Full Moon Jupiter or Venus will classify him as a benefic. Benefic means a good and malefic means an evil planet. TODO Does malefic moon make it malefic atm malefic moon makes it malefic Though in the earlier pages Mercury is defined either as a subba benefic or papa malefic according to its association is with a benefic or malefic Mercury for purposes of calculating Drisbtibala of Bbavas is to be deemed as a full benefic. This is in accord with the injunctions of classical writers Gurugnabbyam tu yuktasya poomamekam tu yojayet. 11. Benefics and Malefics. Among these Srya ani Mangal decreasing Candr Rahu and Ketu the ascending and the descending nodes of Candr are malefics while the rest are benefics. Budh however is a malefic if he joins a malefic. Note ATM malefic planets override benefic TODO not sure if malefic planet overrides benefic if both are conjunct 
        :return: Boolean
         """
        ...
    def IsMoonBenefic(time: Time) -> Boolean:
        """
         Moon is a benefic from the 8th day of the bright half of the lunar month to the 8th day of the dark half of the lunar month and a malefic in the rest of the days. Returns true if benefic false if malefic 
        :return: Boolean
         """
        ...
    def IsPlanetBenefic(planetName: PlanetName, time: Time) -> Boolean:
        """
         Checks if a given planet is benefic 
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
         Checks if a given planet is Malefic 
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
         Checks if the a planet is aspected by another planet 
        :return: Boolean
         """
        ...
    def IsHouseAspectedByPlanet(receiveingAspect: HouseName, transmitingAspect: PlanetName, time: Time) -> Boolean:
        """
         Checks if a house is aspected by a planet 
        :return: Boolean
         """
        ...
    def IsPlanetConjunctWithPlanet(planetA: PlanetName, planetB: PlanetName, time: Time) -> Boolean:
        """
         Checks if the a planet is conjunct with another planet Note Both planets A B are checked if they are in conjunct with each other performance might be effected mildly but errors in conjunction calculation would be caught here. Can be removed once conjunction calculator is confirmed accurate. 
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
         Significance of being Powerful.Among the several planets associated with a bhava that which has the greatest Sbadbala influences the bhava most. Powerful Planets.Ravi is befd to be powerful when hiShadbala Pinda is 5 or more rupas. Chandra becomes strong when his Shadbala Pinda is 6 or more rupas. Kuja becomes powerful when bis Shadbala Pinda does not fall short of 5 rupas.Budha becomes potent by having his Sbadbala Pinda as 7 rupas Guru Sukra and Sani become thoroughly powerful if their Shadbala Pindas are 6.5 5.5 and 5 rupas or more respectively. 
        :return: Boolean
         """
        ...
    def IsHouseBeneficInShadbala(house: HouseName, birthTime: Time, threshold: Double) -> Boolean:
        """
        Empty sample text
        :return: Boolean
         """
        ...
    def AllPlanetStrength(time: Time) -> Any:
        """
         Gets strength shadbala of all 9 planets 
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
         Get special aspect if any of Kuja Guru and Sani 
        :return: Double
         """
        ...
    def FindDrishtiValue(dk: Double) -> Double:
        """
        Empty sample text
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
         NOTE sun moon get score for ISHTAKESHA calculation TODO MOTIONAL STRENGTH Chesta here means Vakra Chesta or act of retrogression. Each planet except the Sun and the Moon and shadowy planets get into the state of Vakra or retrogression when its distance from the Sun exceeds a particular limit. And the strength or potency due to the planet on account of the arc of the retrogression is termed as Chesta Bala Deduct from the Seeghrocbcha half the sum of the True and Mean Longitudes of planets and divide the difference by 3. The quotient is the Chestabala. Max 60 meaning RetrogradeVakra When the distance of any one planet from the Sun exceeds a particular limit it becomes retrograde i.e. when the planet goes from perihelion the point in a planets orbit nearest to the Sun to aphelion the part of a planets oroit most distant from the Sun as it recedes from the Sun it gradually loses the power of the Suns gravitation and consequently 
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
         The mean position of a planet is the position which it would have attained at a uniform rate of motion and the corrections to be applied in respect of the eccentricity of the orbit are not considered 
        :return: Dictionary`2
         """
        ...
    def EpochInterval(time1: Time) -> Double:
        """
         Get interval from the epoch to the birth date in days The result represents the interval from the epoch to the birth date. 
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
         circulation time of the objects in years used by cheshta bala calculation 
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
         TODO use of shadvarga bala might be wrong here needs clarification problem is too much of time goes under bad doesnt seem right for now we put it 140 threhold so guarenteed to be strong and doesn not occur all the time 
        :return: Boolean
         """
        ...
    def PlanetSthanaBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         residence of the planet and as such a certain degree of strength or weakness attends on it Positonal strength A planet occupies a certain sign in a Rasi and friendly neutrai or inimical varga. It is either exalted or debilitated lt ocupies its Moolathrikona or it has its own varga. All these states refer to the position or residence of the planet and as such a certain degree of strength or weakness attends on it. This strength or potency is known as the Sthanabala. 1.Uccha Bala Uccha means exaltation. When a planet is placed in its highest exaltation point it is of full strength and when it is in its deepest debilitation point it is devoid of any strength. When in between the strength is calculated proportionately dependent on the distance these planets are placed from the highest exaltation or deepest debilitation point. 2.Sapta Vargiya Bala Rashi Hora Drekkana Saptamsha Navamsha Dwadasamsha and Trimsamsha constitute the Sapta Varga. The strength of the planets in these seven divisional charts based on their placements in Mulatrikona own sign friendly sign etc. constitute the Sapta vargiya bala. 3.OjaYugma RashiAmsha Bala Oja means odd signs and Yugma means even signs. Thus as the name imply this strength is derived from a planets placement in the odd or even signs in the Rashi and Navamsha. 4.Kendradi Bala The name itself implies how to compute this strength. A planet in a Kendra 14710 gets full strength while one in Panapara 25811 gets half and the one in Apoklimas 12369 gets quarter strength. 5.Drekkana Bala Due to placement in first second or third Drekkana of a sign male female and hermaphrodite planets respectively get a quarter strength according to placements in the first second and third Drekkana. 
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
         Gets a planets Kala Bala or Temporal strength 
        :return: Shashtiamsa
         """
        ...
    def PlanetYuddhaBala(inputedPlanet: PlanetName, preKalaBalaValues: Any, time: Time) -> Shashtiamsa:
        """
         Two planets are said to be in Yuddha or fight when they are in conjunction and the distance between them is less than one degree. TODO Not fully tested Yuddhabala All planets excepting the Sun and the Moon enter into war when two planets are in the same degree. The pJanet having the lesser longitude is the winner. Find out the sum total of the SthanabaJa Kalabala and Digbala of these two planets. Difference between the two divided by the difference of their diameters of its disc gives the Yuddhabala. Add this to the victorious planet and dedu_ct it from the vanquished. 
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
         A heavenly body moves northwards the equator for sometime and then gets southwards. This angular distance from the equinoctial or celestial equator is Kranti or the declination. Declinations are reckoned plus or minus according as the planet is situated in the northern or southern celestial hemisphere 
        :return: Double
         """
        ...
    def EclipticObliquity(time: Time) -> Double:
        """
         true obliquity of the Ecliptic includes nutation 
        :return: Double
         """
        ...
    def PlanetHoraBala(planetName: PlanetName, time: Time) -> Shashtiamsa:
        """
         Hora Bala AKA Horadhipathi Bala 
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
         Gets a planets masa bala the lord of the month of birth is assigned a value of 30 Shashtiamsas as his Masabala 
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
         Gets year month lord at inputed time 
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
         Determines if the input time is day during day used for birth times if day returns true 
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
         Gets Dig Bala of a planet. Jupiter and Mercury are strong in Lagna Ascendant the Sun and Mars in the 10th Saturn in the 7th and the Moon and Venus in the 4th. The opposite houses are weak points. Divide the distance between the longitude of the planet and its depression point by 3. Quotient is the strength. 
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
         House received aspect strength Bhavadrishti Bala.Each bhava in a horoscope remains aspected by certain planets. Sometimes the aspect cast on a bhava will be positive and sometimes it will be negative according as it is aspected by benefics or malefics. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def CalcBhavaDigBala(time: Time) -> HouseSubStrength:
        """
         House strength from different types of signs Bhava Digbala.This is the strength acquired by the different bhavas falling in the different groups or types of signs. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BhavaAdhipathiBala(time: Time) -> HouseSubStrength:
        """
         Bhavadhipatbi Bala This is the potency of the lord of the bhava. For all 12 houses 
        :return: HouseSubStrength
         """
        ...
    def BeneficPlanetListByShadbala(personBirthTime: Time, threshold: Int32) -> Any:
        """
         0 index is strongest 
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
         0 index is strongest 
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
        Empty sample text
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
         0 index is most malefic 
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
         keywords or tag related to a house 
        :return: String
         """
        ...
    def GetSignTags(zodiacName: ZodiacName) -> String:
        """
         Given a zodiac sign will return astro keywords related to sign These details would be highly useful in the delineation of character and mental disposition SourceHindu Predictive Astrology pg.16 
        :return: String
         """
        ...
    def GetPlanetTags(lordOfHouse: PlanetName) -> String:
        """
         Get keywords related to a planet. 
        :return: String
         """
        ...
    def GetHouseType(houseNumber: HouseName) -> String:
        """
         Source Hindu Predictive Astrology pg.17 
        :return: String
         """
        ...
    def GetDasaInfoForAscendant(ascendantName: ZodiacName) -> String:
        """
         Get general planetary info for persons dasa hardcoded table It is intended to be used to interpret dasa predictions as such should be displayed next to dasa chart. This method is direct translation from the book. Similar to method GetPlanetDasaNature Data from pg 80 of Keyplanets for Each Sign in Hindu Predictive Astrology 
        :return: String
         """
        ...

