from abc import abstractmethod, ABC


class Encryption(ABC):
    @abstractmethod
    def encrypt(self):
        pass

    @abstractmethod
    def decrypt(self):
        pass
