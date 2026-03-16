#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n; cin >> n;
    for(int i = 1; i < n; i++) {
        string s = to_string(i);
        //cout << "num : " << s << "\n";
        int k = s.length();
        //cout << "길이 : " << k << "\n";
        int temp = i;
        for(int j = 0; j < k; j++) {
            temp  += (s[j] - '0');
        }
        if(temp == n) {
            cout << i;
            return 0;
        }
    }
    cout << 0;
    
    return 0;
}