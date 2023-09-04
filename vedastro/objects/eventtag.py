import VedAstro.Library as VedAstro


class EventTag:
    Agriculture = VedAstro.EventTag.Agriculture,
    General = VedAstro.EventTag.General,
    Personal = VedAstro.EventTag.Personal,
    Yoga = VedAstro.EventTag.Yoga,
    RulingConstellation = VedAstro.EventTag.RulingConstellation,
    HairNailCutting = VedAstro.EventTag.HairNailCutting,
    Medical = VedAstro.EventTag.Medical,
    Debug = VedAstro.EventTag.Debug,
    Marriage = VedAstro.EventTag.Marriage,
    Astronomical = VedAstro.EventTag.Astronomical,
    BuyingSelling = VedAstro.EventTag.BuyingSelling,
    Building = VedAstro.EventTag.Building,
    Gochara = VedAstro.EventTag.Gochara,
    Dasa = VedAstro.EventTag.Dasa,
    Bhukti = VedAstro.EventTag.Bhukti,
    Antaram = VedAstro.EventTag.Antaram,
    Sukshma = VedAstro.EventTag.Sukshma,  # weeks
    Prana = VedAstro.EventTag.Prana,  # days
    DasaSpecialRules = VedAstro.EventTag.DasaSpecialRules,
    Horoscope = VedAstro.EventTag.Horoscope,
    Tarabala = VedAstro.EventTag.Tarabala,
    Chandrabala = VedAstro.EventTag.Chandrabala,
    Travel = VedAstro.EventTag.Travel,
    RisingSign = VedAstro.EventTag.RisingSign,  # used in birth time finder
    GocharaSummary = VedAstro.EventTag.GocharaSummary,

    @staticmethod
    def get_eventtag_type():
        return VedAstro.EventTag
