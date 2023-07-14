import os
from pythonnet import load

current_path = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_path, 'dlls', 'VedAstro.Library.dll')
full_path = os.path.abspath(dll_path)

runtime_config_path = os.path.abspath(os.path.join(current_path, 'runtimeconfig.json'))

load("coreclr", runtime_config=runtime_config_path)
import clr
clr.AddReference(full_path)
