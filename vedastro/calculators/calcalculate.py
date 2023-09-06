from typing import List, Tuple, Dict

import VedAstro.Library as VedAstro

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
    return VedAstro.Calculate.LordOfHouse(house_number, time)


def time_to_longitude(time: TimeSpan) -> Angle:
    return VedAstro.Calculate.TimeToLongitude(time)


def time_to_ephemeris_time(time: Time) -> float:
    return VedAstro.Calculate.TimeToEphemerisTime(time)


def get_planet_nirayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return VedAstro.Calculate.PlanetNirayanaLongitude(time, planet_name)


def get_lunar_day(time: Time) -> LunarDay:
    return VedAstro.Calculate.LunarDay(time)


def get_moon_constellation(time: Time) -> PlanetConstellation:
    return VedAstro.Calculate.PlanetConstellation(time, PlanetName.Moon)


def get_planet_constellation(time: Time, planet: PlanetName) -> PlanetConstellation:
    return VedAstro.Calculate.PlanetConstellation(time, planet)


def get_tarabala(time: Time, person: Person) -> Tarabala:
    return VedAstro.Calculate.Tarabala(time, person)


def get_chandrabala(time: Time, person: Person) -> int:
    return VedAstro.Calculate.Chandrabala(time, person)


def get_moon_sign_name(time: Time) -> ZodiacName:
    return VedAstro.Calculate.MoonSignName(time)


def get_nithya_yoga(time: Time) -> NithyaYoga:
    return VedAstro.Calculate.NithyaYoga(time)


def get_karana(time: Time) -> Karana:
    return VedAstro.Calculate.Karana(time)


def get_sun_sign(time: Time) -> ZodiacSign:
    return VedAstro.Calculate.SunSign(time)


def get_time_sun_entered_current_sign(time: Time) -> Time:
    return VedAstro.Calculate.TimeSunEnteredCurrentSign(time)


def get_time_sun_leaves_current_sign(time: Time) -> Time:
    return VedAstro.Calculate.TimeSunLeavesCurrentSign(time)


def get_houses(time: Time) -> List[House]:
    return VedAstro.Calculate.Houses(time)


def convert_lmt_to_julian(time: Time) -> float:
    return VedAstro.Calculate.ConvertLmtToJulian(time)


def get_planets_in_conjunction(time: Time, inputed_planet_name: PlanetName) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsInConjuction(time, inputed_planet_name)


def get_distance_between_planets(planet1: PlanetName, planet2: PlanetName, time: Time) -> Angle:
    return VedAstro.Calculate.DistanceBetweenPlanets(planet1, planet2, time)


def get_distance_between_planets_angle(planet1: Angle, planet2: Angle) -> Angle:
    return VedAstro.Calculate.DistanceBetweenPlanets(planet1, planet2)


def get_planets_in_house(house_number: int, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsInHouse(house_number, time)


def get_all_planet_longitude(time: Time) -> List[PlanetLongitude]:
    return VedAstro.Calculate.AllPlanetLongitude(time)


def get_all_planet_fixed_longitude(time: Time) -> List[PlanetLongitude]:
    return VedAstro.Calculate.AllPlanetFixedLongitude(time)


def get_house_planet_is_in(time: Time, planet_name: PlanetName) -> int:
    return VedAstro.Calculate.HousePlanetIsIn(time, planet_name)


def get_lord_of_house_list(house_list: List[HouseName], time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.LordOfHouseList(house_list, time)


def is_house_sign_name(house: int, sign: ZodiacName, time: Time) -> bool:
    return VedAstro.Calculate.HouseSignName(house, time) == sign


def get_house_sign_name(house_number: int, time: Time) -> ZodiacName:
    return VedAstro.Calculate.HouseSignName(house_number, time)


def get_navamsa_sign_name_from_longitude(longitude: Angle) -> ZodiacName:
    return VedAstro.Calculate.NavamsaSignNameFromLongitude(longitude)


def get_sign_counted_from_input_sign(input_sign: ZodiacName, count_to_next_sign: int) -> ZodiacName:
    return VedAstro.Calculate.SignCountedFromInputSign(input_sign, count_to_next_sign)


def get_house_counted_from_input_house(input_house_number: int, count_to_next_house: int) -> int:
    return VedAstro.Calculate.HouseCountedFromInputHouse(input_house_number, count_to_next_house)


def get_planet_rasi_sign(planet_name: PlanetName, time: Time) -> ZodiacSign:
    return VedAstro.Calculate.PlanetRasiSign(planet_name, time)


def is_planet_in_sign(planet_name: PlanetName, sign_input: ZodiacName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetInSign(planet_name, sign_input, time)


def get_planet_navamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetNavamsaSign(planet_name, time)


def get_house_navamsa_sign(house: HouseName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.HouseNavamsaSign(house, time)


def get_planet_thrimsamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetThrimsamsaSign(planet_name, time)


def get_planet_dwadasamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetDwadasamsaSign(planet_name, time)


def get_planet_saptamsa_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetSaptamsaSign(planet_name, time)


def get_planet_drekkana_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetDrekkanaSign(planet_name, time)


def is_planet_in_moolatrikona(planet_name: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetInMoolatrikona(planet_name, time)


def get_planet_relationship_with_sign(planet_name: PlanetName, zodiac_sign_name: ZodiacName,
                                      time: Time) -> PlanetToSignRelationship:
    return VedAstro.Calculate.PlanetRelationshipWithSign(planet_name, zodiac_sign_name, time)


def get_planet_combined_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                 time: Time) -> PlanetToPlanetRelationship:
    return VedAstro.Calculate.PlanetCombinedRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_relationship_with_house(house: HouseName, planet: PlanetName, time: Time) -> PlanetToSignRelationship:
    return VedAstro.Calculate.PlanetRelationshipWithHouse(house, planet, time)


def get_planet_temporary_relationship_with_planet(main_planet: PlanetName, secondary_planet: PlanetName,
                                                  time: Time) -> PlanetToPlanetRelationship:
    return VedAstro.Calculate.PlanetTemporaryRelationshipWithPlanet(main_planet, secondary_planet, time)


def get_planet_temporary_enemy_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetTemporaryEnemyList(planet_name, time)


def get_planet_in_sign(sign_name: ZodiacName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetInSign(sign_name, time)


def get_planet_temporary_friend_list(planet_name: PlanetName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetTemporaryFriendList(planet_name, time)


def get_greenwich_apparent_in_julian_days(time: Time) -> float:
    return VedAstro.Calculate.GreenwichApparentInJulianDays(time)


def get_local_apparent_time(time: Time):
    return VedAstro.Calculate.LocalApparentTime(time)


def get_local_mean_time(time: Time) -> DateTimeOffset:
    return time.LmtDateTimeOffset()


def get_house(house_number: HouseName, time: Time) -> House:
    return VedAstro.Calculate.House(house_number, time)


def get_panchaka(time: Time) -> PanchakaName:
    return VedAstro.Calculate.Panchaka(time)


def get_lord_of_weekday(time: Time) -> PlanetName:
    return VedAstro.Calculate.LordOfWeekday(time)


def get_lord_of_weekday(weekday: DayOfWeek) -> PlanetName:
    return VedAstro.Calculate.LordOfWeekday(weekday)


def lmt_to_std(lmt_date_time: DateTimeOffset, std_offset: TimeSpan) -> DateTimeOffset:
    return VedAstro.Calculate.LmtToStd(lmt_date_time, std_offset)


def get_hora_at_birth(time: Time) -> int:
    return VedAstro.Calculate.HoraAtBirth(time)


def get_planet_hora_sign(planet_name: PlanetName, time: Time) -> ZodiacName:
    return VedAstro.Calculate.PlanetHoraSign(planet_name, time)


def get_sunrise_time(time: Time) -> Time:
    return VedAstro.Calculate.SunriseTime(time)


def get_sunset_time(time: Time) -> Time:
    return VedAstro.Calculate.SunsetTime(time)


def get_noon_time(time: Time):
    return VedAstro.Calculate.NoonTime(time)


def is_planet_in_good_aspect_to_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName,
                                       time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetInGoodAspectToPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_in_good_aspect_to_house(receiving_aspect: PlanetName, transmitting_aspect: HouseName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetInGoodAspectToHouse(receiving_aspect, transmitting_aspect, time)


def get_planet_sthana_bala_neutral_point(planet: PlanetName) -> float:
    return VedAstro.Calculate.PlanetSthanaBalaNeutralPoint(planet)


def get_planet_shadvarga_bala_neutral_point(planet: PlanetName) -> float:
    return VedAstro.Calculate.PlanetShadvargaBalaNeutralPoint(planet)


def is_planet_in_kendra(planet: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetInKendra(planet, time)


def is_house_lord_in_house(lord_house: HouseName, occupied_house: HouseName, time: Time) -> bool:
    return VedAstro.Calculate.IsHouseLordInHouse(lord_house, occupied_house, time)


def is_planet_conjunct_with_malefic_planets(planet_name: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetConjunctWithMaleficPlanets(planet_name, time)


def is_malefic_planet_in_house(house_number: int, time: Time) -> bool:
    return VedAstro.Calculate.IsMaleficPlanetInHouse(house_number, time)


def is_benefic_planet_in_house(house_number: int, time: Time) -> bool:
    return VedAstro.Calculate.IsBeneficPlanetInHouse(house_number, time)


def is_malefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return VedAstro.Calculate.IsMaleficPlanetInSign(sign, time)


def get_malefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.MaleficPlanetListInSign(sign, time)


def is_benefic_planet_in_sign(sign: ZodiacName, time: Time) -> bool:
    return VedAstro.Calculate.IsBeneficPlanetInSign(sign, time)


def get_benefic_planet_list_in_sign(sign: ZodiacName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.BeneficPlanetListInSign(sign, time)


def is_malefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return VedAstro.Calculate.IsMaleficPlanetAspectHouse(house, time)


def is_benefic_planet_aspect_house(house: HouseName, time: Time) -> bool:
    return VedAstro.Calculate.IsBeneficPlanetAspectHouse(house, time)


def is_planet_aspected_by_malefic_planets(lord: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetAspectedByMaleficPlanets(lord, time)


def get_arudha_lagna_sign(time: Time) -> ZodiacName:
    return VedAstro.Calculate.ArudhaLagnaSign(time)


def count_from_sign_to_sign(start_sign: ZodiacName, end_sign: ZodiacName) -> int:
    return VedAstro.Calculate.CountFromSignToSign(start_sign, end_sign)


def count_from_constellation_to_constellation(start: PlanetConstellation, end: PlanetConstellation) -> int:
    return VedAstro.Calculate.CountFromConstellationToConstellation(start, end)


def is_planet_in_house(time: Time, planet: PlanetName, house_number: int) -> bool:
    return VedAstro.Calculate.IsPlanetInHouse(time, planet, house_number)


def is_planet_debilitated(planet: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetDebilitated(planet, time)


def is_planet_exalted(planet: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetExalted(planet, time)


def get_lunar_month(time: Time) -> LunarMonth:
    return VedAstro.Calculate.LunarMonth(time)


def is_full_moon(time: Time) -> bool:
    return VedAstro.Calculate.IsFullMoon(time)


def is_aquatic_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Cancer, ZodiacName.Scorpio, ZodiacName.Pisces]


def is_fire_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Aries, ZodiacName.Leo, ZodiacName.Sagittarius]


def is_earth_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Taurus, ZodiacName.Virgo, ZodiacName.Capricornus]


def is_air_sign(moon_sign: ZodiacName) -> bool:
    return moon_sign in [ZodiacName.Gemini, ZodiacName.Libra, ZodiacName.Aquarius]


def get_planet_antaram_nature(person: Person, planet: PlanetName) -> EventNature:
    return VedAstro.Calculate.PlanetAntaramNature(person, planet)


def is_planet_benefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return VedAstro.Calculate.IsPlanetBeneficToLagna(planet_name, lagna)


def is_planet_malefic_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return VedAstro.Calculate.IsPlanetMaleficToLagna(planet_name, lagna)


def is_planet_yogakaraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return VedAstro.Calculate.IsPlanetYogakarakaToLagna(planet_name, lagna)


def is_planet_maraka_to_lagna(planet_name: PlanetName, lagna: ZodiacName) -> bool:
    return VedAstro.Calculate.IsPlanetMarakaToLagna(planet_name, lagna)


def is_planet_in_own_house(time: Time, planet_name: PlanetName) -> bool:
    return VedAstro.Calculate.IsPlanetInOwnHouse(time, planet_name)


def swe_calc_wrapper(time: Time, planet_name: PlanetName):
    return VedAstro.Calculate.swe_calc_wrapper(time, planet_name)


def is_planet_same_house_with_house_lord(birth_time: Time, house_number: int, planet: PlanetName) -> bool:
    return VedAstro.Calculate.IsPlanetSameHouseWithHouseLord(birth_time, house_number, planet)


def get_time_house_calcs():
    return VedAstro.Calculate.TimeHouseCalcs()


def is_moon_weak(time: Time) -> bool:
    return VedAstro.Calculate.IsMoonWeak(time)


def is_moon_strong(time: Time) -> bool:
    return VedAstro.Calculate.IsMoonStrong(time)


def get_ayanamsa(time: Time) -> Angle:
    return VedAstro.Calculate.Ayanamsa(time)


def get_planet_sayana_longitude(time: Time, planet_name: PlanetName) -> Angle:
    return VedAstro.Calculate.PlanetSayanaLongitude(time, planet_name)


def get_planet_sayana_latitude(time: Time, planet_name: PlanetName) -> Angle:
    return VedAstro.Calculate.PlanetSayanaLatitude(time, planet_name)


def get_planet_speed(time: Time, planet_name: PlanetName) -> float:
    return VedAstro.Calculate.PlanetSpeed(time, planet_name)


def get_constellation_at_longitude(planet_longitude: Angle) -> PlanetConstellation:
    return VedAstro.Calculate.ConstellationAtLongitude(planet_longitude)


def get_zodiac_sign_at_longitude(longitude: Angle) -> ZodiacSign:
    return VedAstro.Calculate.ZodiacSignAtLongitude(longitude)


def get_longitude_at_zodiac_sign(zodiac_sign: ZodiacSign) -> Angle:
    return VedAstro.Calculate.LongitudeAtZodiacSign(zodiac_sign)


def get_day_of_week(time: Time) -> DayOfWeek:
    return VedAstro.Calculate.DayOfWeek(time)


def get_lord_of_hora(hora: int, day: DayOfWeek) -> PlanetName:
    return VedAstro.Calculate.LordOfHora(hora, day)


def get_house_junction_point(previous_house: Angle, next_house: Angle) -> Angle:
    return VedAstro.Calculate.HouseJunctionPoint(previous_house, next_house)


def get_lord_of_zodiac_sign(sign_name: ZodiacName) -> PlanetName:
    return VedAstro.Calculate.LordOfZodiacSign(sign_name)


def get_next_zodiac_sign(input_sign: ZodiacName) -> ZodiacName:
    return VedAstro.Calculate.NextZodiacSign(input_sign)


def get_next_house_number(input_house_number: int) -> int:
    return VedAstro.Calculate.NextHouseNumber(input_house_number)


def get_planet_exaltation_point(planet_name: PlanetName) -> ZodiacSign:
    return VedAstro.Calculate.PlanetExaltationPoint(planet_name)


def get_planet_debilitation_point(planet_name: PlanetName) -> ZodiacSign:
    return VedAstro.Calculate.PlanetDebilitationPoint(planet_name)


def is_even_sign(planet_sign_name: ZodiacName) -> bool:
    return VedAstro.Calculate.IsEvenSign(planet_sign_name)


def is_odd_sign(planet_sign_name: ZodiacName) -> bool:
    return VedAstro.Calculate.IsOddSign(planet_sign_name)


def is_fixed_sign(sun_sign: ZodiacName) -> bool:
    return VedAstro.Calculate.IsFixedSign(sun_sign)


def is_movable_sign(sun_sign: ZodiacName) -> bool:
    return VedAstro.Calculate.IsMovableSign(sun_sign)


def is_common_sign(sun_sign: ZodiacName) -> bool:
    return VedAstro.Calculate.IsCommonSign(sun_sign)


def get_planet_permanent_relationship_with_planet(main_planet: PlanetName,
                                                  secondary_planet: PlanetName) -> PlanetToPlanetRelationship:
    return VedAstro.Calculate.PlanetPermanentRelationshipWithPlanet(main_planet, secondary_planet)


def convert_julian_time_to_normal_time(julian_time: float):
    return VedAstro.Calculate.ConvertJulianTimeToNormalTime(julian_time)


def get_greenwich_time_from_julian_days(julian_time: float) -> DateTimeOffset:
    return VedAstro.Calculate.GreenwichTimeFromJulianDays(julian_time)


def get_greenwich_lmt_in_julian_days(time: Time) -> float:
    return VedAstro.Calculate.GreenwichLmtInJulianDays(time)


def get_house_1_and_10_longitudes(time: Time) -> List[float]:
    return VedAstro.Calculate.House1And10Longitudes(time)


def lmt_to_utc(time: Time) -> DateTimeOffset:
    return VedAstro.Calculate.LmtToUtc(time)


def get_gochara_house(birth_time: Time, current_time: Time, planet: PlanetName) -> int:
    return VedAstro.Calculate.GocharaHouse(birth_time, current_time, planet)


def is_gochara_obstructed(planet: PlanetName, gochara_house: int, birth_time: Time, current_time: Time) -> bool:
    return VedAstro.Calculate.IsGocharaObstructed(planet, gochara_house, birth_time, current_time)


def get_planets_in_gochara_house(birth_time: Time, current_time: Time, gochara_house: int) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsInGocharaHouse(birth_time, current_time, gochara_house)


def get_vedhanka(planet: PlanetName, house: int) -> int:
    return VedAstro.Calculate.Vedhanka(planet, house)


def is_gochara_occurring(birth_time: Time, time: Time, planet: PlanetName, gochara_house: int) -> bool:
    return VedAstro.Calculate.IsGocharaOccurring(birth_time, time, planet, gochara_house)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return VedAstro.Calculate.CurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return VedAstro.Calculate.CurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return VedAstro.Calculate.DasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return VedAstro.Calculate.NextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return VedAstro.Calculate.TimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return VedAstro.Calculate.YearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return VedAstro.Calculate.DasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return VedAstro.Calculate.DasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return VedAstro.Calculate.BhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return VedAstro.Calculate.AntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return VedAstro.Calculate.SukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                     sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return VedAstro.Calculate.PranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                   sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return VedAstro.Calculate.ConstellationDasaPlanet(constellation_name)


def get_planet_dasa_major_planet_and_minor_relationship(major_planet: PlanetName, minor_planet: PlanetName):
    return VedAstro.Calculate.PlanetDasaMajorPlanetAndMinorRelationship(major_planet, minor_planet)


def get_current_dasa_count_from_birth(birth_time: Time, current_time: Time) -> int:
    return VedAstro.Calculate.CurrentDasaCountFromBirth(birth_time, current_time)


def get_current_dasa_bhukti_antaram(birth_time: Time, current_time: Time) -> Dasas:
    return VedAstro.Calculate.CurrentDasaBhuktiAntaram(birth_time, current_time)


def get_dasa_counted_from_input_dasa(start_dasa_planet: PlanetName, years: float) -> Dasas:
    return VedAstro.Calculate.DasaCountedFromInputDasa(start_dasa_planet, years)


def get_next_dasa_planet(planet: PlanetName) -> PlanetName:
    return VedAstro.Calculate.NextDasaPlanet(planet)


def get_time_left_in_birth_dasa(birth_time: Time) -> float:
    return VedAstro.Calculate.TimeLeftInBirthDasa(birth_time)


def get_years_traversed_in_birth_dasa(birth_time: Time) -> float:
    return VedAstro.Calculate.YearsTraversedInBirthDasa(birth_time)


def get_dasa_time_per_minute(constellation_name: ConstellationName) -> float:
    return VedAstro.Calculate.DasaTimePerMinute(constellation_name)


def get_dasa_planet_full_years(planet: PlanetName) -> float:
    return VedAstro.Calculate.DasaPlanetFullYears(planet)


def get_bhukti_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName) -> float:
    return VedAstro.Calculate.BhuktiPlanetFullYears(dasa_planet, bhukti_planet)


def get_antaram_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName,
                                  antaram_planet: PlanetName) -> float:
    return VedAstro.Calculate.AntaramPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet)


def get_sukshma_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                  sukshma_planet: PlanetName) -> float:
    return VedAstro.Calculate.SukshmaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                     sukshma_planet)


def get_prana_planet_full_years(dasa_planet: PlanetName, bhukti_planet: PlanetName, antaram_planet: PlanetName,
                                sukshma_planet: PlanetName, prana_planet: PlanetName) -> float:
    return VedAstro.Calculate.PranaPlanetFullYears(dasa_planet, bhukti_planet, antaram_planet,
                                                   sukshma_planet, prana_planet)


def get_constellation_dasa_planet(constellation_name: ConstellationName) -> PlanetName:
    return VedAstro.Calculate.ConstellationDasaPlanet(constellation_name)


def is_mercury_afflicted(time: Time) -> bool:
    return VedAstro.Calculate.IsMercuryAfflicted(time)


def is_mercury_malefic(time: Time) -> bool:
    return VedAstro.Calculate.IsMercuryMalefic(time)


def is_moon_benefic(time: Time) -> bool:
    return VedAstro.Calculate.IsMoonBenefic(time)


def is_planet_benefic(planet_name: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetBenefic(planet_name, time)


def get_benefic_planet_list(time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.BeneficPlanetList(time)


def is_planet_malefic(planet_name: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetMalefic(planet_name, time)


def get_malefic_planet_list(time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.MaleficPlanetList(time)


def get_planets_in_aspect(planet: PlanetName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsInAspect(planet, time)


def get_planets_aspecting_planet(time: Time, receiving_aspect: PlanetName) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsAspectingPlanet(time, receiving_aspect)


def get_houses_in_aspect(planet: PlanetName, time: Time) -> List[HouseName]:
    return VedAstro.Calculate.HousesInAspect(planet, time)


def get_planets_aspecting_house(input_house: HouseName, time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.PlanetsAspectingHouse(input_house, time)


def is_planet_aspected_by_planet(receiving_aspect: PlanetName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_house_aspected_by_planet(receiving_aspect: HouseName, transmitting_aspect: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsHouseAspectedByPlanet(receiving_aspect, transmitting_aspect, time)


def is_planet_conjunct_with_planet(planet_a: PlanetName, planet_b: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetConjunctWithPlanet(planet_a, planet_b, time)


def get_all_planet_ordered_by_strength(time: Time) -> List[PlanetName]:
    return VedAstro.Calculate.AllPlanetOrderedByStrength(time)


def get_all_planet_strength(time: Time) -> List[Tuple[float, PlanetName]]:
    return VedAstro.Calculate.AllPlanetStrength(time)


def get_all_houses_ordered_by_strength(time: Time) -> List[HouseName]:
    return VedAstro.Calculate.AllHousesOrderedByStrength(time)


def get_planet_shadbala_pinda(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetShadbalaPinda(planet_name, time)


def get_planet_strength(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return get_planet_shadbala_pinda(planet_name, time)


def get_planet_drik_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetDrikBala(planet_name, time)


def find_visesha_drishti(dk: float, p: PlanetName) -> float:
    return VedAstro.Calculate.FindViseshaDrishti(dk, p)


def find_drishti_value(dk: float) -> float:
    return VedAstro.Calculate.FindDrishtiValue(dk)


def get_planet_naisargika_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetNaisargikaBala(planet_name, time)


def get_planet_chesta_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetChestaBala(planet_name, time)


def get_madhya(epoch_to_birth_days: float, time1: Time) -> Dict[PlanetName, float]:
    return VedAstro.Calculate.Madhya(epoch_to_birth_days, time1)


def get_epoch_interval(time1: Time) -> float:
    return VedAstro.Calculate.EpochInterval(time1)


def get_planet_motion_name(planet_name: PlanetName, time: Time) -> PlanetMotion:
    return VedAstro.Calculate.PlanetMotionName(planet_name, time)


def get_planet_circulation_time(planet_name: PlanetName) -> float:
    return VedAstro.Calculate.PlanetCirculationTime(planet_name)


def get_planet_saptavargaja_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetSaptavargajaBala(planet_name, time)


def get_planet_shadvarga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetShadvargaBala(planet_name, time)


def is_planet_strong_in_shadvarga(planet: PlanetName, time: Time) -> bool:
    return VedAstro.Calculate.IsPlanetStrongInShadvarga(planet, time)


def get_planet_sthana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetSthanaBala(planet_name, time)


def get_planet_drekkana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetDrekkanaBala(planet_name, time)


def get_planet_kendra_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetKendraBala(planet_name, time)


def get_planet_ojayugmarasyamsa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetOjayugmarasyamsaBala(planet_name, time)


def get_planet_kala_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetKalaBala(planet_name, time)


def get_planet_yuddha_bala(inputed_planet: PlanetName, pre_kala_bala_values: Dict[PlanetName, Shashtiamsa],
                           time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetYuddhaBala(inputed_planet, pre_kala_bala_values, time)


def get_planet_ayana_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetAyanaBala(planet_name, time)


def get_planet_declination(planet_name: PlanetName, time: Time) -> float:
    return VedAstro.Calculate.PlanetDeclination(planet_name, time)


def get_ecliptic_obliquity(time: Time) -> float:
    return VedAstro.Calculate.EclipticObliquity(time)


def get_planet_hora_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetHoraBala(planet_name, time)


def get_planet_abda_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetAbdaBala(planet_name, time)


def get_planet_masa_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetMasaBala(planet_name, time)


def get_planet_vara_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetVaraBala(planet_name, time)


def get_year_and_month_lord(time: Time) -> object:
    return VedAstro.Calculate.YearAndMonthLord(time)


def get_planet_tribhaga_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetTribhagaBala(planet_name, time)


def get_planet_ochcha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetOchchaBala(planet_name, time)


def is_day_birth(time: Time) -> bool:
    return VedAstro.Calculate.IsDayBirth(time)


def get_planet_paksha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetPakshaBala(planet_name, time)


def get_planet_nathonnatha_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetNathonnathaBala(planet_name, time)


def get_planet_dig_bala(planet_name: PlanetName, time: Time) -> Shashtiamsa:
    return VedAstro.Calculate.PlanetDigBala(planet_name, time)


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
    return VedAstro.Calculate.BhavaBala(input_house, time)


def calc_bhava_drishti_bala(time: Time) -> HouseSubStrength:
    return VedAstro.Calculate.CalcBhavaDrishtiBala(time)


def calc_bhava_dig_bala(time: Time) -> HouseSubStrength:
    return VedAstro.Calculate.CalcBhavaDigBala(time)


def calc_bhava_adhipathi_bala(time: Time) -> HouseSubStrength:
    return VedAstro.Calculate.CalcBhavaAdhipathiBala(time)


def get_benefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return VedAstro.Calculate.BeneficPlanetListByShadbala(person_birth_time, threshold)


# def get_benefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return VedAstro.Calculate.BeneficPlanetListByShadbala(person_birth_time)


def get_benefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return VedAstro.Calculate.BeneficHouseListByShadbala(person_birth_time, threshold)


#
# def get_benefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return VedAstro.Calculate.BeneficHouseListByShadbala(person_birth_time)


def get_malefic_planet_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[PlanetName]:
    return VedAstro.Calculate.MaleficPlanetListByShadbala(person_birth_time, threshold)


# def get_malefic_planet_list_by_shadbala(person_birth_time: Time) -> List[PlanetName]:
#     return VedAstro.Calculate.MaleficPlanetListByShadbala(person_birth_time)


def get_malefic_house_list_by_shadbala(person_birth_time: Time, threshold: int = 0) -> List[HouseName]:
    return VedAstro.Calculate.MaleficHouseListByShadbala(person_birth_time, threshold)


# def get_malefic_house_list_by_shadbala(person_birth_time: Time) -> List[HouseName]:
#     return VedAstro.Calculate.MaleficHouseListByShadbala(person_birth_time)


# def get_astral_body_prediction(person: Person) -> str:
#     return VedAstro.Calculate.AstralBodyPrediction(person)
# Todo:- can't find reference to this function. Look into that
#
# def get_animal(sign: ConstellationName) -> ConstellationAnimal:
#     return VedAstro.Calculate.Animal(sign)
# Todo:- can't find reference to this function. Look into that

def pd1_planet_full_years(planet):
    """
    Gets the full Dasa years for a given planet
		Note: Returns "double" so that division down the road is accurate
		Ref:Hindu Predictive Astrology pg. 54
    """
    if planet == PlanetName.Sun:
        return 6.0
    if planet == PlanetName.Moon:
        return 10.0
    if planet == PlanetName.Mars:
        return 7.0
    if planet == PlanetName.Rahu:
        return 18.0
    if planet == PlanetName.Jupiter:
        return 16.0
    if planet == PlanetName.Saturn:
        return 19.0
    if planet == PlanetName.Mercury:
        return 17.0
    if planet == PlanetName.Ketu:
        return 7.0
    if planet == PlanetName.Venus:
        return 20.0

def pd2_planet_full_years(pd1_planet, pd2_planet):
    """
    Gets the full years of a bhukti planet in a dasa.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.

    Returns:
        float: The full years of the bhukti planet in the dasa.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a bhukti planet consumes in a dasa is a fixed percentage it consumes in a person's full life.
        - Bhukti planet's years in a dasa is a percentage of the dasa planet's full years.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a bhukti planet consumes in a dasa is a fixed percentage it consumes in a person's full life
    bhukti_planet_percentage = pd1_planet_full_years(pd2_planet) / full_human_life_years

    # Bhukti planet's years in a dasa is a percentage of the dasa planet's full years
    bhukti_planet_full_years = bhukti_planet_percentage * pd1_planet_full_years(pd1_planet)

    # Return the calculated value
    return bhukti_planet_full_years

def pd3_planet_full_years(pd1_planet, pd2_planet, pd3_planet):
    """
    Gets the full years of an antaram planet in a bhukti of a dasa.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.

    Returns:
        float: The full years of the antaram planet in the bhukti of the dasa.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time an antaram planet consumes in a bhukti is a fixed percentage it consumes in a person's full life.
        - Antaram planet's full years is a percentage of the bhukti planet's full years.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time an antaram planet consumes in a bhukti is a fixed percentage it consumes in a person's full life
    antaram_planet_percentage = pd1_planet_full_years(pd3_planet) / full_human_life_years

    # Antaram planet's full years is a percentage of the bhukti planet's full years
    antaram_planet_full_years = antaram_planet_percentage * pd2_planet_full_years(pd1_planet, pd2_planet)

    # Return the calculated value
    return antaram_planet_full_years

def pd4_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet):
    """
    Gets the full time of a Sukshma planet.

    Sukshma is a Sanskrit word meaning "subtle" or "dormant." The presence of sukshma is felt, but not seen.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.
        pd4_planet (PlanetName): The Sukshma planet.

    Returns:
        float: The full time of the Sukshma planet.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a Sukshma planet consumes in an antaram is a fixed percentage it consumes in a person's full life.
        - Sukshma planet's full time is a percentage of the Antaram planet's full time.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a Sukshma planet consumes in an antaram is a fixed percentage it consumes in a person's full life
    sukshma_planet_percentage = pd1_planet_full_years(pd4_planet) / full_human_life_years

    # Sukshma planet's full time is a percentage of the Antaram planet's full time
    sukshma_planet_full_years = sukshma_planet_percentage * pd3_planet_full_years(pd1_planet, pd2_planet, pd3_planet)

    # Return the calculated value
    return sukshma_planet_full_years

def pd5_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet):
    """
    Gets the full time of a Prana planet.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.
        pd4_planet (PlanetName): The Sukshma planet.
        pd5_planet (PlanetName): The Prana planet.

    Returns:
        float: The full time of the Prana planet.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a Prana planet consumes in a Sukshma is a fixed percentage it consumes in a person's full life.
        - Prana planet's full time is a percentage of the Sukshma planet's full time.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a Prana planet consumes in a Sukshma is a fixed percentage it consumes in a person's full life
    pd5_planet_percentage = pd1_planet_full_years(pd5_planet) / full_human_life_years

    # Prana planet's full time is a percentage of the Sukshma planet's full time
    pd5_planet_full_time = pd5_planet_percentage * pd4_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet)

    # Return the calculated value
    return pd5_planet_full_time

def pd6_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet, pd6_planet):
    """
    Gets the full time of a Prana planet.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.
        pd4_planet (PlanetName): The Sukshma planet.
        pd5_planet (PlanetName): The Prana planet.
        pd6_planet (PlanetName): The PD6 planet.

    Returns:
        float: The full time of the PD6 planet.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a PD6 planet consumes in a PD5 is a fixed percentage it consumes in a person's full life.
        - PD6 planet's full time is a percentage of the PD5 planet's full time.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a PD6 planet consumes in a PD5 is a fixed percentage it consumes in a person's full life
    pd6_planet_percentage = pd1_planet_full_years(pd6_planet) / full_human_life_years

    # PD6 planet's full time is a percentage of the PD5 planet's full time
    pd6_planet_full_time = pd6_planet_percentage * pd5_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet)

    # Return the calculated value
    return pd6_planet_full_time

def pd7_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet, pd6_planet, pd7_planet):
    """
    Gets the full time of a Prana planet.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.
        pd4_planet (PlanetName): The Sukshma planet.
        pd5_planet (PlanetName): The Prana planet.
        pd6_planet (PlanetName): The PD6 planet.
        pd7_planet (PlanetName): The PD7 planet.

    Returns:
        float: The full time of the PD7 planet.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a PD7 planet consumes in a PD6 is a fixed percentage it consumes in a person's full life.
        - PD7 planet's full time is a percentage of the PD6 planet's full time.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a PD7 planet consumes in a PD6 is a fixed percentage it consumes in a person's full life
    pd7_planet_percentage = pd1_planet_full_years(pd7_planet) / full_human_life_years

    # PD7 planet's full time is a percentage of the PD6 planet's full time
    pd7_planet_full_time = pd7_planet_percentage * pd6_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet, pd6_planet)

    # Return the calculated value
    return pd7_planet_full_time


def pd8_planet_full_years(pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet, pd6_planet, pd7_planet, pd8_planet):
    """
    Gets the full time of a PD8 planet.

    Parameters:
        pd1_planet (PlanetName): The dasa planet.
        pd2_planet (PlanetName): The bhukti planet.
        pd3_planet (PlanetName): The antaram planet.
        pd4_planet (PlanetName): The Sukshma planet.
        pd5_planet (PlanetName): The Prana planet.
        pd6_planet (PlanetName): The PD6 planet.
        pd7_planet (PlanetName): The PD7 planet.
        pd8_planet (PlanetName): The PD8 planet.

    Returns:
        float: The full time of the PD8 planet.

    Notes:
        - The total of all the dasa planet's years is assumed to be 120 years.
        - The time a PD8 planet consumes in a PD7 is a fixed percentage it consumes in a person's full life.
        - PD8 planet's full time is a percentage of the PD7 planet's full time.
    """
    # 120 years is the total of all the dasa planet's years
    full_human_life_years = 120.0

    # The time a PD8 planet consumes in a PD7 is a fixed percentage it consumes in a person's full life
    pd8_planet_percentage = pd1_planet_full_years(pd8_planet) / full_human_life_years

    # PD8 planet's full time is a percentage of the PD7 planet's full time
    pd8_planet_full_time = pd8_planet_percentage * pd7_planet_full_years(
        pd1_planet, pd2_planet, pd3_planet, pd4_planet, pd5_planet, pd6_planet, pd7_planet
    )

    # Return the calculated value
    return pd8_planet_full_time

