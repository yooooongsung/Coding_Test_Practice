#include <bits/stdc++.h>
using namespace std;
int n,m,k,matrix[104][104],visited[104][104],res, sy, sx, ey, ex,cnt;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
vector<int> ans;
int dfs(int y, int x) {
    matrix[y][x] = 1;
    cnt += 1;
    for(int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if(ny >= 0 && ny < n && nx >= 0 && nx < m && matrix[ny][nx] == 0) {
            dfs(ny, nx);
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m >> k;
    for(int i = 0; i < k; i++) {
        cin >> sx >> sy >> ex >> ey;
        for(int a = sy; a < ey; a++) {
            for(int b = sx; b < ex; b++) {
                matrix[a][b] = 1;
            }
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(matrix[i][j] == 0) {
                cnt = 0;
                int temp = dfs(i, j);
                ans.push_back(temp);
                res += 1;
            }
        }
    }

    cout << res << "\n";
    sort(ans.begin(), ans.end());
    for(int a : ans) cout << a << ' ';
    
    
    return 0;
}