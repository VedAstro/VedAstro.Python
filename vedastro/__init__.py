import os
from pythonnet import load

current_path = os.path.dirname(os.path.abspath(__file__))

runtimeconfig_path = os.path.abspath(os.path.join(current_path, 'runtimeconfig.json'))
print(runtimeconfig_path)
load("coreclr", runtime_config=runtimeconfig_path)
import clr

# loading project dlls

dll_path = os.path.join(current_path, 'dlls', 'VedAstro.Library.dll')
full_path = os.path.abspath(dll_path)
clr.AddReference(full_path)
