import VedAstro.Library as libray


class EventTag:
    Agriculture = libray.EventTag.Agriculture,
    General = libray.EventTag.General,
    Personal = libray.EventTag.Personal,
    Yoga = libray.EventTag.Yoga,
    RulingConstellation = libray.EventTag.RulingConstellation,
    HairNailCutting = libray.EventTag.HairNailCutting,
    Medical = libray.EventTag.Medical,
    Debug = libray.EventTag.Debug,
    Marriage = libray.EventTag.Marriage,
    Astronomical = libray.EventTag.Astronomical,
    BuyingSelling = libray.EventTag.BuyingSelling,
    Building = libray.EventTag.Building,
    Gochara = libray.EventTag.Gochara,
    Dasa = libray.EventTag.Dasa,
    Bhukti = libray.EventTag.Bhukti,
    Antaram = libray.EventTag.Antaram,
    Sukshma = libray.EventTag.Sukshma,  # weeks
    Prana = libray.EventTag.Prana,  # days
    DasaSpecialRules = libray.EventTag.DasaSpecialRules,
    Horoscope = libray.EventTag.Horoscope,
    Tarabala = libray.EventTag.Tarabala,
    Chandrabala = libray.EventTag.Chandrabala,
    Travel = libray.EventTag.Travel,
    RisingSign = libray.EventTag.RisingSign,  # used in birth time finder
    GocharaSummary = libray.EventTag.GocharaSummary,

    @staticmethod
    def get_eventtag_type():
        return libray.EventTag
