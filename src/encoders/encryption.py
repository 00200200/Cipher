from abc import abstractmethod, ABC


class Encryption(ABC):
    """
    Base abstract class for encryption strategies
    """

    @abstractmethod
    def encrypt(self, text: str) -> str:
        """
        Encrypt the given text.
        :param text: Text to encrypt
        :return: Encrypted text
        """
        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        """
        Decrypt the given text.
        :param text:  Text to decrypt.
        :return: Decrypted text.
        """
        pass
