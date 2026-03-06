#include <bits/stdc++.h>
using namespace std;
int n, matrix[104][104], visited[104][104], res, ans = -1;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
vector<int> v;

void dfs(int y, int x, int water) {
    visited[y][x] = 1;
    for(int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if(ny >= 0 && ny < n && nx >= 0 && nx < n && visited[ny][nx] == 0 && matrix[ny][nx] > water) {
            dfs(ny, nx, water);
        }
    }
    return;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    v.push_back(0); // 이 문제의 핵심. 안전영역이 1개인, 즉 모든 좌표의 값이 동일할 떄는 지역이 다 물에 안잠길 수 있음.
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> matrix[i][j];
            if(find(v.begin(), v.end(), matrix[i][j]) == v.end()) v.push_back(matrix[i][j]);
        }
    }
    sort(v.begin(), v.end());
    for(int water : v) {
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(matrix[i][j] > water && visited[i][j] == 0) {
                    dfs(i, j, water);
                    res += 1;
                }
            }
        }
        ans = max(ans, res);
        res = 0;
        memset(visited, 0, sizeof(visited));
    }
    
    cout << ans;
    return 0;
}