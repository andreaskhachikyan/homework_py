class Crypto:
  @staticmethod
  def encrypt(text, key):
    pass

  @staticmethod
  def decrypt(text, key):
    pass

class Huffman(Crypto):
  @staticmethod
  def encrypt(text, key = None):
    list = []
    for c in set(text):
      list.append([c, text.count(c)])
    list.sort(key = lambda x: x[1], reverse = True)
    while len(list) != 1:
      list[-2] = [[list[-2], list[-1]], list[-2][1] + list[-1][1]]
      list.pop()
      list.sort(key = lambda x: x[1], reverse = True)

    codedTuple = Huffman.getKey(list, '')
    schifer = []
    Huffman.getSchifer(codedTuple, schifer)
    print(schifer)

  @staticmethod
  def getKey(t, start):
    print(isinstance(t[0], str))
    if isinstance(t[0], str):
      t[1] = start
    else:
      Huffman.getKey(t[0], start + '0')
      Huffman.getKey(t[1], start + '1')

  @staticmethod
  def getSchifer(t, list):
    if isinstance(t[0], str):
      list.append(t)
    else:
      Huffman.getSchifer(t[0], list)
      Huffman.getSchifer(t[1], list)

  @staticmethod
  def decrypt(text, key):
    pass


text = 'beep boop beer!'
Huffman.encrypt(text)
