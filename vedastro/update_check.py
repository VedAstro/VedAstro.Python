from colorama import Fore, Style
import pkg_resources
from packaging import version
import requests
import subprocess


def check_for_update(package_name):
    try:
        
        # Get the installed version
        installed_version = pkg_resources.get_distribution(package_name).version
        
        # Get the latest version
        response = requests.get(f'https://pypi.org/pypi/{package_name}/json')
        latest_version = response.json()['info']['version']
        
        # Compare versions & start AUTO Update if possible
        # NOTE: default to auto update for easy server use
        if version.parse(installed_version) < version.parse(latest_version):
            #warn user
            print(Fore.YELLOW + f"VedAstro Package Outdated! {installed_version} --> {latest_version}" + Style.RESET_ALL)
            #start auto update
            print(Fore.GREEN + f"Starting Update..." + Style.RESET_ALL)
            subprocess.check_call(f"pip install --upgrade {package_name}", shell=True)
    
    except Exception as e:
        # print(f"An error occurred: {e}")
        return
