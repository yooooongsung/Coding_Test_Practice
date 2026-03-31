#include <bits/stdc++.h>
using namespace std; 
int n, m;
unordered_map<string, int> smap;
unordered_map<int, string> imap;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 1; i <= n; i++) {
        string s; cin >> s;
        smap[s] = i;
        imap[i] = s;
    }
    for(int i = 0; i < m; i++) {
        string ss; cin >> ss;
        if(isdigit(ss[0])) {
            cout << imap[stoi(ss)] << "\n";
        }
        else {
            cout << smap[ss] << "\n";
        }
    }
    
    
    return 0;
}