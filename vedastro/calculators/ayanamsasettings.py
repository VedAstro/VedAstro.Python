from enum import Enum

import VedAstro.Library as VedAstro


class AyanamsaSettings:
    """
    Represents ayanamsa settings including the year of coincidence.

    Usage:
    - To set the year of coincidence: AstrologySettings.YearOfCoincidence = new_value
    - To get the year of coincidence: current_value = AstrologySettings.YearOfCoincidence
    """

    # Initialize the property with the default value corresponding to Library.Ayanamsa.Raman
    YearOfCoincidence = int(VedAstro.Library.Ayanamsa.Raman)

    @classmethod
    def get_year_of_coincidence(cls):
        """
        Get the current year of coincidence.

        Returns:
            int: The current year of coincidence.
        """
        return cls.YearOfCoincidence

    @classmethod
    def set_year_of_coincidence(cls, value):
        """
        Set the year of coincidence to a new value.

        Parameters:
            value (int): The new value for the year of coincidence.
        """
        cls.YearOfCoincidence = value


class Ayanamsa(Enum):
    """
    Represents different Ayanamsa values.

    Enum Members:
    - Yukteshwar: The meeting of V.E. with the first point of Aries took place in 499 A.D.
    - Raman: B.V.Raman accepted 397 AD as the Zero Ayanamsa Year.
    - Lahiri: N.C.Lahiri took 285 AD as the Zero Ayanamsa Year.
    - Krishnamurti: K.S.Krishnamurti fixed 291 AD as the Zero Ayanamsa Year.
    - Western: Western astrology does not use ayanamsa, set year 0.
    """

    Yukteshwar = 499
    Raman = 397
    Lahiri = 285
    Krishnamurti = 291
    Western = 0
