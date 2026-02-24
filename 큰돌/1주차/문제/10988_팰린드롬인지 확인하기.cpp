#include <bits/stdc++.h>
using namespace std;

int main() {
    string ip;
    cin >> ip;
    string res = ip;
    reverse(res.begin(), res.end());
    
    // for(int i = ip.size()-1; i >= 0; i--) {
    //     res += ip[i];
    // }
    if(ip == res) cout << 1;
    else cout << 0;
    return 0;
}