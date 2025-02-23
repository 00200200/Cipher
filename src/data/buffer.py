from src.data.text import Text


class Buffer:
    """
    Stores and manage data during program execution.
    """

    def __init__(self) -> None:
        """
        Initialize buffer with list of Text objects.
        """
        self.data: list[Text] = []

    def add(self, text: Text) -> None:
        """
        Adds a new Text object to buffer list
        :param text: Text object to add
        :return: None
        """
        self.data.append(text)

    def get_all(self) -> list[Text]:
        """
        Returns list of text objects in a buffer list.
        :return: list of Text objects
        """
        return self.data

    def clear(self) -> None:
        """
        Clears the buffer.
        :return: None
        """
        self.data.clear()
