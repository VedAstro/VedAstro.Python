import VedAstro.Library as libray

from vedastro.objects import Person
from vedastro.objects.matchprediction import MatchPrediction
from vedastro.objects.matchreport import MatchReport


def GetNewMatchReport(male: Person, female: Person, user_id: str) -> MatchReport:
    return libray.GetNewMatchReport(male, female, user_id)


def Mahendra(male: Person, female: Person) -> MatchPrediction:
    return libray.Mahendra(male, female)


def NadiKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.NadiKuta(male, female)


def GunaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.GunaKuta(male, female)


def Varna(male: Person, female: Person) -> MatchPrediction:
    return libray.Varna(male, female)


def YoniKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.YoniKuta(male, female)


def VedhaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.VedhaKuta(male, female)


def Rajju(male: Person, female: Person) -> MatchPrediction:
    return libray.Rajju(male, female)


def VasyaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.VasyaKuta(male, female)


def GrahaMaitram(male: Person, female: Person) -> MatchPrediction:
    return libray.GrahaMaitram(male, female)


def RasiKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.RasiKuta(male, female)


def StreeDeergha(male: Person, female: Person) -> MatchPrediction:
    return libray.StreeDeergha(male, female)


def DinaKuta(male: Person, female: Person) -> MatchPrediction:
    return libray.DinaKuta(male, female)


def LagnaAndHouse7Good(male: Person, female: Person) -> MatchPrediction:
    return libray.LagnaAndHouse7Good(male, female)


def KujaDosa(male: Person, female: Person) -> MatchPrediction:
    return libray.KujaDosa(male, female)


def BadConstellations(male: Person, female: Person) -> MatchPrediction:
    return libray.BadConstellations(male, female)


def SexEnergyCompatibility(male: Person, female: Person) -> MatchPrediction:
    return libray.SexEnergyCompatibility(male, female)
