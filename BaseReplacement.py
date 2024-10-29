import string, random, Crypto


class BaseReplacement(Crypto.Crypto):
    @staticmethod
    def generate_cipher_alphabet():
        alphabet = list(string.ascii_lowercase)
        shuffled_alphabet = alphabet[:]
        random.shuffle(shuffled_alphabet)
        return dict(zip(alphabet, shuffled_alphabet))

    @staticmethod
    def encrypt(text, cipher_alphabet):
        encrypted_text = ""
        for char in text:
            if char.islower():
                encrypted_text += cipher_alphabet.get(char, char)
            elif char.isupper():
                encrypted_text += cipher_alphabet.get(char.lower(), char).upper()
            else:
                encrypted_text += char
        return encrypted_text

    @staticmethod
    def decrypt(ciphertext, cipher_alphabet):
        reverse_cipher_alphabet = {v: k for k, v in cipher_alphabet.items()}
        decrypted_text = ""
        for char in ciphertext:
            if char.islower():
                decrypted_text += reverse_cipher_alphabet.get(char, char)
            elif char.isupper():
                decrypted_text += reverse_cipher_alphabet.get(char.lower(), char).upper()
            else:
                decrypted_text += char
        return decrypted_text


cipher_alphabet = BaseReplacement.generate_cipher_alphabet()

plaintext = "Andreas Khachikyan"
print(f"Original Text: {plaintext}")
print()

encrypted_text = BaseReplacement.encrypt(plaintext, cipher_alphabet)
print(f"Encrypted Text: {encrypted_text}")
print()

decrypted_text = BaseReplacement.decrypt(encrypted_text, cipher_alphabet)
print(f"Decrypted Text: {decrypted_text}")