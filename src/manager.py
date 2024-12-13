from typing import Callable
from src.menus.menu import Menu
from src.file_service.file_handler import FileHandler
from src.data.buffer import Buffer

class Manager:
    """
    Manages the main logic of the application acting as the fascade
    """

    def __init__(self):
        """
        Initializes class with required methods.

        """
        self.menu = Menu()
        self.buffer = Buffer()
        self.file_handler = FileHandler()
        self.actions: dict[str, Callable] = {
            # "1": self.encrypt_text,
            # "2": self.decrypt_text,
            "3": self.show_buffer,
            "4": self.load_from_file,
            # "5": self.save_to_file,
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
            if choice == "6":
                break
            if action:
                action()

    def show_buffer(self):
        for text in self.buffer.get_all():
            print(f"Text: {text}")

    def load_from_file(self):
