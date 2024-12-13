from src.menus.menu import Menu
from typing import Dict, Callable


class Manager:
    """ Manages the main logic of the application acting as the fascade
    """

    def __init__(self):
        """Initializes class with required methods."""
        self.menu = Menu()
        self.actions: Dict[str, Callable] = {
            "1": self.encrypt_text,
            "2": self.decrypt_text,
            "3": self.show_buffer,
            "4": self.load_from_file,
            "5": self.save_to_file,
        }

    def run(self):
        """
        Main loop of the program.
        Handles user input and selcted actions.
        """
        while True:
            self.menu.show_menu()
            choice = self.menu.get_choice()
            action = self.actions.get(choice)
            if action == "6":
                print("Exit aplication...")
                break
            action()
