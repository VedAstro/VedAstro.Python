import pkg_resources
from packaging import version
import requests
import subprocess


def check_for_update(package_name):
    # Get the installed version
    installed_version = pkg_resources.get_distribution(package_name).version
    
    # Get the latest version
    response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
    latest_version = response.json()['info']['version']
    
    # Compare versions
    if version.parse(installed_version) < version.parse(latest_version):
        print(f"A better version of the awesome VedAstro package is available. Your version is {installed_version}, latest is {latest_version}.")
        update = input("Would you like to update now? (y/n) ")
        if update.lower() == 'y':
            subprocess.check_call(f"pip install --upgrade {package_name}", shell=True)
    # else:
    #     print(f"You are using the latest version of {package_name}. Installed version and latest version are {installed_version}.")
