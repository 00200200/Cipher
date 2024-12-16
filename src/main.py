#!/usr/bin/env python3
from managers.manager import Manager
from file_service.file_handler import FileHandler
from data.buffer import Buffer
from menus.main_menu import MainMenu


def main():
    """Entry point of application
        Initialize main class and start main loop
    """
    manager = Manager(file_handler=FileHandler(), buffer=Buffer(), menu=MainMenu())
    manager.run()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error : {e}")
    except KeyboardInterrupt as e:
        print(f"\nProgram interrupted by user.")
        print("Exiting...")
