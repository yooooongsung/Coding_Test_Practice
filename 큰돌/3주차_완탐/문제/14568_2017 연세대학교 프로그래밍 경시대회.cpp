#include <bits/stdc++.h>
using namespace std;
int candy, ans;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> candy;
    if(candy < 6) {
        cout << 0;
        return 0;
    }
    for(int t = 2; t <= candy - 4; t+=2) {
        for(int y = 1; y <= candy; y++) {
            for(int n = y + 2; n <= candy; n++) {
                if(t + y + n == candy) ans++;
            }
        }
    }
    cout << ans;
    return 0;
}
// t를 먼저 정하고 2 4 6 8 10
// 다음 y를 정하고
// 그 다음 n을 정한다
// 합이 같다면 ans++
// 8
// 2 1 5
// 2 2 4
// 4 1 3