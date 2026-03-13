#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n, m; cin >> n >> m;
    int k = n + m;
    map<string, int> dic;
    for(int i = 0; i < k; i++) {
        string s; cin >> s;
        dic[s]++;
    }
    int res = 0;
    for(auto & it : dic) {
        if(it.second >= 2) {
            res++;
        }
    }
    cout << res << "\n";
    for(auto & it : dic) {
        if(it.second >= 2) {
            cout << it.first << "\n";
        }
    }
    
    return 0;
}