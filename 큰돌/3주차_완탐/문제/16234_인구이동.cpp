#include <bits/stdc++.h>
using namespace std;
int n, L, R, matrix[54][54], visited[54][54], states, sum, ans;
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
vector<pair<int, int>> union_list;

void dfs(int y, int x) {
    visited[y][x] = 1;
    states += 1;
    sum += matrix[y][x];
    union_list.push_back({y, x});
    for(int i = 0; i < 4; i++) {
        int ny = dy[i] + y;
        int nx = dx[i] + x;
        if(ny >= 0 && ny < n && nx >= 0 && nx < n && visited[ny][nx] == 0) {
            if(abs(matrix[ny][nx] - matrix[y][x]) >= L && abs(matrix[ny][nx] - matrix[y][x]) <= R) {
                dfs(ny, nx);
            }
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> L >> R;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> matrix[i][j];
        }
    }
    
    while(true) {
        bool is_moved = false;
        memset(visited, 0, sizeof(visited));
        
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(visited[i][j] == 0) {
                    union_list.clear();
                    sum = 0;
                    states = 0;

                    dfs(i, j);

                    if(union_list.size() > 1) {
                        is_moved = true;
                        int avg = sum / states;
                        for(auto it : union_list) {
                            matrix[it.first][it.second] = avg;
                        }
                    }
                }
            }
        }
        if(!is_moved) break;
        ans++;
    }
    cout << ans;
    return 0;
}