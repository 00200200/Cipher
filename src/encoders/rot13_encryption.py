from encryption import Encryption


class Rot13Encryption(Encryption):
    def encrypt(self, text: str) -> str:
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
        return self.encrypt(text)
