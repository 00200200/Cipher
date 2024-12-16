from src.data.buffer import Buffer
from src.data.text import Text


def test_buffer_add():
    buffer = Buffer()
    text = Text("test", "rot13", "encrypted")
    buffer.add(text)
    assert buffer.get_all() == [text]


def test_buffer_clear():
    buffer = Buffer()
    text = Text("test", "rot13", "encrypted")
    buffer.add(text)
    buffer.clear()
    assert buffer.get_all() == []
