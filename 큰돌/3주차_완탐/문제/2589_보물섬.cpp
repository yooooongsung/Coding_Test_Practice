#include <bits/stdc++.h>
using namespace std;
int n, m;
char matrix[54][54];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
vector<int> ans;
int bfs(int i, int j) {
    deque<pair<int,int>> q;
    q.push_back({i, j});
    int visited[54][54] = {0,};
    visited[i][j] = 1;
    int cnt = 0;
    while(q.size()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop_front();
        for(int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if(ny >= 0 && ny < n && nx >= 0 && nx < m && visited[ny][nx] == 0 && matrix[ny][nx] == 'L') {
                visited[ny][nx] = visited[y][x] + 1;
                cnt = max(cnt, visited[ny][nx]);
                q.push_back({ny, nx});
            }
        }
    }
    return cnt;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(matrix[i][j] == 'L') {
                int temp = bfs(i, j);
                ans.push_back(temp);
            }
        }
    }
    int max_val = 0;
    for(int i : ans) {
        max_val = max(max_val, i);
    }
    if(max_val > 0) cout << max_val - 1;
    else cout << 0;
    return 0;
}