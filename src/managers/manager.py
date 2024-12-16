from typing import Callable
from src.menus.main_menu import MainMenu
from src.file_service.file_handler import FileHandler
from src.data.buffer import Buffer
from src.data.text import Text
from src.encoders.factory import EncryptionFactory


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
         method terminating the main loop of program.
        """
        self.running = False

    def show_buffer(self):
        """
        Displays content in buffer
        :return:None
        """
        for text in self.buffer.get_all():
            print(f"Text: {text}")

    def load_from_file(self) -> None:
        """
        Loads a list of Text objects from specified file
        :return: None
        """
        filename = input("Type path to file: ")
        try:
            data = self.file_handler.load(filename)
            for text in data:
                self.buffer.add(text)
        except Exception as e:
            print(e)

    def save_to_file(self):
        """
        Save buffer to selected file
        :return: None
        """
        filename = input("Enter the filename: ")
        self.file_handler.save(filename, self.buffer.get_all())

    def encrypt_text(self) -> None:
        """
        Encrypts the user provided text using the chosen strategy
        :return:None
        """
        text = input("Enter text to encrypt: ")
        rot_type = input("Choose encryption type (rot13,rot47): ").lower()
        try:
            encryption = EncryptionFactory.get_encryption(rot_type)
            encrypted_text = encryption.encrypt(text)
            self.buffer.add(Text(encrypted_text, rot_type, "encrypted"))
        except Exception as e:
            print(f"Error : {e}")

    def decrypt_text(self):
        """
        Decrypts the user provided text using the chosen strategy
        :return:None
        """
        text = input("Enter text to decrypt: ")
        rot_type = input("Choose decryption type (rot13,rot47): ").lower()
        try:
            encryption = EncryptionFactory.get_encryption(rot_type)
            encrypted_text = encryption.decrypt(text)
            self.buffer.add(Text(encrypted_text, rot_type, "decrypter"))
        except Exception as e:
            print(f"Error : {e}")
