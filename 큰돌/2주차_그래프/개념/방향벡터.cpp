#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> v = {{1, 0, 1}, {1, 0, 1}, {0, 1, 1}};
int visited[3][3];
const int dy[] = {-1, -1, 0, 1, 1, 1, 0, -1};
const int dx[] = {0, 1, 1, 1, 0, -1, -1, -1};

void dfs(int y, int x) {
    for(int k = 0; k < 8; k++) {
        int ny = dy[k] + y;
        int nx = dx[k] + x;

        if(ny >= 0 && ny < 3 && nx >=0 && nx < 3 && visited[ny][nx] == 0 && v[ny][nx] == 1) {
            cout << ny << " - " << nx << "\n";
            visited[ny][nx] = 1;
            dfs(ny, nx);
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(v[i][j] == 1 && visited[i][j] == 0) {
                cout << i << " - " << j << "\n";
                visited[i][j] = 1;
                dfs(i,j);
            }
        }
    }
    
}