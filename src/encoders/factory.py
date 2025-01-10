from src.encoders.rot13_encryption import Rot13Encryption
from src.encoders.rot47_encryption import Rot47Encryption
from src.encoders.encryption import Encryption


class EncryptionFactory:
    """
    Factory class to create encryption objects.
    """

    @staticmethod
    def get_encryption(rot_type: str) -> Encryption:
        """
        Returns the encryption class based on rot_type
        :param rot_type: Type of encryption ('rot13', 'rot47')
        :return:  Instance of and encryption class.
        """
        if rot_type == "rot13":
            return Rot13Encryption()
        elif rot_type == "rot47":
            return Rot47Encryption()
        raise ValueError(f"Unsupported encryption type: {rot_type}")
