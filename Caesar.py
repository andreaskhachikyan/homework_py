import Crypto


class Caesar(Crypto.Crypto):
    @staticmethod
    def encrypt(message, key):
        result = ""
        for ch in message:
            if ch.isupper():
                result += chr((ord(ch) + key - 65) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) + key - 97) % 26 + 97)
            else:
                result += ch
        return result

    @staticmethod
    def decrypt(message, key):
        return Caesar.encrypt(message, 26 - key)


class Tigran(Crypto.Crypto):
    alphabet = [
        'Ա', 'Բ', 'Գ', 'Դ', 'Ե', 'Զ', 'Է', 'Ը', 'Թ', 'Ժ', 'Ի', 'Լ', 'Խ', 'Ծ', 'Կ', 'Հ',
        'Ձ', 'Ղ', 'Ճ', 'Մ', 'Յ', 'Ն', 'Շ', 'Ո', 'Չ', 'Պ', 'Ջ', 'Ռ', 'Ս', 'Վ', 'Տ', 'Ր',
        'Ց', 'Ո', 'Ւ', 'Փ', 'Ք', 'և', 'Օ', 'Ֆ', 'ա', 'բ', 'գ', 'դ', 'ե', 'զ', 'է', 'ը', 'թ', 'ժ', 'ի', 'լ', 'խ', 'ծ', 'կ',
        'հ',
        'ձ', 'ղ', 'ճ', 'մ', 'յ', 'ն', 'շ', 'ո', 'չ', 'պ', 'ջ', 'ռ', 'ս', 'վ', 'տ', 'ր',
        'ց', 'ո', 'ւ', 'փ', 'ք', 'և', 'օ', 'ֆ']

    @staticmethod
    def encrypt(message, key):
        result = ""
        for ch in message:
            index = (Tigran.alphabet.index(ch) + key) % len(Tigran.alphabet)
            if index < 0:
                index += len(Tigran.alphabet)
            result += Tigran.alphabet[(Tigran.alphabet.index(ch) + key) % len(Tigran.alphabet)]
        return result

    @staticmethod
    def decrypt(message, key):
        return Tigran.encrypt(message, -key)


message = input("Enter the message: ")
shift = int(input("Enter the shift (1-25): "))

encrypted_message = Caesar.encrypt(message, shift)
print("Encoded message:", encrypted_message)

decrypted_message = Caesar.decrypt(encrypted_message, shift)
print("Decoded message:", decrypted_message)

message = input("Enter armenian the message: ")
shift = int(input("Enter the shift (1-25): "))

encrypted_message = Tigran.encrypt(message, shift)
print("Encoded message:", encrypted_message)

decrypted_message = Tigran.decrypt(encrypted_message, shift)
print("Decoded message:", decrypted_message)