from rot13_encryption import Rot13Encryption
from rot47_encryption import Rot47Encryption
from encryption import Encryption


class EncryptionFactory:
    @staticmethod
    def get_encryption(rot_type: str) -> Encryption:
        if rot_type == "rot13":
            return Rot13Encryption()
        elif rot_type == "rot47":
            return Rot47Encryption()
        else:
            raise ValueError(f"Unsupported encryption type: {rot_type}")