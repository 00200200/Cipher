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
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
            return [Text(item["text"], item["rot_type"], item["status"]) for item in data]
