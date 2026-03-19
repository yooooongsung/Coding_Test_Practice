#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    int h1, b1;
    cin >> h1 >> b1;
    int h2, b2;
    cin >> h2 >> b2;

    int one = 3 * h1 + b1;
    int two = 3 * h2 + b2;
    if(one > two) cout << 1 << " " << one - two;
    else if(one < two) cout << 2 << " " << two - one;
    else if(one == two) cout << "NO SCORE";
    
    
    return 0;
}