from src.encoders.rot13_encryption import Rot13Encryption
import pytest


@pytest.mark.parametrize("input_text, output", [
    ("hello", "uryyb"), ("HELLO", "URYYB"), ("12345", "12345"), ("''", "''"),
    ("test example", "grfg rknzcyr"), ("TEST EXAMPLE", "GRFG RKNZCYR"), ("Test Example", "Grfg Rknzcyr"),
])
def test_rot13_encrypt(input_text, output) -> None:
    """
    Tests the encryption() method of Rot13Encryption class
    Ensures that encryption workds correctly
    """
    rot13 = Rot13Encryption()
    assert rot13.encrypt(input_text) == output


@pytest.mark.parametrize("input_text, output", [
    ("uryyb", "hello"), ("URYYB", "HELLO"), ("12345", "12345"), ("''", "''"),
    ("grfg rknzcyr", "test example"), ("GRFG RKNZCYR", "TEST EXAMPLE"), ("Grfg Rknzcyr", "Test Example"),
])
def test_rot13_decrypt(input_text, output):
    """
    Tests the decrypt() method of Rot13Encryption class
    Ensures that decryption workds correctly
    """
    rot13 = Rot13Encryption()
    assert rot13.decrypt(input_text) == output
