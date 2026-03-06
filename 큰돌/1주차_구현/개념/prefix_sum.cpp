#include <bits/stdc++.h>
using namespace std;
int n,m;
int a,b;
int main () {
    cin >> n >> m;

    vector<int> num(100000);
    for(int i = 1; i <= n; i++) {
        num[i] = i;
    }

    vector<int> psum(100000);
    for(int i = 1; i <= n; i++) {
        psum[i] = psum[i-1] + num[i];
    }

    for(int i = 0; i < m; i++) {
        cin >> a >> b;
        cout << psum[b] - psum[a-1] << endl;
    }

    return 0;
}
