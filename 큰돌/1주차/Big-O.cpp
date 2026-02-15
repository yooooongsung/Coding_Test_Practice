#include <bits/stdc++.h>
using namespace std;

int N;
int cnt;
void solve(int N) {
    int a = 0, i = N;
    while (i > 0) {
        a += i;
        i /= 2;
        cnt += 1;
    }
    cout << cnt << endl;
}

int main () {
    cin >> N;
    solve(N);
    return 0;
}

// 