#include <bits/stdc++.h>
using namespace std;
int n, m;
int arr[150004];
int res;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        int ip;
        cin >> ip;
        arr[i] = ip;
    }

    for(int i = 0; i < n; i++) {
        for(int j = i + 1; j < n; j++) {
            if(arr[i] + arr[j] == m) res += 1;
        }
    }
    cout << res;    
    return 0;
}