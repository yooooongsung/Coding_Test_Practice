#include <bits/stdc++.h>
using namespace std;

int main() {
    string ip;
    cin >> ip;
    int alphabet[26] = {0,};

    for(char c : ip) {
        int temp = c-'a';
        alphabet[temp] += 1;
        // ASCII 
        // 65 - A, 90 - Z
        // 97 - a, 122 - z
    }

    for(int i = 0; i < 26; i++) cout << alphabet[i] << ' ';

    return 0;
}