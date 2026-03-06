#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    map<int, string> is;
    map<string, int> si;
    // string arr[100004];

    int n,m;
    cin >> n >> m;

    string a;
    for(int i = 0; i < n; i++) {
        cin >> a;
        is[i + 1] = a;
        si[a] = i + 1;
        // arr[i + 1] = a;
    }

    string b;
    for(int j = 0; j < m; j ++) {
        cin >> b;
        if(isdigit(b[0])) {
            cout << is[stoi(b)] << "\n";
            // cout << a[stoi(b)] << endl;
        }
        else {
            cout << si[b] << "\n";
        }
    }
    return 0;
}