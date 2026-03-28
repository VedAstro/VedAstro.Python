from colorama import Fore, Style
from packaging import version
import requests
import subprocess
import sys


def check_for_update(package_name):
    try:
        from importlib.metadata import version as get_version
        installed_version = get_version(package_name)

        response = requests.get(f'https://pypi.org/pypi/{package_name}/json', timeout=5)
        latest_version = response.json()['info']['version']

        if version.parse(installed_version) < version.parse(latest_version):
            print(Fore.YELLOW + f"VedAstro Update Available: {installed_version} --> {latest_version}" + Style.RESET_ALL)
            print(Fore.YELLOW + "Auto-updating..." + Style.RESET_ALL)
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--upgrade", package_name, "--quiet"],
            )
            print(Fore.GREEN + f"VedAstro updated to {latest_version}. Please restart your script for changes to take effect." + Style.RESET_ALL)

    except Exception:
        return
