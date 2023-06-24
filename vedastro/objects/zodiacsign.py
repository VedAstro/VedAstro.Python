import VedAstro.Library as libray

from vedastro.objects import ZodiacName
from vedastro.objects.angle import Angle


class ZodiacSign():

    def __init__(self, sign_name: ZodiacName, degrees_in_sign: Angle):
        self.zodiac_name = sign_name
        self.degrees_in_sign = degrees_in_sign
    #
    # def get_sign_name(self):
    #     return libray.ZodiacSign.GetSignName()
    #
    # def get_degrees_in_sign(self):
    #     return libray.ZodiacSign.GetDegreesInSign()
    #
    #
