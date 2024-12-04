import Huffman
import BaseReplacement
import Caesar
import RLE
import MatrixCrypto


while True:
    print()
    print("Choose an option: ")
    print("1. Huffman")
    print("2. Base Replacement")
    print("3. Caesar")
    print("4. RLE")
    print("5. Matrix")
    print("6. Tigran")
    print("7. Exit")
    choice = input('Input your choice: ')
    print()
    if choice == '1':
        Huffman.use_huffman()
    elif choice == '2':
        BaseReplacement.use_cipher_alphabet()
    elif choice == '3':
        Caesar.use_caesar()
    elif choice == '4':
        RLE.use_rle()
    elif choice == '5':
        MatrixCrypto.use_matrix()
    elif choice == '6':
        Caesar.use_tigran()
    elif choice == '7':
        print('Program stoped')
        break
    else:
        print('Invalid choice')
      
