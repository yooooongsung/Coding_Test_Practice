#include <bits/stdc++.h>
using namespace std;
int n, res;
long long m = 200000000;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 666; i < m; i++) {
        string s = to_string(i);
        auto along = s.find("666") != string::npos;
        if(along) res++;
        if(n == res) {
            cout << i;
            return 0;
        }
    }

    
    return 0;
}