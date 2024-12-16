from abc import abstractmethod, ABC


class Encryption(ABC):

    @abstractmethod
    def encrypt(self, text: str) -> str:

        pass

    @abstractmethod
    def decrypt(self, text: str) -> str:
        pass
