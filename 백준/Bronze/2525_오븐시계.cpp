#include <bits/stdc++.h>
using namespace std; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    int a, b, t;
    cin >> a >> b >> t;
    if(b + t >= 60) {
        int temp = (b + t) / 60;
        a += temp;
        b = b + t - 60 * temp;
        if(a >= 24) {
            a -= 24;
        }
    }
    else {
        b += t;
    }
    cout << a << " " << b;

    
    return 0;
}