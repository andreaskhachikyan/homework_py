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
    return encrypt(text, 26 - (shift % 26)); // Reverse shift for decryption
}

void encryptFile(const string& inputFile, const string& outputFile, int shift) {
    ifstream in(inputFile);
    ofstream out(outputFile);
    if (!in.is_open() || !out.is_open()) {
        cerr << "Error: Unable to open files." << endl;
        return;
    }

    string line;
    while (getline(in, line)) {
        out << encrypt(line, shift) << endl;
    }

    in.close();
    out.close();
    cout << "File encrypted successfully: " << outputFile << endl;
}

void decryptFile(const string& inputFile, const string& outputFile, int shift) {
    ifstream in(inputFile);
    ofstream out(outputFile);
    if (!in.is_open() || !out.is_open()) {
        cerr << "Error: Unable to open files." << endl;
        return;
    }

    string line;
    while (getline(in, line)) {
        out << decrypt(line, shift) << endl;
    }

    in.close();
    out.close();
    cout << "File decrypted successfully: " << outputFile << endl;
}

int main(int argc, char* argv[]) {
    if (argc < 5) {
        cerr << "Usage:\n";
        cerr << "  For text:    encrypt.exe text <mode> <shift> <input_text>\n";
        cerr << "  For files:   encrypt.exe file <mode> <shift> <input_file> <output_file>\n";
        cerr << "Mode: encrypt | decrypt\n";
        return 1;
    }

    string type = argv[1];
    string mode = argv[2];
    int shift = stoi(argv[3]);

    if (type == "text") {
        string input = argv[4];
        if (mode == "encrypt") {
            cout << "Encrypted Text: " << encrypt(input, shift) << endl;
        }
        else if (mode == "decrypt") {
            cout << "Decrypted Text: " << decrypt(input, shift) << endl;
        }
        else {
            cerr << "Invalid mode. Use 'encrypt' or 'decrypt'." << endl;
        }
    }
    else if (type == "file") {
        if (argc < 6) {
            cerr << "Error: Missing file arguments." << endl;
            return 1;
        }
        string inputFile = argv[4];
        string outputFile = argv[5];

        if (mode == "encrypt") {
            encryptFile(inputFile, outputFile, shift);
        }
        else if (mode == "decrypt") {
            decryptFile(inputFile, outputFile, shift);
        }
        else {
            cerr << "Invalid mode. Use 'encrypt' or 'decrypt'." << endl;
        }
    }
    else {
        cerr << "Invalid type. Use 'text' or 'file'." << endl;
    }

    return 0;
}
