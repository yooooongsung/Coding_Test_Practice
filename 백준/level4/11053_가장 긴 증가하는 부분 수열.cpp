#include <bits/stdc++.h>
using namespace std; 
int n;
vector<int> v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    int res[n];
    for(int i = 0; i < n; i++) {
        int ip; cin >> ip;
        v.push_back(ip);
    }
    for(int i = 0; i < n; i++) {
        res[i] = 1;
        for(int j = 0; j < i; j++) {
            if(v[j] < v[i]) {              
                res[i] = max(res[i], res[j] + 1);
            }
        }
    }
    cout << *max_element(res, res + n);
    return 0;
}