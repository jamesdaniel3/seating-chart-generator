import subprocess
import pyautogui

def install_package(package):
    subprocess.check_call(["python", "-m", "pip", "install", package])


def check_required_packages():
    required_package = "pyautogui"
    try:
        import pyautogui
    except ImportError:
        print("Required package " + required_package + " is not installed. Installing it now...")
        install_package(required_package)
        import pyautogui


def take_screenshot(window, system_platform, file_path="seating_chart.png"):
    window.update()
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