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
        # Compare versions
        if version.parse(installed_version) < version.parse(latest_version):
            print(f"A better version of the awesome VedAstro package is available. Your version is {installed_version}, latest is {latest_version}.")
            update = input("Would you like to update now? (y/n) ")
            if update.lower() == 'y':
                subprocess.check_call(f"pip install --upgrade {package_name}", shell=True)
    except Exception as e:
        # print(f"An error occurred: {e}")
        return
