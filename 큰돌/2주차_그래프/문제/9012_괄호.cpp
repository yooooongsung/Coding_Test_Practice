#include <bits/stdc++.h>
using namespace std;
int t;
string s;
vector<char> v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> s;
        v.clear();
        for(char c : s) {
            if(v.size() >= 1) {
                if(v.back() == '(' && c == ')') {
                    v.pop_back();
                    continue;
                }
                v.push_back(c);
            }
            else {
                v.push_back(c);
            }
        }
        if(v.size()) cout << "NO" << "\n";
        else cout << "YES" << "\n";
            
    }
        
        
    return 0;
}