#include <bits/stdc++.h>
using namespace std; 
int r, c, ans = -987654321;
char matrix[20][20];
int visited[26];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
deque<pair<int, int>> q;

void dfs(int y, int x, int cnt) {
    ans = max(ans, cnt);
    visited[matrix[y][x] - 'A'] = 1;
    for(int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if(0 <= ny && ny < r && 0 <= nx && nx < c && visited[matrix[ny][nx] - 'A'] == 0) {
            dfs(ny, nx, cnt + 1);
        }
    }
    visited[matrix[y][x] -'A'] = 0;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> r >> c;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            cin >> matrix[i][j];
        }
    }
    dfs(0, 0, 1);
    cout << ans;
    return 0;
}