#include <bits/stdc++.h>
using namespace std;
int r, c, visited[1004][1004], ans;
char matrix[1004][1004];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};
pair<int, int> jh;
deque<pair<int, int>> fq;

void bfs(int a, int b) {
    while(!fq.size()) {
        int fy = fq.front().first;
        int fx = fq.front().second;
        fq.pop_front();
        for(int k = 0; k < 4; k++) {
            int fny = dy[k] + fy;
            int fnx = dx[k] + fx;
            if(fny < 0 || fny >= r || fnx < 0 || fnx >= c) continue;
            if(matrix[fny][fnx] == 'J' || matrix[fny][fnx] == '.') {
                cout << "불 퍼트리기 : " << fny << ", " << fnx << "\n";
                matrix[fny][fnx] = 'F';
                visited[fny][fnx] = visited[fy][fx] + 1;
                fq.push_back({fny, fnx});
            }                
        }
    }

    deque<pair<int, int>> jq;
    jq.push_back({a, b});
    visited[a][b] = 1;

    while(!jq.empty()) {
        int jy = jq.front().first;
        int jx = jq.front().second;
        jq.pop_front();

        for(int k = 0; k < 4; k++) {
            int jny = dy[k] + jy;
            int jnx = dx[k] + jx;
            if(jny < 0 || jny >= r || jnx < 0 || jnx >= c) {
                cout << "탈출 성공 : " << jny << ", " << jnx << "\n";
                ans = visited[jny][jnx];
                return;
            }
            if(visited[jny][jnx] > visited[jy][jx]) {
                cout << "지호가 갈 다음 칸 : " << jny << ", " << jnx << "\n";
                visited[jny][jnx] = visited[jy][jx] + 1;
                cout << "시간 : " << visited[jny][jnx] << "\n";
                jq.push_back({jny, jnx});
            }
        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> r >> c;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            cin >> matrix[i][j];
            if(matrix[i][j] == 'J') {
                jh.first = i;
                jh.second = j;
            }
            else if(matrix[i][j] == 'F') {
                visited[i][j] = 1;
                fq.push_back({i,j});
            }
        }
    }
    bfs(jh.first, jh.second);
    cout << ans;
    
    return 0;
}