from typing import List, Tuple, Dict

import VedAstro.Library as libray

from vedastro.objects import Time, Person
from vedastro.objects.angle import Angle
from vedastro.objects.constellationanimal import ConstellationAnimal
from vedastro.objects.constellationname import ConstellationName
from vedastro.objects.dasas import Dasas
from vedastro.objects.datetime_offset import DateTimeOffset
from vedastro.objects.dayofweek import DayOfWeek
from vedastro.objects.eventnature import EventNature
from vedastro.objects.house import House
from vedastro.objects.housename import HouseName
from vedastro.objects.housesubstrength import HouseSubStrength
from vedastro.objects.karana import Karana
from vedastro.objects.lunarday import LunarDay
from vedastro.objects.lunarmonth import LunarMonth
from vedastro.objects.nithyayoga import NithyaYoga
from vedastro.objects.panchaka_name import PanchakaName
from vedastro.objects.planetconstellation import PlanetConstellation
from vedastro.objects.planetlongitude import PlanetLongitude
from vedastro.objects.planetmotion import PlanetMotion
from vedastro.objects.planetname import PlanetName
from vedastro.objects.planettoplanetrelationship import PlanetToPlanetRelationship
from vedastro.objects.planettosignrelationship import PlanetToSignRelationship
from vedastro.objects.shashtiamsa import Shashtiamsa
from vedastro.objects.tarabala import Tarabala
from vedastro.objects.timespan import TimeSpan
from vedastro.objects.zodiacname import ZodiacName
from vedastro.objects.zodiacsign import ZodiacSign


#  var lordOfHouse = AstronomicalCalculator.GetLordOfHouse((HouseName)houseNumber, _time);


def get_lord_of_house(house_number: HouseName, time: Time):
    return libray.AstronomicalCalculator.GetLordOfHouse(house_number, time)


def time_to_longitude(time: TimeSpan) -> Angle:
    return libray.AstronomicalCalculator.TimeToLongitude(time)


def time_to_ephemeris_time(time: Time) -> float:
    return libray.AstronomicalCalculator.TimeToEphemerisTime(time)


def get_planet_nirayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return libray.AstronomicalCalculator.GetPlanetNirayanaLongitude(time, planet_name)


def get_lunar_day(time: Time) -> LunarDay:
    return libray.AstronomicalCalculator.GetLunarDay(time)


def get_moon_constellation(time: Time) -> PlanetConstellation:
    return libray.AstronomicalCalculator.GetPlanetConstellation(time, PlanetName.Moon)


def get_planet_constellation(time: Time, planet: PlanetName) -> PlanetConstellation:
    return libray.AstronomicalCalculator.GetPlanetConstellation(time, planet)


def get_tarabala(time: Time, person: Person) -> Tarabala:
    return libray.AstronomicalCalculator.GetTarabala(time, person)


def get_chandrabala(time: Time, person: Person) -> int:
    return libray.AstronomicalCalculator.GetChandrabala(time, person)


def get_moon_sign_name(time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetMoonSignName(time)


def get_nithya_yoga(time: Time) -> NithyaYoga:
    return libray.AstronomicalCalculator.GetNithyaYoga(time)


def get_karana(time: Time) -> Karana:
    return libray.AstronomicalCalculator.GetKarana(time)


def get_sun_sign(time: Time) -> ZodiacSign:
    return libray.AstronomicalCalculator.GetSunSign(time)


def get_time_sun_entered_current_sign(time: Time) -> Time:
    return libray.AstronomicalCalculator.GetTimeSunEnteredCurrentSign(time)


def get_time_sun_leaves_current_sign(time: Time) -> Time:
    return libray.AstronomicalCalculator.GetTimeSunLeavesCurrentSign(time)


def get_houses(time: Time) -> List[House]:
    return libray.AstronomicalCalculator.GetHouses(time)


def convert_lmt_to_julian(time: Time) -> float:
    return libray.AstronomicalCalculator.ConvertLmtToJulian(time)


def get_planets_in_conjunction(time: Time, inputed_planet_name: PlanetName) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsInConjuction(time, inputed_planet_name)


def get_distance_between_planets(planet1: PlanetName, planet2: PlanetName, time: Time) -> Angle:
    return libray.AstronomicalCalculator.GetDistanceBetweenPlanets(planet1, planet2, time)


def get_distance_between_planets_angle(planet1: Angle, planet2: Angle) -> Angle:
    return libray.AstronomicalCalculator.GetDistanceBetweenPlanets(planet1, planet2)


def get_planets_in_house(house_number: int, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsInHouse(house_number, time)


def get_all_planet_longitude(time: Time) -> List[PlanetLongitude]:
    return libray.AstronomicalCalculator.GetAllPlanetLongitude(time)


def get_all_planet_fixed_longitude(time: Time) -> List[PlanetLongitude]:
    return libray.AstronomicalCalculator.GetAllPlanetFixedLongitude(time)


def get_house_planet_is_in(time: Time, planet_name: PlanetName) -> int:
    return libray.AstronomicalCalculator.GetHousePlanetIsIn(time, planet_name)


def get_lord_of_house_list(house_list: List[HouseName], time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetLordOfHouseList(house_list, time)


def is_house_sign_name(house: int, sign: ZodiacName, time: Time) -> bool:
    return libray.AstronomicalCalculator.GetHouseSignName(house, time) == sign


def get_house_sign_name(house_number: int, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetHouseSignName(house_number, time)


def get_navamsa_sign_name_from_longitude(longitude: Angle) -> ZodiacName:
    return libray.AstronomicalCalculator.GetNavamsaSignNameFromLongitude(longitude)


def get_sign_counted_from_input_sign(input_sign: ZodiacName, count_to_next_sign: int) -> ZodiacName:
    return libray.AstronomicalCalculator.GetSignCountedFromInputSign(input_sign, count_to_next_sign)


def get_house_counted_from_input_house(input_house_number: int, count_to_next_house: int) -> int:
    return libray.AstronomicalCalculator.GetHouseCountedFromInputHouse(input_house_number, count_to_next_house)


def get_planet_rasi_sign(planet_name: PlanetName, time: Time) -> ZodiacSign:
    return libray.AstronomicalCalculator.GetPlanetRasiSign(planet_name, time)


def is_planet_in_sign(planet_name: PlanetName, sign_input: ZodiacName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInSign(planet_name, sign_input, time)


def get_planet_navamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetNavamsaSign(planet_name, time)


def get_house_navamsa_sign(house: HouseName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetHouseNavamsaSign(house, time)


def get_planet_thrimsamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetThrimsamsaSign(planet_name, time)


def get_planet_dwadasamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetDwadasamsaSign(planet_name, time)


def get_planet_saptamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetSaptamsaSign(planet_name, time)


def get_planet_drekkana_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetDrekkanaSign(planet_name, time)


def is_planet_in_moolatrikona(planet_name: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInMoolatrikona(planet_name, time)


def get_planet_relationship_with_sign(planet_name: PlanetName, zodiac_sign_name: ZodiacName,
                                      time: Time) -> PlanetToSignRelationship:
    return libray.AstronomicalCalculator.GetPlanetRelationshipWithSign(planet_name, zodiac_sign_name, time)


def get_planet_combined_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                 time: Time) -> PlanetToPlanetRelationship:
    return libray.AstronomicalCalculator.GetPlanetCombinedRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_relationship_with_house(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
    return libray.AstronomicalCalculator.GetPlanetRelationshipWithHouse(house, planet, time)


def get_planet_temporary_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                  time: Time) -> PlanetToPlanetRelationship:
    return libray.AstronomicalCalculator.GetPlanetTemporaryRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_temporary_enemy_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetTemporaryEnemyList(planet_name, time)


def get_planet_in_sign(sign_name: ZodiacName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetInSign(sign_name, time)


def get_planet_temporary_friend_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetTemporaryFriendList(planet_name, time)


def get_greenwich_apparent_in_julian_days(time: Time) -> float:
    return libray.AstronomicalCalculator.GetGreenwichApparentInJulianDays(time)


def get_local_apparent_time(time: Time):
    return libray.AstronomicalCalculator.GetLocalApparentTime(time)


def get_local_mean_time(time: Time) -> DateTimeOffset:
    return time.GetLmtDateTimeOffset()


def get_house(house_number: HouseName, time: Time) -> House:
    return libray.AstronomicalCalculator.GetHouse(house_number, time)


def get_panchaka(time: Time) -> PanchakaName:
    return libray.AstronomicalCalculator.GetPanchaka(time)


def get_lord_of_weekday(time: Time) -> PlanetName:
    return libray.AstronomicalCalculator.GetLordOfWeekday(time)


def get_lord_of_weekday(weekday: DayOfWeek) -> PlanetName:
    return libray.AstronomicalCalculator.GetLordOfWeekday(weekday)


def lmt_to_std(lmt_date_time: DateTimeOffset, std_offset: TimeSpan) -> DateTimeOffset:
    return libray.AstronomicalCalculator.LmtToStd(lmt_date_time, std_offset)


def get_hora_at_birth(time: Time) -> int:
    return libray.AstronomicalCalculator.GetHoraAtBirth(time)


def get_planet_hora_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetPlanetHoraSign(planet_name, time)


def get_sunrise_time(time: Time) -> Time:
    return libray.AstronomicalCalculator.GetSunriseTime(time)


def get_sunset_time(time: Time) -> Time:
    return libray.AstronomicalCalculator.GetSunsetTime(time)


def get_noon_time(time: Time):
    return libray.AstronomicalCalculator.GetNoonTime(time)


def is_planet_in_good_aspect_to_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName,
                                       time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInGoodAspectToPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_in_good_aspect_to_house(receiving_aspect: PlanetName, transmitting_aspect: HouseName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInGoodAspectToHouse(receiving_aspect, transmitting_aspect, time)


def get_planet_sthana_bala_neutral_point(planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPlanetSthanaBalaNeutralPoint(planet)


def get_planet_shadvarga_bala_neutral_point(planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPlanetShadvargaBalaNeutralPoint(planet)


def is_planet_in_kendra(planet: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInKendra(planet, time)


def is_house_lord_in_house(lord_house: HouseName, occupied_house: HouseName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsHouseLordInHouse(lord_house, occupied_house, time)


def is_planet_conjunct_with_malefic_planets(planet_name: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetConjunctWithMaleficPlanets(planet_name, time)


def is_malefic_planet_in_house(house_number: int, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMaleficPlanetInHouse(house_number, time)


def is_benefic_planet_in_house(house_number: int, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsBeneficPlanetInHouse(house_number, time)


def is_malefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMaleficPlanetInSign(sign, time)


def get_malefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetMaleficPlanetListInSign(sign, time)


def is_benefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsBeneficPlanetInSign(sign, time)


def get_benefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetBeneficPlanetListInSign(sign, time)


def is_malefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMaleficPlanetAspectHouse(house, time)


def is_benefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsBeneficPlanetAspectHouse(house, time)


def is_planet_aspected_by_malefic_planets(lord: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetAspectedByMaleficPlanets(lord, time)


def get_arudha_lagna_sign(time: Time) -> ZodiacName:
    return libray.AstronomicalCalculator.GetArudhaLagnaSign(time)


def count_from_sign_to_sign(start_sign: ZodiacName, end_sign: ZodiacName) -> int:
    return libray.AstronomicalCalculator.CountFromSignToSign(start_sign, end_sign)


def count_from_constellation_to_constellation(start: PlanetConstellation, end: PlanetConstellation) -> int:
    return libray.AstronomicalCalculator.CountFromConstellationToConstellation(start, end)


def is_planet_in_house(time: Time, planet: PlanetName, house_number: int) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInHouse(time, planet, house_number)


def is_planet_debilitated(planet: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetDebilitated(planet, time)


def is_planet_exalted(planet: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetExalted(planet, time)


def get_lunar_month(time: Time) -> LunarMonth:
    return libray.AstronomicalCalculator.GetLunarMonth(time)


def is_full_moon(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsFullMoon(time)


def is_aquatic_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Cancer, ZodiacName.Scorpio, ZodiacName.Pisces]


def is_fire_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Aries, ZodiacName.Leo, ZodiacName.Sagittarius]


def is_earth_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Taurus, ZodiacName.Virgo, ZodiacName.Capricornus]


def is_air_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Gemini, ZodiacName.Libra, ZodiacName.Aquarius]


def get_planet_antaram_nature(person: Person, planet: PlanetName) -> EventNature:
    return libray.AstronomicalCalculator.GetPlanetAntaramNature(person, planet)


def is_planet_benefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetBeneficToLagna(planet_name, lagna)


def is_planet_malefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetMaleficToLagna(planet_name, lagna)


def is_planet_yogakaraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetYogakarakaToLagna(planet_name, lagna)


def is_planet_maraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetMarakaToLagna(planet_name, lagna)


def is_planet_in_own_house(time: Time, planet_name: PlanetName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetInOwnHouse(time, planet_name)


def swe_calc_wrapper(time: Time, planet_name: PlanetName):
    return libray.AstronomicalCalculator.swe_calc_wrapper(time, planet_name)


def is_planet_same_house_with_house_lord(birth_time: Time, house_number: int, planet: PlanetName) -> bool:
    return libray.AstronomicalCalculator.IsPlanetSameHouseWithHouseLord(birth_time, house_number, planet)


def get_time_house_calcs():
    return libray.AstronomicalCalculator.GetTimeHouseCalcs()


def is_moon_weak(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMoonWeak(time)


def is_moon_strong(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMoonStrong(time)


def get_ayanamsa(time: Time) -> Angle:
    return libray.AstronomicalCalculator.GetAyanamsa(time)


def get_planet_sayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return libray.AstronomicalCalculator.GetPlanetSayanaLongitude(time, planet_name)


def get_planet_sayana_latitude(time: Time, planet_name: PlanetName) -> Angle:
    return libray.AstronomicalCalculator.GetPlanetSayanaLatitude(time, planet_name)


def get_planet_speed(time: Time, planet_name: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPlanetSpeed(time, planet_name)


def get_constellation_at_longitude(planet_longitude: Angle) -> PlanetConstellation:
    return libray.AstronomicalCalculator.GetConstellationAtLongitude(planet_longitude)


def get_zodiac_sign_at_longitude(longitude: Angle) -> ZodiacSign:
    return libray.AstronomicalCalculator.GetZodiacSignAtLongitude(longitude)


def get_longitude_at_zodiac_sign(zodiac_sign: ZodiacSign) -> Angle:
    return libray.AstronomicalCalculator.GetLongitudeAtZodiacSign(zodiac_sign)


def get_day_of_week(time: Time) -> DayOfWeek:
    return libray.AstronomicalCalculator.GetDayOfWeek(time)


def get_lord_of_hora(hora: int, day: DayOfWeek) -> PlanetName:
    return libray.AstronomicalCalculator.GetLordOfHora(hora, day)


def get_house_junction_point(previous_house: Angle, next_house: Angle) -> Angle:
    return libray.AstronomicalCalculator.GetHouseJunctionPoint(previous_house, next_house)


def get_lord_of_zodiac_sign(sign_name: ZodiacName) -> PlanetName:
    return libray.AstronomicalCalculator.GetLordOfZodiacSign(sign_name)


def get_next_zodiac_sign(input_sign: ZodiacName) -> ZodiacName:
    return libray.AstronomicalCalculator.GetNextZodiacSign(input_sign)


def get_next_house_number(input_house_number: int) -> int:
    return libray.AstronomicalCalculator.GetNextHouseNumber(input_house_number)


def get_planet_exaltation_point(planet_name: PlanetName) -> ZodiacSign:
    return libray.AstronomicalCalculator.GetPlanetExaltationPoint(planet_name)


def get_planet_debilitation_point(planet_name: PlanetName) -> ZodiacSign:
    return libray.AstronomicalCalculator.GetPlanetDebilitationPoint(planet_name)


def is_even_sign(planet_sign_name: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsEvenSign(planet_sign_name)


def is_odd_sign(planet_sign_name: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsOddSign(planet_sign_name)


def is_fixed_sign(sun_sign: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsFixedSign(sun_sign)


def is_movable_sign(sun_sign: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsMovableSign(sun_sign)


def is_common_sign(sun_sign: ZodiacName) -> bool:
    return libray.AstronomicalCalculator.IsCommonSign(sun_sign)


def get_planet_permanent_relationship_with_planet(main_planet: PlanetName,
                                                  secondary_planet: PlanetName) -> PlanetToPlanetRelationship:
    return libray.AstronomicalCalculator.GetPlanetPermanentRelationshipWithPlanet(main_planet, secondary_planet)


def convert_julian_time_to_normal_time(julian_time: float):
    return libray.AstronomicalCalculator.ConvertJulianTimeToNormalTime(julian_time)


def get_greenwich_time_from_julian_days(julian_time: float) -> DateTimeOffset:
    return libray.AstronomicalCalculator.GetGreenwichTimeFromJulianDays(julian_time)


def get_greenwich_lmt_in_julian_days(time: Time) -> float:
    return libray.AstronomicalCalculator.GetGreenwichLmtInJulianDays(time)


def get_house_1_and_10_longitudes(time: Time) -> List[float]:
    return libray.AstronomicalCalculator.GetHouse1And10Longitudes(time)


def lmt_to_utc(time: Time) -> DateTimeOffset:
    return libray.AstronomicalCalculator.LmtToUtc(time)


def get_gochara_house(birth_time: Time, current_time: Time, planet: PlanetName) -> int:
    return libray.AstronomicalCalculator.GetGocharaHouse(birth_time, current_time, planet)


def is_gochara_obstructed(planet: PlanetName, gochara_house: int, birth_time: Time, current_time: Time) -> bool:
    return libray.AstronomicalCalculator.IsGocharaObstructed(planet, gochara_house, birth_time, current_time)


def get_planets_in_gochara_house(birth_time: Time, current_time: Time, gochara_house: int) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsInGocharaHouse(birth_time, current_time, gochara_house)


def get_vedhanka(planet: PlanetName, house: int) -> int:
    return libray.AstronomicalCalculator.GetVedhanka(planet, house)


def is_gochara_occurring(birth_time: Time, time: Time, planet: PlanetName, gochara_house: int) -> bool:
    return libray.AstronomicalCalculator.IsGocharaOccurring(birth_time, time, planet, gochara_house)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return libray.AstronomicalCalculator.GetCurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return libray.AstronomicalCalculator.GetCurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return libray.AstronomicalCalculator.GetDasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return libray.AstronomicalCalculator.GetNextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return libray.AstronomicalCalculator.GetTimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return libray.AstronomicalCalculator.GetYearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return libray.AstronomicalCalculator.GetDasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetDasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetBhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetAntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetSukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                   sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                 sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return libray.AstronomicalCalculator.GetConstellationDasaPlanet(constellation_name)


def get_planet_dasa_major_planet_and_minor_relationship(major_planet: PlanetName, minor_planet: PlanetName):
    return libray.AstronomicalCalculator.GetPlanetDasaMajorPlanetAndMinorRelationship(major_planet, minor_planet)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return libray.AstronomicalCalculator.GetCurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return libray.AstronomicalCalculator.GetCurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return libray.AstronomicalCalculator.GetDasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return libray.AstronomicalCalculator.GetNextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return libray.AstronomicalCalculator.GetTimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return libray.AstronomicalCalculator.GetYearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return libray.AstronomicalCalculator.GetDasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetDasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetBhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetAntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetSukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                   sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                 sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return libray.AstronomicalCalculator.GetConstellationDasaPlanet(constellation_name)


def is_mercury_afflicted(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMercuryAfflicted(time)


def is_mercury_malefic(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMercuryMalefic(time)


def is_moon_benefic(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsMoonBenefic(time)


def is_planet_benefic(planet_name: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetBenefic(planet_name, time)


def get_benefic_planet_list(time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetBeneficPlanetList(time)


def is_planet_malefic(planet_name: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetMalefic(planet_name, time)


def get_malefic_planet_list(time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetMaleficPlanetList(time)


def get_planets_in_aspect(planet: PlanetName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsInAspect(planet, time)


def get_planets_aspecting_planet(time: Time, receiving_aspect: PlanetName) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsAspectingPlanet(time, receiving_aspect)


def get_houses_in_aspect(planet: PlanetName, time: Time) -> List[HouseName]:
    return libray.AstronomicalCalculator.GetHousesInAspect(planet, time)


def get_planets_aspecting_house(input_house: HouseName, time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetPlanetsAspectingHouse(input_house, time)


def is_planet_aspected_by_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_house_aspected_by_planet(receiving_aspect: HouseName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsHouseAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_conjunct_with_planet(planet_a: PlanetName, planet_b: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetConjunctWithPlanet(planet_a, planet_b, time)


def get_all_planet_ordered_by_strength(time: Time) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetAllPlanetOrderedByStrength(time)


def get_all_planet_strength(time: Time) -> List[Tuple[float, PlanetName]]:
    return libray.AstronomicalCalculator.GetAllPlanetStrength(time)


def get_all_houses_ordered_by_strength(time: Time) -> List[HouseName]:
    return libray.AstronomicalCalculator.GetAllHousesOrderedByStrength(time)


def get_planet_shadbala_pinda(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetShadbalaPinda(planet_name, time)


def get_planet_strength(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return get_planet_shadbala_pinda(planet_name, time)


def get_planet_drik_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetDrikBala(planet_name, time)


def find_visesha_drishti(dk: float, p: PlanetName) -> float:
    return libray.AstronomicalCalculator.FindViseshaDrishti(dk, p)


def find_drishti_value(dk: float) -> float:
    return libray.AstronomicalCalculator.FindDrishtiValue(dk)


def get_planet_naisargika_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetNaisargikaBala(planet_name, time)


def get_planet_chesta_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetChestaBala(planet_name, time)


def get_madhya(epoch_to_birth_days: float, time1: Time) -> Dict[PlanetName, float]:
    return libray.AstronomicalCalculator.GetMadhya(epoch_to_birth_days, time1)


def get_epoch_interval(time1: Time) -> float:
    return libray.AstronomicalCalculator.GetEpochInterval(time1)


def get_planet_motion_name(planet_name: PlanetName, time: Time) -> PlanetMotion:
    return libray.AstronomicalCalculator.GetPlanetMotionName(planet_name, time)


def get_planet_circulation_time(planet_name: PlanetName) -> float:
    return libray.AstronomicalCalculator.GetPlanetCirculationTime(planet_name)


def get_planet_saptavargaja_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetSaptavargajaBala(planet_name, time)


def get_planet_shadvarga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetShadvargaBala(planet_name, time)


def is_planet_strong_in_shadvarga(planet: PlanetName, time: Time) -> bool:
    return libray.AstronomicalCalculator.IsPlanetStrongInShadvarga(planet, time)


def get_planet_sthana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetSthanaBala(planet_name, time)


def get_planet_drekkana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetDrekkanaBala(planet_name, time)


def get_planet_kendra_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetKendraBala(planet_name, time)


def get_planet_ojayugmarasyamsa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetOjayugmarasyamsaBala(planet_name, time)


def get_planet_kala_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetKalaBala(planet_name, time)


def get_planet_yuddha_bala(inputed_planet: PlanetName, pre_kala_bala_values: Dict[PlanetName, Shashtiamsa],
                           time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetYuddhaBala(inputed_planet, pre_kala_bala_values, time)


def get_planet_ayana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetAyanaBala(planet_name, time)


def get_planet_declination(planet_name: PlanetName, time: Time) -> float:
    return libray.AstronomicalCalculator.GetPlanetDeclination(planet_name, time)


def get_ecliptic_obliquity(time: Time) -> float:
    return libray.AstronomicalCalculator.GetEclipticObliquity(time)


def get_planet_hora_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetHoraBala(planet_name, time)


def get_planet_abda_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetAbdaBala(planet_name, time)


def get_planet_masa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetMasaBala(planet_name, time)


def get_planet_vara_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetVaraBala(planet_name, time)


def get_year_and_month_lord(time: Time) -> object:
    return libray.AstronomicalCalculator.GetYearAndMonthLord(time)


def get_planet_tribhaga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetTribhagaBala(planet_name, time)


def get_planet_ochcha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetOchchaBala(planet_name, time)


def is_day_birth(time: Time) -> bool:
    return libray.AstronomicalCalculator.IsDayBirth(time)


def get_planet_paksha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetPakshaBala(planet_name, time)


def get_planet_nathonnatha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetNathonnathaBala(planet_name, time)


def get_planet_dig_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return libray.AstronomicalCalculator.GetPlanetDigBala(planet_name, time)


def get_bhava_bala(input_house: HouseName, time: Time) -> Shashtiamsa:
    """
           Bhava Bala.-Bhava means house and
         Bala means strength. Bhava Bala is the potency or
         strength of the house or bhava or signification. We
         have already seen that there are 12 bhavas which
         comprehend all human events. Each bhava signifies
         or indicates certain events or functions. For
         instance, the first bhava represents Thanu or body,
         the appearance of the individual, his complexion,
         his disposition, his stature, etc.

         If it attains certain strength, the native will enjoy the indications of
         the bhava fully, otherwise he will not sufficiently
         enjoy them. The strength of a bhava is composed
         of three factors, viz., (1) Bhavadhipathi Bala,
         (2) Bhava Digbala, (3) Bhava Drishti Bala.
         todo change to house strength
    """
    return libray.AstronomicalCalculator.GetBhavaBala(input_house, time)


def calc_bhava_drishti_bala(time: Time) -> HouseSubStrength:
    return libray.AstronomicalCalculator.CalcBhavaDrishtiBala(time)


def calc_bhava_dig_bala(time: Time) -> HouseSubStrength:
    return libray.AstronomicalCalculator.CalcBhavaDigBala(time)


def calc_bhava_adhipathi_bala(time: Time) -> HouseSubStrength:
    return libray.AstronomicalCalculator.CalcBhavaAdhipathiBala(time)


def get_benefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetBeneficPlanetListByShadbala(person_birth_time, threshold)


# def get_benefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return libray.AstronomicalCalculator.GetBeneficPlanetListByShadbala(person_birth_time)


def get_benefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return libray.AstronomicalCalculator.GetBeneficHouseListByShadbala(person_birth_time, threshold)

#
# def get_benefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return libray.AstronomicalCalculator.GetBeneficHouseListByShadbala(person_birth_time)


def get_malefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return libray.AstronomicalCalculator.GetMaleficPlanetListByShadbala(person_birth_time, threshold)


# def get_malefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return libray.AstronomicalCalculator.GetMaleficPlanetListByShadbala(person_birth_time)


def get_malefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return libray.AstronomicalCalculator.GetMaleficHouseListByShadbala(person_birth_time, threshold)


# def get_malefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return libray.AstronomicalCalculator.GetMaleficHouseListByShadbala(person_birth_time)


def get_astral_body_prediction(person: Person) -> str:
    return libray.AstronomicalCalculator.GetAstralBodyPrediction(person)


def get_animal(sign: ConstellationName) -> ConstellationAnimal:
    return libray.AstronomicalCalculator.GetAnimal(sign)
