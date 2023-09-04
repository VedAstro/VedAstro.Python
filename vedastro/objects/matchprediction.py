from enum import Enum

import VedAstro.Library as VedAstro


class MatchPredictionName(Enum):
    Empty = 0,
    Mahendra = 1,
    NadiKuta = 2,
    GunaKuta = 3,
    Varna = 4,
    YoniKuta = 5,
    Vedha = 6,
    VasyaKuta = 7,
    GrahaMaitram = 8,
    RasiKuta = 9,
    StreeDeergha = 10,
    DinaKuta = 11,
    KujaDosa = 12,
    Rajju = 13,
    LagnaAnd7thGood = 14,
    BadConstellation = 15,
    SexEnergyCompatibility = 16


class EventNature(Enum):
    Empty = 0,
    Good = 1,
    Neutral = 2,
    Bad = 3


class MatchPrediction(VedAstro.MatchPrediction):

    def __init__(self, name: MatchPredictionName, nature: EventNature, male_info: str, female_info: str, info: str,
                 description: str):
        self.super.__init__(self, name, nature, male_info, female_info, info, description)
