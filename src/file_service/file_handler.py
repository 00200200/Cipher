import json
from src.data.text import Text
from typing import List


class FileHandler:

    @staticmethod
    def load(filename: str) -> List[Text]:
        with open(filename, "r", encoding='utf-8') as file:
            data = json.load(file)
            return [Text(item["text"], item["rot_type"], item["status"]) for item in data]
