#include <bits/stdc++.h>
using namespace std;
string s, res;
int arr[26];
int cnt = 0;
char midChar = 0;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> s;
    for(char c : s) arr[c-'A']++;

    for(int i = 0; i < 26; i++) {
        if(arr[i] % 2 == 1) {
            cnt++;
            midChar = i + 'A';
        }
    }

    if(cnt > 1) {
        cout << "I'm Sorry Hansoo";
        return 0;
    } 

    string leftHalf = "";
    for(int i = 0; i < 26; i++) {
        char c = i + 'A';
        for(int j = 0; j < arr[i] / 2; j++) {
            leftHalf += c;
        }
    }

    string rightHalf = leftHalf;
    reverse(rightHalf.begin(), rightHalf.end());

    if(cnt == 1) {
        res = leftHalf + midChar + rightHalf;
    }
    else res = leftHalf + rightHalf;

    cout << res;
    return 0;
}
