#include <bits/stdc++.h>
using namespace std;

int n, m;
int sy, sx;
int my, mx;
int matrix[104][104];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int visited[104][104];

void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({y, x});
    while(q.size()) {
        // auto [y, x] = q.front();
        // y = q.front().first;
        // x = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if(ny >= 0 && ny < n && nx >= 0 && nx < m && visited[ny][nx] == 0) {
                visited[ny][nx] = visited[y][x] + 1;
                q.push({ny,nx});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    cin >> sy >> sx;
    cin >> my >> mx;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }
    visited[sy][sx] = 1;
    bfs(sy, sx);    
    cout << visited[my][mx];
    return 0;
}