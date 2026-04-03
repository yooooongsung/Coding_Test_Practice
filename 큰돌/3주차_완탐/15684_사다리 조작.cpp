#include <bits/stdc++.h>
using namespace std; 
int n, m, h, a, b, ans = 4;
int matrix[34][14];

bool check() {
    for(int i = 1; i <= n; i++) {
        int cur = i;
        for(int j = 1; j <= h; j++) {
            if(matrix[j][cur] == 1) cur++;
            else if(matrix[j][cur - 1]) cur--;
        }
        if(cur != i) return false;
    }
    return true;
}
void dfs(int cnt, int r) {
    if(check()) {
        ans = min(ans, cnt);
        return;
    }
    if(cnt >= 3) return;
    
    for(int i = r; i <= h; i++) {
        for(int j = 1; j < n; j++) {
            if(!matrix[i][j] && !matrix[i][j - 1] && !matrix[i][j + 1]) {
                matrix[i][j] = 1;
                dfs(cnt + 1, i);
                matrix[i][j] = 0;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m >> h;
    if(m == 0) {
        cout << 0;
        return 0;
    }

    for(int i = 0; i < m; i++) {
        cin >> a >> b;
        matrix[a][b] = 1;
    }
    dfs(0, 1);
    if(ans > 3) cout << -1;
    else cout << ans;
    return 0;
}