""" Import necessary modules for the program to work """
import sys
import platform
import ctypes
import os
import time
import winreg
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMessageBox



""" Utility function to check if the system is Windows 10 """
def is_windows_11():
    version = platform.version()
    return version.startswith("10.0") and int(platform.release()) >= 10



""" Utility function to display a UI error popout """
def show_error(message):
    app = QApplication(sys.argv)
    msg_box = QMessageBox()
    msg_box.setIcon(QMessageBox.Critical)
    msg_box.setWindowTitle("Talon")
    msg_box.setText(message)
    msg_box.exec_()
    os._exit(1)



""" Check the system for if it is running Windows 10 or older """
def check_system():
    if not is_windows_11():
        show_error("You are currently on Windows 10 or older. Talon is designed to only work on freshly installed Windows 11 systems. Please update to a fresh installation of Windows 11 before attempting to use Talon again.")
    
    install_date = get_installation_date()
    if install_date is None:
        show_error("Could not determine Windows installation date. Please ensure your system is properly configured.")



""" Start the program """
if __name__ == "__main__":
    check_system()