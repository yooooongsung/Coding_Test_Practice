#include <bits/stdc++.h>
using namespace std;
string s;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    while(getline(cin,s)) {
        vector<char> v;
        if(s == ".") return 0;
        for(char c : s) {
            // if(c == ' ' || c == '.' || isalpha(c)) continue;
            if(c == '(' || c == ')' || c == '[' || c == ']') {
                if(v.size() >= 1) {
                    if(v.back() == '(' && c == ')') {
                        v.pop_back();
                        continue;
                    }
                    else if(v.back() == '[' && c == ']') {
                        v.pop_back();
                        continue;
                    }
                    v.push_back(c);
                }
                else v.push_back(c);
            }
        }
        if(v.size() >= 1) cout << "no" << "\n";
        else cout << "yes" << "\n";
    }
    
    
    return 0;
}