from abc import ABC


class Crypto(ABC):
    @staticmethod
    def encrypt(message, key): pass

    @staticmethod
    def decrypt(message, key): pass
