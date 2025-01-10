from src.encoders.factory import EncryptionFactory
from src.encoders.rot13_encryption import Rot13Encryption
from src.encoders.rot47_encryption import Rot47Encryption
import pytest


class TestEncryptionFactory:
    def test_get_rot13_encryption(self) -> None:
        """
        Test get_encryption method
        Checking if type "ROT13" is instance of  Rot13Encryption class
        """
        encryption = EncryptionFactory.get_encryption("rot13")
        assert isinstance(encryption, Rot13Encryption)

    def test_get_rot47_encryption(self) -> None:
        """
        Test get_encryption method
        Checking if type "Rot47" is instance of  Rot47Encryption class
        """
        encryption = EncryptionFactory.get_encryption("rot47")
        assert isinstance(encryption, Rot47Encryption)

    def test_get_invalid_encryption(self) -> None:
        """
        Test get_encryption method
        Checking if invalind type raises exceipton ValueError
        """
        with pytest.raises(ValueError):
            EncryptionFactory.get_encryption("Wrong type")
