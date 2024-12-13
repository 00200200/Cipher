from src.data.text import Text


class Buffer:
    def __init__(self):
        self.data: list[Text] = []

    def add(self, text: Text):
        self.data.append(text)

    def get_all(self):
        return self.data

