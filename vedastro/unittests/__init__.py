import os
from pythonnet import load

load("coreclr")
import clr

# loading project dlls
current_path = os.path.dirname(os.path.abspath(__file__))

dll_path = os.path.join(current_path, 'dlls', 'VedAstro.Library.dll')
full_path = os.path.abspath(dll_path)
clr.AddReference(full_path)
#
# from ..planets import Planets
# from ..astronomical_calculator import Calculator
# from ..time import Time
# from ..geolocation import GeoLocation
