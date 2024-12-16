from src.file_service.file_handler import FileHandler
from src.data.text import Text


def test_file_handler_save_and_load():
    data = [Text("Test", "rot13", "encrypted")]
    FileHandler.save("test.json",data)

    loaded_data = FileHandler.load("test.json")
    assert loaded_data == data


def test_file_handler_load_not_existing():
    assert FileHandler.load("not_existing.json") == []