from typing import List, Tuple, Dict

import VedAstro.Library as library

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


#  var lordOfHouse = Calculator.LordOfHouse((HouseName)houseNumber, _time);


def get_lord_of_house(house_number: HouseName, time: Time):
    return library.Calculate.LordOfHouse(house_number, time)


def time_to_longitude(time: TimeSpan) -> Angle:
    return library.Calculate.TimeToLongitude(time)


def time_to_ephemeris_time(time: Time) -> float:
    return library.Calculate.TimeToEphemerisTime(time)


def get_planet_nirayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return library.Calculate.PlanetNirayanaLongitude(time, planet_name)


def get_lunar_day(time: Time) -> LunarDay:
    return library.Calculate.LunarDay(time)


def get_moon_constellation(time: Time) -> PlanetConstellation:
    return library.Calculate.PlanetConstellation(time, PlanetName.Moon)


def get_planet_constellation(time: Time, planet: PlanetName) -> PlanetConstellation:
    return library.Calculate.PlanetConstellation(time, planet)


def get_tarabala(time: Time, person: Person) -> Tarabala:
    return library.Calculate.Tarabala(time, person)


def get_chandrabala(time: Time, person: Person) -> int:
    return library.Calculate.Chandrabala(time, person)


def get_moon_sign_name(time: Time) -> ZodiacName:
    return library.Calculate.MoonSignName(time)


def get_nithya_yoga(time: Time) -> NithyaYoga:
    return library.Calculate.NithyaYoga(time)


def get_karana(time: Time) -> Karana:
    return library.Calculate.Karana(time)


def get_sun_sign(time: Time) -> ZodiacSign:
    return library.Calculate.SunSign(time)


def get_time_sun_entered_current_sign(time: Time) -> Time:
    return library.Calculate.TimeSunEnteredCurrentSign(time)


def get_time_sun_leaves_current_sign(time: Time) -> Time:
    return library.Calculate.TimeSunLeavesCurrentSign(time)


def get_houses(time: Time) -> List[House]:
    return library.Calculate.Houses(time)


def convert_lmt_to_julian(time: Time) -> float:
    return library.Calculate.ConvertLmtToJulian(time)


def get_planets_in_conjunction(time: Time, inputed_planet_name: PlanetName) -> List[PlanetName]:
    return library.Calculate.PlanetsInConjuction(time, inputed_planet_name)


def get_distance_between_planets(planet1: PlanetName, planet2: PlanetName, time: Time) -> Angle:
    return library.Calculate.DistanceBetweenPlanets(planet1, planet2, time)


def get_distance_between_planets_angle(planet1: Angle, planet2: Angle) -> Angle:
    return library.Calculate.DistanceBetweenPlanets(planet1, planet2)


def get_planets_in_house(house_number: int, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetsInHouse(house_number, time)


def get_all_planet_longitude(time: Time) -> List[PlanetLongitude]:
    return library.Calculate.AllPlanetLongitude(time)


def get_all_planet_fixed_longitude(time: Time) -> List[PlanetLongitude]:
    return library.Calculate.AllPlanetFixedLongitude(time)


def get_house_planet_is_in(time: Time, planet_name: PlanetName) -> int:
    return library.Calculate.HousePlanetIsIn(time, planet_name)


def get_lord_of_house_list(house_list: List[HouseName], time: Time) -> List[PlanetName]:
    return library.Calculate.LordOfHouseList(house_list, time)


def is_house_sign_name(house: int, sign: ZodiacName, time: Time) -> bool:
    return library.Calculate.HouseSignName(house, time) == sign


def get_house_sign_name(house_number: int, time: Time) -> ZodiacName:
    return library.Calculate.HouseSignName(house_number, time)


def get_navamsa_sign_name_from_longitude(longitude: Angle) -> ZodiacName:
    return library.Calculate.NavamsaSignNameFromLongitude(longitude)


def get_sign_counted_from_input_sign(input_sign: ZodiacName, count_to_next_sign: int) -> ZodiacName:
    return library.Calculate.SignCountedFromInputSign(input_sign, count_to_next_sign)


def get_house_counted_from_input_house(input_house_number: int, count_to_next_house: int) -> int:
    return library.Calculate.HouseCountedFromInputHouse(input_house_number, count_to_next_house)


def get_planet_rasi_sign(planet_name: PlanetName, time: Time) -> ZodiacSign:
    return library.Calculate.PlanetRasiSign(planet_name, time)


def is_planet_in_sign(planet_name: PlanetName, sign_input: ZodiacName, time: Time) -> bool:
    return library.Calculate.IsPlanetInSign(planet_name, sign_input, time)


def get_planet_navamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetNavamsaSign(planet_name, time)


def get_house_navamsa_sign(house: HouseName, time: Time) -> ZodiacName:
    return library.Calculate.HouseNavamsaSign(house, time)


def get_planet_thrimsamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetThrimsamsaSign(planet_name, time)


def get_planet_dwadasamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetDwadasamsaSign(planet_name, time)


def get_planet_saptamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetSaptamsaSign(planet_name, time)


def get_planet_drekkana_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetDrekkanaSign(planet_name, time)


def is_planet_in_moolatrikona(planet_name: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetInMoolatrikona(planet_name, time)


def get_planet_relationship_with_sign(planet_name: PlanetName, zodiac_sign_name: ZodiacName,
                                      time: Time) -> PlanetToSignRelationship:
    return library.Calculate.PlanetRelationshipWithSign(planet_name, zodiac_sign_name, time)


def get_planet_combined_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                 time: Time) -> PlanetToPlanetRelationship:
    return library.Calculate.PlanetCombinedRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_relationship_with_house(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
    return library.Calculate.PlanetRelationshipWithHouse(house, planet, time)


def get_planet_temporary_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                  time: Time) -> PlanetToPlanetRelationship:
    return library.Calculate.PlanetTemporaryRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_temporary_enemy_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetTemporaryEnemyList(planet_name, time)


def get_planet_in_sign(sign_name: ZodiacName, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetInSign(sign_name, time)


def get_planet_temporary_friend_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetTemporaryFriendList(planet_name, time)


def get_greenwich_apparent_in_julian_days(time: Time) -> float:
    return library.Calculate.GreenwichApparentInJulianDays(time)


def get_local_apparent_time(time: Time):
    return library.Calculate.LocalApparentTime(time)


def get_local_mean_time(time: Time) -> DateTimeOffset:
    return time.LmtDateTimeOffset()


def get_house(house_number: HouseName, time: Time) -> House:
    return library.Calculate.House(house_number, time)


def get_panchaka(time: Time) -> PanchakaName:
    return library.Calculate.Panchaka(time)


def get_lord_of_weekday(time: Time) -> PlanetName:
    return library.Calculate.LordOfWeekday(time)


def get_lord_of_weekday(weekday: DayOfWeek) -> PlanetName:
    return library.Calculate.LordOfWeekday(weekday)


def lmt_to_std(lmt_date_time: DateTimeOffset, std_offset: TimeSpan) -> DateTimeOffset:
    return library.Calculate.LmtToStd(lmt_date_time, std_offset)


def get_hora_at_birth(time: Time) -> int:
    return library.Calculate.HoraAtBirth(time)


def get_planet_hora_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return library.Calculate.PlanetHoraSign(planet_name, time)


def get_sunrise_time(time: Time) -> Time:
    return library.Calculate.SunriseTime(time)


def get_sunset_time(time: Time) -> Time:
    return library.Calculate.SunsetTime(time)


def get_noon_time(time: Time):
    return library.Calculate.NoonTime(time)


def is_planet_in_good_aspect_to_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName,
                                       time: Time) -> bool:
    return library.Calculate.IsPlanetInGoodAspectToPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_in_good_aspect_to_house(receiving_aspect: PlanetName, transmitting_aspect: HouseName, time: Time) -> bool:
    return library.Calculate.IsPlanetInGoodAspectToHouse(receiving_aspect, transmitting_aspect, time)


def get_planet_sthana_bala_neutral_point(planet: PlanetName) -> float:
    return library.Calculate.PlanetSthanaBalaNeutralPoint(planet)


def get_planet_shadvarga_bala_neutral_point(planet: PlanetName) -> float:
    return library.Calculate.PlanetShadvargaBalaNeutralPoint(planet)


def is_planet_in_kendra(planet: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetInKendra(planet, time)


def is_house_lord_in_house(lord_house: HouseName, occupied_house: HouseName, time: Time) -> bool:
    return library.Calculate.IsHouseLordInHouse(lord_house, occupied_house, time)


def is_planet_conjunct_with_malefic_planets(planet_name: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetConjunctWithMaleficPlanets(planet_name, time)


def is_malefic_planet_in_house(house_number: int, time: Time) -> bool:
    return library.Calculate.IsMaleficPlanetInHouse(house_number, time)


def is_benefic_planet_in_house(house_number: int, time: Time) -> bool:
    return library.Calculate.IsBeneficPlanetInHouse(house_number, time)


def is_malefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return library.Calculate.IsMaleficPlanetInSign(sign, time)


def get_malefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return library.Calculate.MaleficPlanetListInSign(sign, time)


def is_benefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return library.Calculate.IsBeneficPlanetInSign(sign, time)


def get_benefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return library.Calculate.BeneficPlanetListInSign(sign, time)


def is_malefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return library.Calculate.IsMaleficPlanetAspectHouse(house, time)


def is_benefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return library.Calculate.IsBeneficPlanetAspectHouse(house, time)


def is_planet_aspected_by_malefic_planets(lord: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetAspectedByMaleficPlanets(lord, time)


def get_arudha_lagna_sign(time: Time) -> ZodiacName:
    return library.Calculate.ArudhaLagnaSign(time)


def count_from_sign_to_sign(start_sign: ZodiacName, end_sign: ZodiacName) -> int:
    return library.Calculate.CountFromSignToSign(start_sign, end_sign)


def count_from_constellation_to_constellation(start: PlanetConstellation, end: PlanetConstellation) -> int:
    return library.Calculate.CountFromConstellationToConstellation(start, end)


def is_planet_in_house(time: Time, planet: PlanetName, house_number: int) -> bool:
    return library.Calculate.IsPlanetInHouse(time, planet, house_number)


def is_planet_debilitated(planet: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetDebilitated(planet, time)


def is_planet_exalted(planet: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetExalted(planet, time)


def get_lunar_month(time: Time) -> LunarMonth:
    return library.Calculate.LunarMonth(time)


def is_full_moon(time: Time) -> bool:
    return library.Calculate.IsFullMoon(time)


def is_aquatic_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Cancer, ZodiacName.Scorpio, ZodiacName.Pisces]


def is_fire_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Aries, ZodiacName.Leo, ZodiacName.Sagittarius]


def is_earth_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Taurus, ZodiacName.Virgo, ZodiacName.Capricornus]


def is_air_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Gemini, ZodiacName.Libra, ZodiacName.Aquarius]


def get_planet_antaram_nature(person: Person, planet: PlanetName) -> EventNature:
    return library.Calculate.PlanetAntaramNature(person, planet)


def is_planet_benefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return library.Calculate.IsPlanetBeneficToLagna(planet_name, lagna)


def is_planet_malefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return library.Calculate.IsPlanetMaleficToLagna(planet_name, lagna)


def is_planet_yogakaraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return library.Calculate.IsPlanetYogakarakaToLagna(planet_name, lagna)


def is_planet_maraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return library.Calculate.IsPlanetMarakaToLagna(planet_name, lagna)


def is_planet_in_own_house(time: Time, planet_name: PlanetName) -> bool:
    return library.Calculate.IsPlanetInOwnHouse(time, planet_name)


def swe_calc_wrapper(time: Time, planet_name: PlanetName):
    return library.Calculate.swe_calc_wrapper(time, planet_name)


def is_planet_same_house_with_house_lord(birth_time: Time, house_number: int, planet: PlanetName) -> bool:
    return library.Calculate.IsPlanetSameHouseWithHouseLord(birth_time, house_number, planet)


def get_time_house_calcs():
    return library.Calculate.TimeHouseCalcs()


def is_moon_weak(time: Time) -> bool:
    return library.Calculate.IsMoonWeak(time)


def is_moon_strong(time: Time) -> bool:
    return library.Calculate.IsMoonStrong(time)


def get_ayanamsa(time: Time) -> Angle:
    return library.Calculate.Ayanamsa(time)


def get_planet_sayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return library.Calculate.PlanetSayanaLongitude(time, planet_name)


def get_planet_sayana_latitude(time: Time, planet_name: PlanetName) -> Angle:
    return library.Calculate.PlanetSayanaLatitude(time, planet_name)


def get_planet_speed(time: Time, planet_name: PlanetName) -> float:
    return library.Calculate.PlanetSpeed(time, planet_name)


def get_constellation_at_longitude(planet_longitude: Angle) -> PlanetConstellation:
    return library.Calculate.ConstellationAtLongitude(planet_longitude)


def get_zodiac_sign_at_longitude(longitude: Angle) -> ZodiacSign:
    return library.Calculate.ZodiacSignAtLongitude(longitude)


def get_longitude_at_zodiac_sign(zodiac_sign: ZodiacSign) -> Angle:
    return library.Calculate.LongitudeAtZodiacSign(zodiac_sign)


def get_day_of_week(time: Time) -> DayOfWeek:
    return library.Calculate.DayOfWeek(time)


def get_lord_of_hora(hora: int, day: DayOfWeek) -> PlanetName:
    return library.Calculate.LordOfHora(hora, day)


def get_house_junction_point(previous_house: Angle, next_house: Angle) -> Angle:
    return library.Calculate.HouseJunctionPoint(previous_house, next_house)


def get_lord_of_zodiac_sign(sign_name: ZodiacName) -> PlanetName:
    return library.Calculate.LordOfZodiacSign(sign_name)


def get_next_zodiac_sign(input_sign: ZodiacName) -> ZodiacName:
    return library.Calculate.NextZodiacSign(input_sign)


def get_next_house_number(input_house_number: int) -> int:
    return library.Calculate.NextHouseNumber(input_house_number)


def get_planet_exaltation_point(planet_name: PlanetName) -> ZodiacSign:
    return library.Calculate.PlanetExaltationPoint(planet_name)


def get_planet_debilitation_point(planet_name: PlanetName) -> ZodiacSign:
    return library.Calculate.PlanetDebilitationPoint(planet_name)


def is_even_sign(planet_sign_name: ZodiacName) -> bool:
    return library.Calculate.IsEvenSign(planet_sign_name)


def is_odd_sign(planet_sign_name: ZodiacName) -> bool:
    return library.Calculate.IsOddSign(planet_sign_name)


def is_fixed_sign(sun_sign: ZodiacName) -> bool:
    return library.Calculate.IsFixedSign(sun_sign)


def is_movable_sign(sun_sign: ZodiacName) -> bool:
    return library.Calculate.IsMovableSign(sun_sign)


def is_common_sign(sun_sign: ZodiacName) -> bool:
    return library.Calculate.IsCommonSign(sun_sign)


def get_planet_permanent_relationship_with_planet(main_planet: PlanetName,
                                                  secondary_planet: PlanetName) -> PlanetToPlanetRelationship:
    return library.Calculate.PlanetPermanentRelationshipWithPlanet(main_planet, secondary_planet)


def convert_julian_time_to_normal_time(julian_time: float):
    return library.Calculate.ConvertJulianTimeToNormalTime(julian_time)


def get_greenwich_time_from_julian_days(julian_time: float) -> DateTimeOffset:
    return library.Calculate.GreenwichTimeFromJulianDays(julian_time)


def get_greenwich_lmt_in_julian_days(time: Time) -> float:
    return library.Calculate.GreenwichLmtInJulianDays(time)


def get_house_1_and_10_longitudes(time: Time) -> List[float]:
    return library.Calculate.House1And10Longitudes(time)


def lmt_to_utc(time: Time) -> DateTimeOffset:
    return library.Calculate.LmtToUtc(time)


def get_gochara_house(birth_time: Time, current_time: Time, planet: PlanetName) -> int:
    return library.Calculate.GocharaHouse(birth_time, current_time, planet)


def is_gochara_obstructed(planet: PlanetName, gochara_house: int, birth_time: Time, current_time: Time) -> bool:
    return library.Calculate.IsGocharaObstructed(planet, gochara_house, birth_time, current_time)


def get_planets_in_gochara_house(birth_time: Time, current_time: Time, gochara_house: int) -> List[PlanetName]:
    return library.Calculate.PlanetsInGocharaHouse(birth_time, current_time, gochara_house)


def get_vedhanka(planet: PlanetName, house: int) -> int:
    return library.Calculate.Vedhanka(planet, house)


def is_gochara_occurring(birth_time: Time, time: Time, planet: PlanetName, gochara_house: int) -> bool:
    return library.Calculate.IsGocharaOccurring(birth_time, time, planet, gochara_house)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return library.Calculate.CurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return library.Calculate.CurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return library.Calculate.DasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return library.Calculate.NextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return library.Calculate.TimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return library.Calculate.YearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return library.Calculate.DasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return library.Calculate.DasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return library.Calculate.BhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return library.Calculate.AntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return library.Calculate.SukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                   sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return library.Calculate.PranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                 sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return library.Calculate.ConstellationDasaPlanet(constellation_name)


def get_planet_dasa_major_planet_and_minor_relationship(major_planet: PlanetName, minor_planet: PlanetName):
    return library.Calculate.PlanetDasaMajorPlanetAndMinorRelationship(major_planet, minor_planet)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return library.Calculate.CurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return library.Calculate.CurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return library.Calculate.DasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return library.Calculate.NextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return library.Calculate.TimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return library.Calculate.YearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return library.Calculate.DasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return library.Calculate.DasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return library.Calculate.BhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return library.Calculate.AntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return library.Calculate.SukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                   sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return library.Calculate.PranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                                 sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return library.Calculate.ConstellationDasaPlanet(constellation_name)


def is_mercury_afflicted(time: Time) -> bool:
    return library.Calculate.IsMercuryAfflicted(time)


def is_mercury_malefic(time: Time) -> bool:
    return library.Calculate.IsMercuryMalefic(time)


def is_moon_benefic(time: Time) -> bool:
    return library.Calculate.IsMoonBenefic(time)


def is_planet_benefic(planet_name: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetBenefic(planet_name, time)


def get_benefic_planet_list(time: Time) -> List[PlanetName]:
    return library.Calculate.BeneficPlanetList(time)


def is_planet_malefic(planet_name: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetMalefic(planet_name, time)


def get_malefic_planet_list(time: Time) -> List[PlanetName]:
    return library.Calculate.MaleficPlanetList(time)


def get_planets_in_aspect(planet: PlanetName, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetsInAspect(planet, time)


def get_planets_aspecting_planet(time: Time, receiving_aspect: PlanetName) -> List[PlanetName]:
    return library.Calculate.PlanetsAspectingPlanet(time, receiving_aspect)


def get_houses_in_aspect(planet: PlanetName, time: Time) -> List[HouseName]:
    return library.Calculate.HousesInAspect(planet, time)


def get_planets_aspecting_house(input_house: HouseName, time: Time) -> List[PlanetName]:
    return library.Calculate.PlanetsAspectingHouse(input_house, time)


def is_planet_aspected_by_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_house_aspected_by_planet(receiving_aspect: HouseName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return library.Calculate.IsHouseAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_conjunct_with_planet(planet_a: PlanetName, planet_b: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetConjunctWithPlanet(planet_a, planet_b, time)


def get_all_planet_ordered_by_strength(time: Time) -> List[PlanetName]:
    return library.Calculate.AllPlanetOrderedByStrength(time)


def get_all_planet_strength(time: Time) -> List[Tuple[float, PlanetName]]:
    return library.Calculate.AllPlanetStrength(time)


def get_all_houses_ordered_by_strength(time: Time) -> List[HouseName]:
    return library.Calculate.AllHousesOrderedByStrength(time)


def get_planet_shadbala_pinda(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetShadbalaPinda(planet_name, time)


def get_planet_strength(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return get_planet_shadbala_pinda(planet_name, time)


def get_planet_drik_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetDrikBala(planet_name, time)


def find_visesha_drishti(dk: float, p: PlanetName) -> float:
    return library.Calculate.FindViseshaDrishti(dk, p)


def find_drishti_value(dk: float) -> float:
    return library.Calculate.FindDrishtiValue(dk)


def get_planet_naisargika_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetNaisargikaBala(planet_name, time)


def get_planet_chesta_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetChestaBala(planet_name, time)


def get_madhya(epoch_to_birth_days: float, time1: Time) -> Dict[PlanetName, float]:
    return library.Calculate.Madhya(epoch_to_birth_days, time1)


def get_epoch_interval(time1: Time) -> float:
    return library.Calculate.EpochInterval(time1)


def get_planet_motion_name(planet_name: PlanetName, time: Time) -> PlanetMotion:
    return library.Calculate.PlanetMotionName(planet_name, time)


def get_planet_circulation_time(planet_name: PlanetName) -> float:
    return library.Calculate.PlanetCirculationTime(planet_name)


def get_planet_saptavargaja_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetSaptavargajaBala(planet_name, time)


def get_planet_shadvarga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetShadvargaBala(planet_name, time)


def is_planet_strong_in_shadvarga(planet: PlanetName, time: Time) -> bool:
    return library.Calculate.IsPlanetStrongInShadvarga(planet, time)


def get_planet_sthana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetSthanaBala(planet_name, time)


def get_planet_drekkana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetDrekkanaBala(planet_name, time)


def get_planet_kendra_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetKendraBala(planet_name, time)


def get_planet_ojayugmarasyamsa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetOjayugmarasyamsaBala(planet_name, time)


def get_planet_kala_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetKalaBala(planet_name, time)


def get_planet_yuddha_bala(inputed_planet: PlanetName, pre_kala_bala_values: Dict[PlanetName, Shashtiamsa],
                           time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetYuddhaBala(inputed_planet, pre_kala_bala_values, time)


def get_planet_ayana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetAyanaBala(planet_name, time)


def get_planet_declination(planet_name: PlanetName, time: Time) -> float:
    return library.Calculate.PlanetDeclination(planet_name, time)


def get_ecliptic_obliquity(time: Time) -> float:
    return library.Calculate.EclipticObliquity(time)


def get_planet_hora_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetHoraBala(planet_name, time)


def get_planet_abda_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetAbdaBala(planet_name, time)


def get_planet_masa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetMasaBala(planet_name, time)


def get_planet_vara_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetVaraBala(planet_name, time)


def get_year_and_month_lord(time: Time) -> object:
    return library.Calculate.YearAndMonthLord(time)


def get_planet_tribhaga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetTribhagaBala(planet_name, time)


def get_planet_ochcha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetOchchaBala(planet_name, time)


def is_day_birth(time: Time) -> bool:
    return library.Calculate.IsDayBirth(time)


def get_planet_paksha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetPakshaBala(planet_name, time)


def get_planet_nathonnatha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetNathonnathaBala(planet_name, time)


def get_planet_dig_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return library.Calculate.PlanetDigBala(planet_name, time)


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
    return library.Calculate.BhavaBala(input_house, time)


def calc_bhava_drishti_bala(time: Time) -> HouseSubStrength:
    return library.Calculate.CalcBhavaDrishtiBala(time)


def calc_bhava_dig_bala(time: Time) -> HouseSubStrength:
    return library.Calculate.CalcBhavaDigBala(time)


def calc_bhava_adhipathi_bala(time: Time) -> HouseSubStrength:
    return library.Calculate.CalcBhavaAdhipathiBala(time)


def get_benefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return library.Calculate.BeneficPlanetListByShadbala(person_birth_time, threshold)


# def get_benefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return library.Calculate.BeneficPlanetListByShadbala(person_birth_time)


def get_benefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return library.Calculate.BeneficHouseListByShadbala(person_birth_time, threshold)

#
# def get_benefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return library.Calculate.BeneficHouseListByShadbala(person_birth_time)


def get_malefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return library.Calculate.MaleficPlanetListByShadbala(person_birth_time, threshold)


# def get_malefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return library.Calculate.MaleficPlanetListByShadbala(person_birth_time)


def get_malefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return library.Calculate.MaleficHouseListByShadbala(person_birth_time, threshold)


# def get_malefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return library.Calculate.MaleficHouseListByShadbala(person_birth_time)


def get_astral_body_prediction(person: Person) -> str:
    return library.Calculate.AstralBodyPrediction(person)


def get_animal(sign: ConstellationName) -> ConstellationAnimal:
    return library.Calculate.Animal(sign)
