from colorama import Fore, Style
from packaging import version
import requests


def check_for_update(package_name):
    try:
        from importlib.metadata import version as get_version
        installed_version = get_version(package_name)

        response = requests.get(f'https://pypi.org/pypi/{package_name}/json', timeout=5)
        latest_version = response.json()['info']['version']

        if version.parse(installed_version) < version.parse(latest_version):
            print(Fore.YELLOW + f"VedAstro Package Outdated! {installed_version} --> {latest_version}" + Style.RESET_ALL)
            print(Fore.YELLOW + f"Run: pip install --upgrade {package_name}" + Style.RESET_ALL)

    except Exception:
        return
