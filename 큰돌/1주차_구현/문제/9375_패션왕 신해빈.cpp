#include <bits/stdc++.h>
using namespace std;
int main() {
    int tc;
    cin >> tc;
    for(int i = 0; i < tc; i++) {
        int n;
        cin >> n;
        map<string, int> m;
        for(int j = 0; j < n; j++) {
            string item, cate;
            cin >> item >> cate;
            m[cate]++;
        }
        long long res = 1;
        for(const auto& item : m) {
            res *= (item.second+1);
        }
        cout << res - 1 << endl;
    }
    
    return 0;
}