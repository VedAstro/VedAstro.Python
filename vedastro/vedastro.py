import requests
import json
from enum import Enum

class GeoLocation:
    def __init__(self, location_name, longitude, latitude):
        """
        Initialize a GeoLocation object.

        Args:
        location_name (str): The name of the location.
        longitude (float): The longitude of the location.
        latitude (float): The latitude of the location.
        """
        self.location_name = location_name
        self.longitude = longitude
        self.latitude = latitude

    def __str__(self):
        """
        Return a string representation of the GeoLocation object.
        """
        return f"{self.location_name} ({self.longitude}, {self.latitude})"

class Time:
    def __init__(self, time_string, geolocation):
        """
        Initialize a Time object.

        Args:
        time_string (str): A string representing the time in the format "HH:MM DD/MM/YYYY +HH:MM".
        geolocation (GeoLocation): The geolocation associated with the time.
        """
        self.time_string = time_string
        self.geolocation = geolocation

    def __str__(self):
        """
        Return a string representation of the Time object.
        """
        return f"{self.time_string} at {self.geolocation}"

    def url_time_string(self):
        """
        Return the time string formatted as "HH:MM/DD/MM/YYYY/+HH:MM"
        """
        time_parts = self.time_string.split()
        time = time_parts[0]
        date = time_parts[1].split('/')
        offset = time_parts[2]
        return f"{time}/{date[0]}/{date[1]}/{date[2]}/{offset}"

class PlanetName(Enum):
    All = "All"
    Sun = "Sun"
    Moon = "Moon"
    Mars = "Mars"
    Mercury = "Mercury"
    Jupiter = "Jupiter"
    Venus = "Venus"
    Saturn = "Saturn"
    Rahu = "Rahu"
    Ketu = "Ketu"

class HouseName(Enum):
    House1 = "House1"
    House2 = "House2"
    House3 = "House3"
    House4 = "House4"
    House5 = "House5"
    House6 = "House6"
    House7 = "House7"
    House8 = "House8"
    House9 = "House9"
    House10 = "House10"
    House11 = "House11"
    House12 = "House12"

class ZodiacName(Enum):
    Aries = "Aries"
    Taurus = "Taurus"
    Gemini = "Gemini"
    Cancer = "Cancer"
    Leo = "Leo"
    Virgo = "Virgo"
    Libra = "Libra"
    Scorpio = "Scorpio"
    Sagittarius = "Sagittarius"
    Capricorn = "Capricorn"
    Aquarius = "Aquarius"
    Pisces = "Pisces"

class ChartType(Enum):
    """Enum for various chart types based on house longitudes."""
    BhavaChalit = 1
    RasiD1 = 2
    HoraD2 = 3
    DrekkanaD3 = 4
    ChaturthamshaD4 = 5
    SaptamshaD7 = 6
    NavamshaD9 = 7
    DashamamshaD10 = 8
    DwadashamshaD12 = 9
    ShodashamshaD16 = 10
    VimshamshaD20 = 11
    ChaturvimshamshaD24 = 12
    BhamshaD27 = 13
    TrimshamshaD30 = 14
    KhavedamshaD40 = 15
    AkshavedamshaD45 = 16
    ShashtyamshaD60 = 17

class DayOfWeek(Enum):
    Sunday = 1
    Monday = 2
    Tuesday = 3
    Wednesday = 4
    Thursday = 5
    Friday = 6
    Saturday = 7

class ConstellationName(Enum):
    Empty = 0
    Aswini = 1
    Bharani = 2
    Krithika = 3
    Rohini = 4
    Mrigasira = 5
    Aridra = 6
    Punarvasu = 7
    Pushyami = 8
    Aslesha = 9
    Makha = 10
    Pubba = 11
    Uttara = 12  # Uttara Phalguni
    Hasta = 13
    Chitta = 14
    Swathi = 15
    Vishhaka = 16
    Anuradha = 17
    Jyesta = 18
    Moola = 19
    Poorvashada = 20
    Uttarashada = 21
    Sravana = 22
    Dhanishta = 23
    Satabhisha = 24
    Poorvabhadra = 25
    Uttarabhadra = 26
    Revathi = 27
    # Abhijit = 28  # Uncomment if needed

class Avasta(Enum):
    """Represents different emotional states."""
    
    # Kshudita/hungry
    KshuditaStarved = 1
    
    # Trashita/thirsty
    TrishitaThirst = 2
    
    # Lajjita/humiliated
    LajjitaShamed = 3
    
    # Garvita/proud
    GarvitaProud = 4
    
    # Mudita/sated/happy
    MuditaDelighted = 5
    
    # Kshobhita/guilty/repentant
    KshobitaAgitated = 6

class Ayanamsa(Enum):
    Fagan_Bradley = 0
    Lahiri = 1
    Deluce = 2
    Raman = 3
    Ushashashi = 4
    Krishnamurti = 5
    Djwhal_Khul = 6
    Yukteshwar = 7
    Jn_Bhasin = 8
    Babyl_Kugler1 = 9
    Babyl_Kugler2 = 10
    Babyl_Kugler3 = 11
    Babyl_Huber = 12
    Babyl_Etpsc = 13
    Aldebaran_15Tau = 14
    Hipparchos = 15
    Sassanian = 16
    Galcent_0Sag = 17
    J2000 = 18
    J1900 = 19
    B1950 = 20
    Suryasiddhanta = 21
    Suryasiddhanta_MSun = 22
    Aryabhata = 23
    Aryabhata_MSun = 24
    Ss_Revati = 25
    Ss_Citra = 26
    True_Citra = 27
    True_Revati = 28
    True_Pushya = 29
    Galcent_Rgbrand = 30
    Galequ_Iau1958 = 31
    Galequ_True = 32
    Galequ_Mula = 33
    Galalign_Mardyks = 34
    True_Mula = 35
    Galcent_Mula_Wilhelm = 36
    Aryabhata_522 = 37
    Babyl_Britton = 38
    True_Sheoran = 39
    Galcent_Cochrane = 40
    Galequ_Fiorenza = 41
    Valens_Moon = 42
    Lahiri_1940 = 43
    Lahiri_VP285 = 44
    Krishnamurti_VP291 = 45
    Lahiri_ICRC = 46

class Karana(Enum):
    Bava = 1
    Balava = 2
    Kaulava = 3
    Taitula = 4
    Garija = 5
    Vanija = 6
    Visti = 7  # AKA Bhadra
    Sakuna = 8  # AKA Sakuni
    Chatushpada = 9
    Naga = 10
    Kimstughna = 11

class LunarDayGroup(Enum):
    Nanda = 1
    Bhadra = 2
    Jaya = 3
    Rikta = 4
    Purna = 5

class LunarMonth(Enum):
    Empty = 0
    Chaitra = 1
    Vaisaakha = 2
    Jyeshtha = 3
    Aashaadha = 4
    Sraavana = 5
    Bhaadrapada = 6
    Aaswayuja = 7
    Kaarteeka = 8
    Maargasira = 9
    Pushya = 10
    Maagha = 11
    Phaalguna = 12
    ChaitraAdhika = 13
    VaisaakhaAdhika = 14
    JyeshthaAdhika = 15
    AashaadhaAdhika = 16
    SraavanaAdhika = 17
    BhaadrapadaAdhika = 18
    AaswayujaAdhika = 19
    KaarteekaAdhika = 20
    MaargasiraAdhika = 21
    PushyaAdhika = 22
    MaaghaAdhika = 23
    PhaalgunaAdhika = 24
