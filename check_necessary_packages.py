import subprocess

def install_package(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])


def check_required_packages():
    required_package = "pyautogui"
    try:
        import pyautogui
    except ImportError:
        print(f"Required package '{required_package}' is not installed. Installing it now...")
        install_package(required_package)
        import pyautogui  # Now import again after installation
