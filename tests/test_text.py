from src.data.text import Text


def test_text():
    text = Text("hello", "rot13", "encrypted")
    assert text.text == "hello"
    assert text.rot_type == "rot13"
    assert text.status == "encrypted"
