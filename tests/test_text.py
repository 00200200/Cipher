from src.data.text import Text


def test_text() -> None:
    """
    Tests the initialization of Text dataclass
    Ensures that attributes are correctly assigned.
    :return:None
    """
    text = Text("hello", "rot13", "encrypted")
    assert text.text == "hello"
    assert text.rot_type == "rot13"
    assert text.status == "encrypted"
