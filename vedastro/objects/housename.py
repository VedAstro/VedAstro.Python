import VedAstro.Library as VedAstro
class HouseName:
    """
    return a tuple of given housename.
    tuple has only one element.
    """

    HOUSE1 = VedAstro.HouseName.House1,
    HOUSE2 = VedAstro.HouseName.House2,
    HOUSE3 = VedAstro.HouseName.House3,
    HOUSE4 = VedAstro.HouseName.House4,
    HOUSE5 = VedAstro.HouseName.House5,
    HOUSE6 = VedAstro.HouseName.House6,
    HOUSE7 = VedAstro.HouseName.House7,
    HOUSE8 = VedAstro.HouseName.House8,
    HOUSE9 = VedAstro.HouseName.House9,
    HOUSE10 = VedAstro.HouseName.House10,
    HOUSE11 = VedAstro.HouseName.House11,
    HOUSE12 = VedAstro.HouseName.House12


    @staticmethod
    def get_house_no(house_name):
        """
        return house number of given house name.
        """
        match house_name:
            case HouseName.HOUSE1:
                return 1
            case HouseName.HOUSE2:
                return 2
            case HouseName.HOUSE3:
                return 3
            case HouseName.HOUSE4:
                return 4
            case HouseName.HOUSE5:
                return 5
            case HouseName.HOUSE6:
                return 6
            case HouseName.HOUSE7:
                return 7
            case HouseName.HOUSE8:
                return 8
            case HouseName.HOUSE9:
                return 9
            case HouseName.HOUSE10:
                return 10
            case HouseName.HOUSE11:
                return 11
            case HouseName.HOUSE12:
                return 12
            case _:
                return None



    @staticmethod
    def get_house_name(house_no):
        """
        return house name of given house number.
        """
        match house_no:
            case 1:
                return HouseName.HOUSE1
            case 2:
                return HouseName.HOUSE2
            case 3:
                return HouseName.HOUSE3
            case 4:
                return HouseName.HOUSE4
            case 5:
                return HouseName.HOUSE5
            case 6:
                return HouseName.HOUSE6
            case 7:
                return HouseName.HOUSE7
            case 8:
                return HouseName.HOUSE8
            case 9:
                return HouseName.HOUSE9
            case 10:
                return HouseName.HOUSE10
            case 11:
                return HouseName.HOUSE11
            case 12:
                return HouseName.HOUSE12
            case _:
                return None



