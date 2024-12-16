#!/usr/bin/env python3

from managers.manager import Manager
from file_service.file_handler import FileHandler
from data.buffer import Buffer
from menus.main_menu import MainMenu


def main():
    """Entry point of application
        Initialize main class and start main loop
    """
    manager = Manager(file_handler=FileHandler(), buffer=Buffer(), menu=Menu())
    manager.run()


if __name__ == "__main__":
    main()
