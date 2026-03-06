#include <bits/stdc++.h>
using namespace std;
int a,b,c;
long long exp(int tar) {
    if(tar == 1) {
        return a % c;
    }
    long long temp = exp(tar / 2); 
    if(tar % 2 == 0) return temp * temp % c;
    else return (temp * temp % c) * (a % c) % c;
}

/*
1 2 5 10
4 2 2 2
*/

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> a >> b >> c;
    int tar = b;
    long long res = exp(tar);
    cout << res;
    return 0;
}