import VedAstro.Library as VedAstro
from vedastro.objects import Person
from vedastro.objects.matchprediction import MatchPrediction
from vedastro.objects.matchreport import MatchReport


def GetNewMatchReport(male: Person, female: Person, user_id: str) -> MatchReport:
    """
    Calculates and returns a new match report between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.
        user_id (str): The user ID.

    Returns:
        MatchReport: The match report object.
    """
    return VedAstro.MatchCalculator.GetNewMatchReport(male, female, user_id)


def Mahendra(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Mahendra match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.Mahendra(male, female)


def NadiKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Nadi Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.NadiKuta(male, female)


def GunaKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Guna Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.GunaKuta(male, female)


def Varna(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Varna match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.Varna(male, female)


def YoniKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Yoni Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.YoniKuta(male, female)


def VedhaKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Vedha Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.VedhaKuta(male, female)


def Rajju(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Rajju match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.Rajju(male, female)


def VasyaKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Vasya Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.VasyaKuta(male, female)


def GrahaMaitram(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Graha Maitram match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.GrahaMaitram(male, female)


def RasiKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Rasi Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.RasiKuta(male, female)


def StreeDeergha(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Stree Deergha match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.StreeDeergha(male, female)


def DinaKuta(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Dina Kuta match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.DinaKuta(male, female)


def LagnaAndHouse7Good(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the match prediction for Lagna and House 7 compatibility between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.LagnaAndHouse7Good(male, female)


def KujaDosa(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the Kuja Dosa match prediction between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.KujaDosa(male, female)


def BadConstellations(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the match prediction for bad constellations between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.BadConstellations(male, female)


def SexEnergyCompatibility(male: Person, female: Person) -> MatchPrediction:
    """
    Calculates and returns the match prediction for sex energy compatibility between a male and female person.

    Args:
        male (Person): The male person object.
        female (Person): The female person object.

    Returns:
        MatchPrediction: The match prediction object.
    """
    return VedAstro.MatchCalculator.SexEnergyCompatibility(male, female)
