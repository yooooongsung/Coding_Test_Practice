#include <bits/stdc++.h>
using namespace std;

int main() {

    int ip;
    vector<int> v;
    int ans = 0;
    while(ans < 100) {
        cin >> ip;
        if((ans + ip) > 100) {
            continue;
        }
        ans += ip;
        v.push_back(ip);
    }
    sort(v.begin(), v.end());

    cout << endl;
    for(int i = 0; i < 7; i++) {
        cout << v[i] << endl;
    }
    return 0;
}