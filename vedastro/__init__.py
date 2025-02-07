import os # used to get file paths

# welcome message
print("VedAstro - Made & Funded by Users - https://vedastro.org/Donate\n")

# check if current package is up to date else warn user
from.update_check import check_for_update
check_for_update("vedastro")

from.vedastro import *
from.calculate import *


