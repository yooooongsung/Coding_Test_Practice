#include <bits/stdc++.h>
using namespace std;

int main() {
    unordered_map<char,int> m;
    int n;
    cin >> n;
    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        m[s[0]]++;
        // if(m.find(s[0]) != m.end()) {
        //     m[s[0]]++;
        // }
        // else {
        //     m[s[0]] = 1;
        // }
    }
    string res = "";
    for(const auto& item : m) {
        // cout << item.first << " : " << item.second << endl;
        if(item.second >= 5) {
            res += item.first;
        }
    }
    sort(res.begin(), res.end());
    if(res == "") cout << "PREDAJA";
    else cout << res;
    return 0;
}