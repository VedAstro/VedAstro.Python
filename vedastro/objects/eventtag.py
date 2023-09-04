import VedAstro.Library as library


class EventTag:
    Agriculture = library.EventTag.Agriculture,
    General = library.EventTag.General,
    Personal = library.EventTag.Personal,
    Yoga = library.EventTag.Yoga,
    RulingConstellation = library.EventTag.RulingConstellation,
    HairNailCutting = library.EventTag.HairNailCutting,
    Medical = library.EventTag.Medical,
    Debug = library.EventTag.Debug,
    Marriage = library.EventTag.Marriage,
    Astronomical = library.EventTag.Astronomical,
    BuyingSelling = library.EventTag.BuyingSelling,
    Building = library.EventTag.Building,
    Gochara = library.EventTag.Gochara,
    Dasa = library.EventTag.Dasa,
    Bhukti = library.EventTag.Bhukti,
    Antaram = library.EventTag.Antaram,
    Sukshma = library.EventTag.Sukshma,  # weeks
    Prana = library.EventTag.Prana,  # days
    DasaSpecialRules = library.EventTag.DasaSpecialRules,
    Horoscope = library.EventTag.Horoscope,
    Tarabala = library.EventTag.Tarabala,
    Chandrabala = library.EventTag.Chandrabala,
    Travel = library.EventTag.Travel,
    RisingSign = library.EventTag.RisingSign,  # used in birth time finder
    GocharaSummary = library.EventTag.GocharaSummary,

    @staticmethod
    def get_eventtag_type():
        return library.EventTag
