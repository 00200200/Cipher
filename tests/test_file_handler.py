from src.file_service.file_handler import FileHandler
from src.data.text import Text


def test_file_handler_save_and_load() -> None:
    """
    Tests save() and load() methods
    Ensures that data is correctly savend and loaded.
    :return: None
    """
    data = [Text("Test", "rot13", "encrypted")]
    FileHandler.save("test.json", data)

    loaded_data = FileHandler.load("test.json")
    assert loaded_data == data


def test_file_handler_load_not_existing() -> None:
    """
    Tests load() method for not existed file
    Ensures it returns an empty list.
    :return:
    """
    assert FileHandler.load("not_existing.json") == []
