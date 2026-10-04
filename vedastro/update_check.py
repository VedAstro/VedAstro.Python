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
            print(f"VedAstro Update Available: {installed_version} --> {latest_version}")
            print("Auto-updating...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "--upgrade", package_name, "--quiet"],
            )
            print(f"VedAstro updated to {latest_version}. Please restart your script for changes to take effect.")

    except Exception:
        return
