import pkg_resources
from packaging import version
import subprocess


# checks pip package if outdated
def check_for_update(package_name):
    
    # Get the installed version
    installed_version = pkg_resources.get_distribution(package_name).version
    
    # Get the latest version
    pypi_info = subprocess.check_output(f"pip show {package_name}", shell=True).decode()
    latest_version = [line.split(": ")[1] for line in pypi_info.split("\n") if "Version" in line][0]
    
    # Compare versions
    if version.parse(installed_version) < version.parse(latest_version):
        print(f"A new version of {package_name} is available. You are currently using version {installed_version}, but version {latest_version} is available.")
        update = input("Would you like to update now? (y/n) ")
        if update.lower() == 'y':
            subprocess.check_call(f"pip install --upgrade {package_name}", shell=True)
