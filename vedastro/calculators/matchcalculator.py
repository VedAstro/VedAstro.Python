import VedAstro.Library as libray

from vedastro.objects import Person
from vedastro.objects.matchprediction import MatchPrediction
from vedastro.objects.matchreport import MatchReport


def GetNewMatchReport(male: Person, female: Person, user_id: str) -> MatchReport:
    return libray.MatchCalculator.GetNewMatchReport(male, female, user_id)


def Mahendra(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.Mahendra(male, female)


def NadiKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.NadiKuta(male, female)


def GunaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.GunaKuta(male, female)


def Varna(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.Varna(male, female)


def YoniKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.YoniKuta(male, female)


def VedhaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.VedhaKuta(male, female)


def Rajju(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.Rajju(male, female)


def VasyaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.VasyaKuta(male, female)


def GrahaMaitram(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.GrahaMaitram(male, female)


def RasiKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.RasiKuta(male, female)


def StreeDeergha(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.StreeDeergha(male, female)


def DinaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.DinaKuta(male, female)


def LagnaAndHouse7Good(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.LagnaAndHouse7Good(male, female)


def KujaDosa(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.KujaDosa(male, female)


def BadConstellations(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.BadConstellations(male, female)


def SexEnergyCompatibility(male: Person, female: Person) -> MatchPrediction:
    return libray.MatchCalculator.SexEnergyCompatibility(male, female)
