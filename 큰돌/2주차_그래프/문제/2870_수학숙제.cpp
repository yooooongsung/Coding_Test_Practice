#include <bits/stdc++.h>
using namespace std;
int n;
string s;
vector<string> res;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;

    for(int i = 0; i < n; i++) {
        string temp = "";
        cin >> s;

        for(int j = 0; j < s.size(); j++) {
            if(isdigit(s[j])) {
                temp += s[j];
                if(j == s.size() - 1) {
                    while(temp.size() > 1 && temp[0] == '0') temp.erase(0,1);
                    res.push_back(temp);
                    break;
                }
            }
            else {
                if(temp.size() >= 1) {
                    while(temp.size() > 1 && temp[0] == '0') temp.erase(0,1);
                    res.push_back(temp);
                    temp = "";
                }
            }

        }
    }
    sort(res.begin(), res.end(), [](string a, string b) {
        if(a.size() == b.size()) return a < b;
        return a.size() < b.size();
    });
    for(string k : res) cout << k << "\n";
    
    return 0;
}