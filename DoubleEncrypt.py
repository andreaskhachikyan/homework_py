import RLE, Caesar

message = input("Input message: ")
key = int(input("Input Caesar key: "))

encryptedCaesar = Caesar.Caesar.encrypt(message, key)
print(f'Caesar Encrypted Message: {encryptedCaesar}')
rleEncrypted = RLE.RLE.encrypt(encriptedCaesar)
print(f'RLE encrypted message: {rleEncrypted}')
decryptedMessage = Caesar.Caesar.decrypt(RLE.RLE.decrypt(rleEmcrypted), key)
print(f'Decrypted message: {decryptedMessage}')