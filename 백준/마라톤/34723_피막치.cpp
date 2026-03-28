#include <bits/stdc++.h>
using namespace std; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int p, m, c; cin >> p >> m >> c;
    int x; cin >> x;
    int _min = 1999999999;
    for(int i = 1; i <= p; i++) {
        for(int j = 1; j <= m; j++) {
            for(int k = 1; k <= c; k++) {
                int temp = abs((i + j) * (j + k) - x);
                _min = min(_min, temp);
            }
        }
    }
    cout << _min;
    
    return 0;
}