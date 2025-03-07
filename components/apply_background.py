import os
import sys
import ctypes
import shutil

def set_wallpaper(image_path):
    try:
        result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
        if result:
            print("Wallpaper set successfully.")
        else:
            print("Failed to set wallpaper.")
    except Exception as e:
        print(f"Error setting wallpaper: {e}")

def main():
    if getattr(sys, 'frozen', False):
        resource_path = sys._MEIPASS
    else:
        resource_path = os.path.dirname(os.path.abspath(__file__))
    
    source_image_path = os.path.join(resource_path, "DesktopBackground.png")
    if not os.path.exists(source_image_path):
        print(f"Error: Source image not found at {source_image_path}")
        return
    
    pictures_dir = os.path.join(os.path.expanduser("~"), "Pictures")
    os.makedirs(pictures_dir, exist_ok=True)
    destination_image_path = os.path.join(pictures_dir, "DesktopBackground.png")
    
    try:
        shutil.copy2(source_image_path, destination_image_path)
        print(f"Image copied to {destination_image_path}")
    except Exception as e:
        print(f"Error copying file: {e}")
        return
    
    set_wallpaper(destination_image_path)

if __name__ == "__main__":
    main()