from src.encoders.encryption import Encryption


class Rot13Encryption(Encryption):
    """
    Implements rot13 encryption and decryption
    """
    def encrypt(self, text: str) -> str:
        """
        Encrypt the given text using ROT13.
        :param text: Text to encrypt
        :return: Encrypted Text
        """
        encrypted_text = ""
        for char in text:
            if 'A' <= char <= 'Z':
                encrypted_text += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
            elif 'a' <= char <= 'z':
                encrypted_text += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text: str) -> str:
        """
        Decrypt the given Text.
        :param text: text to dectypt.
        :return: decrypted text.
        """
        return self.encrypt(text)
