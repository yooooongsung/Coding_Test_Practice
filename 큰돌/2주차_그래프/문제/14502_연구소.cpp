#include <bits/stdc++.h>
using namespace std;
int n, m, matrix[8][8], visited[8][8];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
int res = 0, temp = 0;

int virus() {
    deque<pair<int,int>> q;
    int cnt = 0;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(matrix[i][j] == 2) {
                visited[i][j] = 1;
                q.push_back({i, j});
            }
            
        }
    }
    while(q.size()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop_front();
        for(int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if(ny >= 0 && ny < n && nx >= 0 && nx < m && visited[ny][nx] == 0) {
                if(matrix[ny][nx] == 0) {
                    visited[ny][nx] = 1;
                    q.push_back({ny, nx});
                }
            }
        }
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(visited[i][j] == 0 && matrix[i][j] == 0) cnt++;
        }
    }
    return cnt;
}

void setWall(int wall) {
    if(wall == 3) {
        temp = virus();
        res = max(res, temp);
        temp = 0;
        memset(visited, 0, sizeof(visited));
        return;
    }
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(matrix[i][j] == 0) {
                matrix[i][j] = 1;
                setWall(wall + 1);
                matrix[i][j] = 0;
            }
        }
    }
    return;
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
    setWall(0);
    cout << res;
    
    return 0;
}