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
