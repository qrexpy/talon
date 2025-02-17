import sys
import platform
import ctypes
import os
from PyQt5.QtWidgets import QApplication, QMessageBox

def is_windows_11():
    version = platform.version()
    return version.startswith("10.0") and int(platform.release()) >= 10

def get_system_uptime():
    try:
        return ctypes.windll.kernel32.GetTickCount64() // 1000
    except AttributeError:
        return ctypes.windll.kernel32.GetTickCount() // 1000

def show_error(message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Talon")
    msg_box.setText(message)
    msg_box.exec_()
    os._exit(1)

def check_system():
    if not is_windows_11():
        show_error("You are currently on Windows 10 or older. Talon is designed to only work on freshly installed Windows 11 systems. Please update to a fresh installation of Windows 11 before attempting to use Talon again.")
    uptime_days = get_system_uptime() / 86400
    if uptime_days < 1:
        show_error("Your system is already in-use. Talon is designed to only work on freshly installed Windows 11 systems. Please ensure you are on a fresh installation of Windows 11 before attempting to use Talon again.")

if __name__ == "__main__":
    check_system()
