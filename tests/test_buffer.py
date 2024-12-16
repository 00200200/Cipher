from src.data.buffer import Buffer
from src.data.text import Text


def test_buffer_add() -> None:
    """
    Tests add() function of Buffer Class.
    Checking if Text object is added to buffer.
    :return: None
    """
    buffer = Buffer()
    text = Text("test", "rot13", "encrypted")
    buffer.add(text)
    assert buffer.get_all() == [text]


def test_buffer_clear() -> None:
    """
    Tests clear() function of Buffer class.
    Checking if buffor is correctly cleared.
    :return: None
    """
    buffer = Buffer()
    text = Text("test", "rot13", "encrypted")
    buffer.add(text)
    buffer.clear()
    assert buffer.get_all() == []
