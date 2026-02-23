#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v;
    int ip;
    int sum = 0;
    for(int i = 0; i < 9; i++) {
        cin >> ip;
        v.push_back(ip);
        sum += ip;
    }
    sort(v.begin(), v.end());

    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < i; j++) {
            if(sum - v[i] - v[j] == 100) {
                for(int k = 0; k < 9; k ++) {
                    if(k == i || k == j) continue;
                    cout << v[k] <<  endl;
                }
                return 0;
            }
        }
    }
}