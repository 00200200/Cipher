from src.data.buffer import Buffer
from src.data.text import Text


def test_buffer_add() -> None:
    """
    Test add() function of Buffer Class.
    Checking if Text object is added to buffer.
    :return: None
    """
    buffer = Buffer()
    text = Text("test", "rot13", "encrypted")
    buffer.add(text)
    assert buffer.data == [text]


def test_buffer_clear() -> None:
    """
    Test clear() function of Buffer class.
    Checking if buffor is correctly cleared.
    """
    buffer = Buffer()
    buffer.data = [Text("test", "rot13", "encrypted")]
    buffer.clear()
    assert buffer.data == []
