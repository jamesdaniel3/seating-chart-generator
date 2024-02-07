import subprocess
import pyautogui

def install_package(package):
    """
    This function installs a package on the users computer.

    :param package: the name of the package to install
    """
    subprocess.check_call(["python", "-m", "pip", "install", package])


def check_required_packages():
    """
    This function checks that the user has the necessary packages installed on their computer and installs them if they
    are not present.
    """
    required_package = "pyautogui"
    try:
        import pyautogui
    except ImportError:
        print("Required package " + required_package + " is not installed. Installing it now...")
        install_package(required_package)
        import pyautogui


def take_screenshot(window, system_platform, file_path="seating_chart.png"):
    """
    This function takes a screenshot of the image generated by the code and saves it. The goal for the future is to allow
    users to specify a file path but that is not currently in place.

    :param window: the window object where the image is generated
    :param system_platform: the system that the user's computer is running on
    :param file_path: the location where the user would like to save the image
    """
    window.update()
    window.geometry(str(window.winfo_width()) + "x" + str(window.winfo_height()) + "+0+0")
    x = window.winfo_rootx()
    y = window.winfo_rooty()
    width = window.winfo_width()
    height = window.winfo_height()

    check_required_packages()
    if system_platform == 'Windows':
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save(file_path)
    elif system_platform == 'Darwin':  # macOS
        subprocess.run(["screencapture", "-R", f"{x},{y},{width},{height}", file_path])
    elif system_platform == 'Linux':
        subprocess.run(["scrot", "-u", "-o", file_path, "-s"])
    else:
        print("Unsupported operating system for downloads")