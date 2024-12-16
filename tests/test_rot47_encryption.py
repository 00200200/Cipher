from src.encoders.rot47_encryption import Rot47Encryption
import pytest

@pytest.mark.parametrize("input_text, output", [
    ("hello", "96==@"),
    ("HELLO", "wt{{~"),
    ("12345", "`abcd"),
    ("", ""),
    ("test example", "E6DE 6I2>A=6"),
    ("TEST EXAMPLE", "%t$% t)p|!{t"),
    ("Test Example", "%6DE tI2>A=6"),
])
def test_rot47_encrypt(input_text, output) -> None:
    """
    Tests the encryption() method of Rot47Encryption class
    Ensures that encryption workds correctly
    """
    rot47 = Rot47Encryption()
    assert rot47.encrypt(input_text) == output

@pytest.mark.parametrize("input_text, output", [
    ("96==@", "hello"),
    ("wt{{~", "HELLO"),
    ("`abcd", "12345"),
    ("", ""),
    ("E6DE 6I2>A=6", "test example"),
    ("%t$% t)p|!{t", "TEST EXAMPLE"),
    ("%6DE tI2>A=6", "Test Example"),
])
def test_rot47_decrypt(input_text, output):
    """
    Tests the decrypt() method of Rot47Encryption class
    Ensures that decryption workds correctly
    """
    rot47 = Rot47Encryption()
    assert rot47.decrypt(input_text) == output
