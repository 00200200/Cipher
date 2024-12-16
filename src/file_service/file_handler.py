import json
from src.data.text import Text
from typing import List


class FileHandler:
    """
    Handles file operations saving/loading Text Objects.
    """
    @staticmethod
    def load(filename: str) -> List[Text]:
        """
        Load a list of Text objects from JSON file.
        :param filename: path to JSON file.
        :return: A list of Text objects
        """
        try:
            with open(filename, "r", encoding='utf-8') as file:
                data = json.load(file)
                return [Text(item["text"], item["rot_type"], item["status"]) for item in data]
        except FileNotFoundError as e:
            print(f"Error File {filename} not found ")
        except Exception as e:
            print(f"Error {e}")

    @staticmethod
    def save(filename: str, data: List[Text]) -> None:
        """
        Save a List of Text objects to specified file.
        :param filename: path to JSON file.
        :param data: List of Text objects
        :return:  None
        """

        try:
    
            with open(filename, "w", encoding='utf-8') as file:
                json.dump([{"text": item.text, "rot_type": item.rot_type, "status": item.status} for item in data], file,
                          indent=2)
        except Exception as e:
            print(f"Unexpected error {e}")
