#include <bits/stdc++.h>
using namespace std;
int t, n;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> n;
        int res2 = 0, res5 = 0;
        for(int j = 2; j <= n; j *= 2) {
            res2 += (n / j);
        }
        for(int j = 5; j <= n; j *= 5) {
            res5 += (n / j);
        }
        cout << min(res2, res5) << "\n";
    }
}