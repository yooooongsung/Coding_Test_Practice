#include <bits/stdc++.h>
using namespace std; 
int n, matrix[70][70];
string ans, s;
void dfs(int n, int y, int x) {
    int value = matrix[y][x];
    for(int i = y; i < y + n; i++) {
        for(int j = x; j < x + n; j++) {
            if(value != matrix[i][j]) {
                ans += '(';
                dfs(n / 2, y, x);
                dfs(n / 2, y, x + n / 2);
                dfs(n / 2, y + n / 2, x);
                dfs(n / 2, y + n / 2, x + n / 2);
                ans += ')';
                return;
            }
        }
    }
    ans += to_string(value);
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> s;
        for(int j = 0; j < n; j++) {
            matrix[i][j] = s[j] - '0';
        }
    }
    dfs(n, 0, 0);
    cout << ans;
    return 0;
}