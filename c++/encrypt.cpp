#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string encrypt(const string& text, int shift) {
    string result = "";
    for (char c : text) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            result += (c - base + shift) % 26 + base;
        }
        else {
            result += c;
        }
    }
    return result;
}

string decrypt(const string& text, int shift) {
    return encrypt(text, 26 - (shift % 26));
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        cerr << "Usage: encrypt.exe <mode> <shift> <input>\n";
        cerr << "Mode: encrypt | decrypt\n";
        return 1;
    }

    string mode = argv[1];
    int shift = stoi(argv[2]);
    string input = argv[3];

    if (mode == "encrypt") {
        cout << "Encrypted Text: " << encrypt(input, shift) << endl;
    }
    else if (mode == "decrypt") {
        cout << "Decrypted Text: " << decrypt(input, shift) << endl;
    }
    else {
        cerr << "Invalid mode. Use 'encrypt' or 'decrypt'.\n";
        return 1;
    }

    return 0;
}
