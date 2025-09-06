import platform
from app.gui import SteganographyApp

if __name__ == "__main__":
    # This check is important for freezing the app with tools like PyInstaller
    if platform.system() == "Windows":
        try:
            from ctypes import windll

            windll.shcore.SetProcessDPIAwareness(1)
        except Exception as e:
            print(f"Warning: Could not set DPI awareness: {e}")

    app = SteganographyApp()
    app.mainloop()