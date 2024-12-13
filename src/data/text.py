from dataclasses import dataclass


@dataclass
class Text:
    """
    Represents a text object

    text: content
    rot_type: type of encryption (rot13 , rot47)
    status: status : (encyrpted,decrypted)
    """
    text: str
    rot_type: str
    status: str
