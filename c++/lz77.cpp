#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

struct LZ77Token {
    int offset;
    int length;
    char nextChar;
};

void compressLZ77(const string& inputFile, const string& outputFile) {
    ifstream in(inputFile, ios::binary);
    ofstream out(outputFile, ios::binary);

    if (!in.is_open() || !out.is_open()) {
        cerr << "Error: Could not open files." << endl;
        return;
    }

    string buffer((istreambuf_iterator<char>(in)), istreambuf_iterator<char>());
    vector<LZ77Token> tokens;

    const int windowSize = 1024;
    int i = 0;

    while (i < buffer.size()) {
        int maxMatchLength = 0, bestOffset = 0;
        for (int j = max(0, i - windowSize); j < i; ++j) {
            int matchLength = 0;
            while (matchLength < windowSize && i + matchLength < buffer.size() && buffer[j + matchLength] == buffer[i + matchLength]) {
                ++matchLength;
            }

            if (matchLength > maxMatchLength) {
                maxMatchLength = matchLength;
                bestOffset = i - j;
            }
        }

        char nextChar = buffer[i + maxMatchLength];
        tokens.push_back({ bestOffset, maxMatchLength, nextChar });
        i += maxMatchLength + 1;
    }

    for (auto& token : tokens) {
        out.write(reinterpret_cast<char*>(&token), sizeof(token));
    }

    cout << "File compressed successfully: " << outputFile << endl;

    in.close();
    out.close();
}

void decompressLZ77(const string& inputFile, const string& outputFile) {
    ifstream in(inputFile, ios::binary);
    ofstream out(outputFile, ios::binary);

    if (!in.is_open() || !out.is_open()) {
        cerr << "Error: Could not open files." << endl;
        return;
    }

    vector<char> buffer;
    LZ77Token token;

    while (in.read(reinterpret_cast<char*>(&token), sizeof(token))) {
        int start = buffer.size() - token.offset;
        for (int i = 0; i < token.length; ++i) {
            buffer.push_back(buffer[start + i]);
        }
        buffer.push_back(token.nextChar);
    }

    for (char c : buffer) {
        out.put(c);
    }

    cout << "File decompressed successfully: " << outputFile << endl;

    in.close();
    out.close();
}

int main(int argc, char* argv[]) {
    if (argc < 4) {
        cerr << "Usage: lz77.exe <compress|decompress> <input_file> <output_file>" << endl;
        return 1;
    }

    string mode = argv[1];
    string inputFile = argv[2];
    string outputFile = argv[3];

    if (mode == "compress") {
        compressLZ77(inputFile, outputFile);
    }
    else if (mode == "decompress") {
        decompressLZ77(inputFile, outputFile);
    }
    else {
        cerr << "Invalid mode. Use 'compress' or 'decompress'." << endl;
        return 1;
    }

    return 0;
}
