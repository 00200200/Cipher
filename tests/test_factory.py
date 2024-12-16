from src.encoders.factory import EncryptionFactory
from src.encoders.rot13_encryption import Rot13Encryption
from src.encoders.rot47_encryption import Rot47Encryption
import pytest


def test_get_rot13_encryption():
    encryption = EncryptionFactory.get_encryption("rot13")
    assert isinstance(encryption,Rot13Encryption)


def test_get_rot47_encryption():
    encryption = EncryptionFactory.get_encryption("rot47")
    assert isinstance(encryption,Rot47Encryption)


def test_get_invalid_encryption():
    with pytest.raises(ValueError):
        EncryptionFactory.get_encryption("Wrong type")