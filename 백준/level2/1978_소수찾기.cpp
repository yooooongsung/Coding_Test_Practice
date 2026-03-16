#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n; cin >> n;
    int ans = 0;
    for(int i = 0; i < n; i++) {
        int ip; cin >> ip;
        int res = 0;
        for(int j = 1; j <= ip; j++) {
            if(ip % j == 0) res++;
        }
        if(res == 2) ans++;
    }
    cout << ans;
    
    
    return 0;
}