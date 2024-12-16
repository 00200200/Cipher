from encryption import Encryption


class Rot47Encryption(Encryption):
    """
    Implements rot47 encryption and decryption
    """
    def encrypt(self, text: str) -> str:
        """
        Encrypt the given text using ROT47.
        :param text: Text to encrypt
        :return: Encrypted Text
        """
        encrypted_text = ""
        for char in text:
            if 33 <= ord(char) <= 126:
                encrypted_text += chr(33 + ((ord(char) - 33 + 47) % 94))
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
    