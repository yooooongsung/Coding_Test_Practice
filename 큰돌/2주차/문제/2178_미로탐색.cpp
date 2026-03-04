#include <bits/stdc++.h>
using namespace std;
int n,m, matrix[104][104], visited[104][104];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0,-1};

void bfs(int y, int x) {
    queue<pair<int,int>> q;
    q.push({y, x});
    while(q.size()) {
        y = q.front().first;
        x = q.front().second;
        q.pop();
        for(int i = 0; i < 4; i++) {
            int ny = dy[i] + y;
            int nx = dx[i] + x;
            if(ny >= 0 && ny < n && nx >=0 && nx < m && visited[ny][nx] == 0 && matrix[ny][nx] == 1) {
                visited[ny][nx] = visited[y][x] + 1;
                q.push({ny, nx});
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    
    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for(int j = 0; j < m; j++) {
            if(isdigit(s[j])) matrix[i][j] = s[j] - '0';
        }
    }
    visited[0][0] = 1;
    bfs(0,0);
    cout << visited[n-1][m-1];
    
    return 0;
}