from src.menus.menu import Menu
from typing import Dict, Callable


class Manager:

    def __init__(self):
        self.menu = Menu()
        self.actions: Dict[str, Callable] = {
            "1": self.encrypt_text,
            "2": self.decrypt_text,
            "3": self.show_buffer,
            "4": self.load_from_file,
            "5": self.save_to_file,
        }

    def run(self):

        while True:
            self.menu.show_menu()
            choice = self.menu.get_choice()
            action = self.actions.get(choice)
            if action == "6":
                print("Exit aplication...")
                break
            action()
