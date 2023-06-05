from dataclasses import dataclass


from VedAstro.Library import PlanetName

class Planets(PlanetName):
    """
    This class represents the nine planets in Vedic astrology.

    Attributes:
        sun (PlanetName): The sun planet.
        moon (PlanetName): The moon planet.
        mars (PlanetName): The mars planet.
        mercury (PlanetName): The mercury planet.
        jupiter (PlanetName): The jupiter planet.
        venus (PlanetName): The venus planet.
        saturn (PlanetName): The saturn planet.
        ketu (PlanetName): The ketu planet.
        rahu (PlanetName): The rahu planet.
    """
    sun = PlanetName.Sun
    moon = PlanetName.Moon
    mars = PlanetName.Mars
    mercury = PlanetName.Mercury
    jupiter = PlanetName.Jupiter
    venus = PlanetName.Venus
    saturn = PlanetName.Saturn
    ketu = PlanetName.Ketu
    rahu = PlanetName.Rahu

# Todo:- just for now stored as attribs. Need to change in future