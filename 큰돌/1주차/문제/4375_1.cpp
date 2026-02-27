#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int n; 
    while(cin >> n) {
        int res = 0;
        long long temp = 0;
        while(true) {
            temp = (temp * 10 + 1) % n;
            res++;
            if(temp == 0) {
                cout << res << "\n";
                break;
            }
        }
    }
    
    
    return 0;
}
