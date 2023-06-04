import os
from pythonnet import load
load("coreclr")
import clr

# loading project dlls
dll_path = os.path.join('dlls', 'VedAstro.Library.dll')
full_path = os.path.abspath(dll_path)
clr.AddReference(full_path)
