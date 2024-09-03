import sys

from mainWindow import run_main_window

if __name__ == "__main__":
    try:
        run_main_window()
    except Exception as e:
        print(f"An error occurred while running main window: {e}")
        sys.exit(1)
