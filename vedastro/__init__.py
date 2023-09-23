import os # used to get file paths
from pythonnet import load


# welcome message
print("VedAstro - Made & Funded by Users - https://vedastro.org/Donate\n")

# check if current package is up to date else warn user
from .update_check import check_for_update
check_for_update("vedastro")

# initialize the VedAstro by loading the necessary DLL and setting up the runtime configuration.
current_path = os.path.dirname(os.path.abspath(__file__))
dll_path = os.path.join(current_path, 'dlls', 'VedAstro.Library.dll')
full_path = os.path.abspath(dll_path)

# load CLR settings first, else won't work
runtime_config_path = os.path.abspath(os.path.join(current_path, 'runtimeconfig.json'))
load("coreclr", runtime_config=runtime_config_path)

try:

    #note CLR can only be imported AFTER runtime config has been set above
    import clr # provided by the Pythonnet package

    # Add reference to .NET assembly
    clr.AddReference(full_path)
    clr.AddReference('VedAstro.Library')
    
    # Import the namespace from the assembly
    from VedAstro.Library import *
    

except RuntimeError:
    print(f"Dotnet 7 not found. please visit https://dotnet.microsoft.com/en-us/download/dotnet/7.0")


