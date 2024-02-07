import subprocess
import pyautogui

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


def take_screenshot(window, system_platform):
    window.update()
    x = window.winfo_rootx() + window.winfo_x()
    y = window.winfo_rooty() + window.winfo_y()
    width = x + window.winfo_width()
    height = y + window.winfo_height()

    check_required_packages()
    if system_platform == 'Windows':
        screenshot = pyautogui.screenshot(region=(x, y, width, height))
        screenshot.save("seating_chart.png")
    elif system_platform == 'Darwin':  # macOS
        subprocess.run(["screencapture", "-R", f"{x},{y},{width},{height}", "seating_chart.png"])
    elif system_platform == 'Linux':
        subprocess.run(["scrot", "-u", "-o", "seating_chart.png", "-s"])
    else:
        print("Unsupported operating system for downloads")