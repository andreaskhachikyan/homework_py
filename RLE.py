from Crypto import Crypto


class RLE(Crypto):
    @staticmethod
    def encrypt(message, key=None):
        result = []
        count = 1
        for i in range(len(message) - 1):
            if message[i] == message[i + 1]:
                count += 1
            else:
                result.append(str(count) + message[i])
                count = 1
        result.append(str(count) + message[-1])
        return ' '.join(result)

    @staticmethod
    def decrypt(message, key = None):
        result = []
        for part in message.split():
            count = int(part[0])
            result.append(part[1] * count)
        return ''.join(result)


class MatrixCripto:
  def encript(self, data, colCount):
    mat = []
    for i in range(0, len(data), colCount):
      mat.append(list(data[i:(i + colCount)]))
    result = ''
    for i in range(colCount):
      for j in range(len(mat)):
        try:
          result += mat[j][i]
        except(IndexError):
          result += ' '
    return result

  def decript(self, data, colCount):
    mat = []
    col = len(data) // colCount
    for i in range(0, len(data), col):
      mat.append(list(data[i:(i + col)]))
    result = ''
    for i in range(colCount):
      for j in range(len(mat)):
        try:
          result += mat[j][i]
        except(IndexError):
          result += ' '
    return result


testData = 'mmmdddjjjj'
print('Test data: ' + testData)
print()

#
# print('Matrix Cripto:')
# mat = MatrixCripto()
# matEncripted = mat.encript(testData, 3)
# print('Encripted mat method: ', matEncripted)
# print('Decripted mat method: ', mat.decript(matEncripted, 3))
#

print()
print('RLE Cripto:')
encriptedData = RLE.encrypt(testData)
print('Edcripted data: ', encriptedData)
print('Decripted data: ', RLE.decrypt(encriptedData))
