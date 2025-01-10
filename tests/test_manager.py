from unittest.mock import Mock
from src.managers.manager import Manager
from src.data.buffer import Buffer
from src.menus.main_menu import MainMenu
from src.file_service.file_handler import FileHandler
import pytest
from src.data.text import Text
from unittest.mock import patch


@pytest.fixture
def manager() -> Manager:
    """
    Fixture that creates an instance of manager
    """
    return Manager(menu=MainMenu(), buffer=Buffer(), file_handler=FileHandler())


def test_clear_buffer() -> None:
    """
    Test the clear_buffer method to ensure it clears all data.
    """
    mock_buffer = Mock()
    manager = Manager(menu=Mock(), buffer=mock_buffer, file_handler=Mock())
    # manager.buffer.add(Text("exmaple", "rot13", "encrypted"))
    # assert len(manager.buffer.get_all()) == 1
    manager.clear_buffer()
    # assert len(manager.buffer.get_all()) == 0

    assert mock_buffer.clear.call_count == 1


def test_exit(manager) -> None:
    """
    Test the _exit method to ensure is stops the main loop.
    """
    manager.running = True
    manager._exit()
    assert manager.running is False


def test_encrypt_text(manager) -> None:
    """
    Test the encrypt_text method to ensure encrypted text is added to Buffer list.
    """
    with patch("builtins.input", side_effect=["hello", "rot13"]):
        manager.encrypt_text()
        buffer_data = manager.buffer.get_all()
        assert len(buffer_data) == 1
        assert buffer_data[0] == Text("uryyb", "rot13", "encrypted")


def test_decrypt_text(manager) -> None:
    """
    Test the decrypt_text method to ensure encrypted text is removed from Buffer list.
    """
    with patch("builtins.input", side_effect=["uryyb", "rot13"]):
        manager.decrypt_text()
        buffer_data = manager.buffer.get_all()
        assert len(buffer_data) == 1
        assert buffer_data[0] == Text("hello", "rot13", "decrypted")


def test_save_and_load_from_file(manager):
    """
    save / load methods to verify data is correctly saved and loaded.
    """

    manager.buffer.add(Text("hello", "rot13", "encrypted"))

    with patch("builtins.input", side_effect="test.json"):
        manager.save_to_file()

    manager.clear_buffer()

    with patch("builtins.input", side_effect="test.json"):
        manager.load_from_file()

    assert len(manager.buffer.get_all()) == 1
    buffer_data = manager.buffer.get_all()
    assert buffer_data == [Text("hello", "rot13", "encrypted")]
