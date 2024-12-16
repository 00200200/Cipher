from encryption import Encryption


class Rot47Encryption(Encryption):
    def encrypt(self, text: str) -> str:
        encrypted_text = ""
        for char in text:
            if 33 <= ord(char) <= 126:
                encrypted_text += chr(33 + ((ord(char) - 33 + 47) % 94))
            else:
                encrypted_text += char
        return encrypted_text

