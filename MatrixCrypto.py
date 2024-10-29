from Crypto import Crypto


class MatrixCripto(Crypto):
    @staticmethod
    def encrypt(message, key):
        mat = []
        for i in range(0, len(message), key):
            mat.append(list(message[i:i + key]))
        result = ''
        for i in range(key):
            for j in range(len(mat)):
                try:
                    result += mat[j][i]
                except IndexError:
                    result += ' '
        return result

    @staticmethod
    def decrypt(message, key):
        mat = []
        col = len(message) // key
        for i in range(0, len(message), col):
            mat.append(list(message[i:i + col]))
        result = ''
        for i in range(col):
            for j in range(len(mat)):
                try:
                    result += mat[j][i]
                except IndexError:
                    result += ' '
        return result.strip()


testData = 'mmmdddjjjj'
print('Test data: ' + testData)
print()

print('Matrix Cripto:')
matEncrypted = MatrixCripto.encrypt(testData, 3)
print('Encrypted text: ', matEncrypted)
print('Decrypted text: ', MatrixCripto.decrypt(matEncrypted, 3))
