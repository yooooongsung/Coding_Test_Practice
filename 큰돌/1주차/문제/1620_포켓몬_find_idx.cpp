#include <bits/stdc++.h>
using namespace std;
int main() {
    int n,m;
    cin >> n >> m;

    vector<string> v(n);

    string a;
    for(int i = 0; i < n; i++) {
        cin >> a;
        v[i] = a;
    }

    string b;
    for(int j = 0; j < m; j++) {
        cin >> b;
        if(isdigit(b[0])) {
            cout << v[stoi(b)-1] << endl;
        }
        else {
            auto it = find(v.begin(), v.end(), b);
            if (it != v.end()) {
                int idx = it - v.begin();
                cout << idx+1 << endl;
            }
        }
    }
    return 0;
}