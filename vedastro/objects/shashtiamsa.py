import VedAstro.Library as VedAstro

class Shashtiamsa(VedAstro.Shashtiamsa):


    def __init__(self):
        super().__init__()


    def to_double(self):
        return super().ToDouble()

    def to_rupa(self):
        return super().ToRupa()


   # //METHODS
   #      public double ToDouble() => _shashtiamsaAsDouble;
   #
   #      //This divided by 60 will give shashtiamsa in rupas
   #      public double ToRupa() => _shashtiamsaAsDouble / 60;
