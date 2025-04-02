import subprocess
from git_author_rewrite.message_handler import display_messages
from git_author_rewrite.enums import Status
from pyinputplus import inputChoice

PACKAGES = ['git-filter-repo']

def install_package(package_name: str):
    result = None
    try:
        result = subprocess.run(
            [ 'pip', 'install', package_name],
            check=True,
            text=True,
            capture_output=True,
        )
        display_messages(
            'Installation successful',
            f'{result.stdout}')
    except subprocess.CalledProcessError as e:
        display_messages(
            'Installation failed',
            f'{result.stderr}')


def is_package_installed(package_name: str):
    result = subprocess.run(['pip', 'show', package_name], check=True, text=True, capture_output=True)
    return result.returncode == 0


def ensure_pip_packages():
    for package_name in PACKAGES:
        if not is_package_installed(package_name):
            response = inputChoice(['y', 'n'], prompt=f'{package_name} is not installed. Install it? (Y/n) ')
            if response != 'y':
                display_messages(f'{package_name} is required. Please install it to proceed.', status=Status.ERROR)
            install_package(package_name)  # Install package
