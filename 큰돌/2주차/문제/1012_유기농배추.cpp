#include <bits/stdc++.h>
using namespace std;
int t,n,m,k,matrix[54][54],visited[54][54],res;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

void dfs(int y, int x) {
    visited[y][x] = 1;
    for(int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if(ny >= 0 && ny < n && nx >= 0 && nx < m && visited[ny][nx] == 0 && matrix[ny][nx] == 1) {
            dfs(ny, nx);
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> t;
    for(int i = 0; i < t; i++) {
        cin >> m >> n;
        cin >> k;

        memset(matrix, 0, sizeof(matrix));
        memset(visited, 0, sizeof(visited));

        for(int j = 0; j < k; j++) {
            int y, x;
            cin >> x >> y;
            matrix[y][x] = 1;
        }
        for(int a = 0; a < n; a++) {
            for(int b = 0; b < m; b++) {
                if(matrix[a][b] == 1 && visited[a][b] == 0) {
                    dfs(a, b);
                    res += 1;
                }
            }
        }
        cout << res << "\n";
        res = 0;
    }
    return 0;
}

