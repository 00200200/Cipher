from typing import Callable
from src.menus.main_menu import MainMenu
from src.file_service.file_handler import FileHandler
from src.data.buffer import Buffer


class Manager:
    """
    Manages the main logic of the application acting as the fascade
    """

    def __init__(self, menu: MainMenu, buffer: Buffer, file_handler: FileHandler):
        """
        Initializes class with required methods.

        """
        self.menu = menu
        self.buffer = buffer
        self.file_handler = file_handler
        self.actions: dict[int, Callable] = {
            1: self.encrypt_text,
            2: self.decrypt_text,
            3: self.show_buffer,
            4: self.load_from_file,
            5: self.save_to_file,
            6: self._exit,
        }
        self.running = True

    def run(self):
        """
        Main loop of the program.
        Handles user input and selcted actions.
        """
        while self.running:
            self.menu.show_menu()
            choice = self.menu.get_choice()
            action = self.actions.get(choice)
            if action:
                action()

    def _exit(self) -> None:
        """

        """
        self.running = False
    def show_buffer(self):
        """
        Displays content in buffer
        :return:None
        """
        for text in self.buffer.get_all():
            print(f"Text: {text}")

    def save_to_file(self):
        """
        Save buffer to selected file
        :return: None
        """
        filename = input("Enter the filename: ")
        self.file_handler.save(filename,self.buffer.get_all())
