#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n;
    cin >> n;
    vector<int> v;
    for(int i = 0; i < 6; i++) {
        int ip; cin >> ip;
        v.push_back(ip);
    }
    int t, p;
    cin >> t >> p;
    int shirts = 0;
    int pen = 0;
    for(int i = 0; i < 6; i++) {
        if(v[i] == 0) continue;
        if(v[i] <= t) shirts++;
        else {
            if(v[i] % t == 0) shirts += (v[i] / t);
            else shirts = shirts + (v[i] / t) + 1;
        }
    }
    cout << shirts << "\n";
    cout << n / p << " " << n % p << "\n";
    return 0;
}