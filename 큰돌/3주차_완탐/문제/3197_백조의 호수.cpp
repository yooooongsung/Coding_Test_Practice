#include <bits/stdc++.h>
using namespace std; 
int r, c, visited_water[1504][1504], visited_swan[1504][1504], sy1, sx1, sy2, sx2;
char matrix[1504][1504];
deque<pair<int, int>> swan_q;
deque<pair<int, int>> next_swan_q;
deque<pair<int, int>> q;
deque<pair<int, int>> next_q;
int dy[4] = {-1, 0 , 1, 0};
int dx[4] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> r >> c;
    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            cin >> matrix[i][j];
            if(matrix[i][j] == 'L') {
                swan_q.push_back({i, j});
                q.push_back({i, j});
                visited_water[i][j] = 1;
            }
            if(matrix[i][j] == '.') {
                q.push_back({i, j});
                visited_water[i][j] = 1;
            }
        }
    }
    sy1 = swan_q.front().first; sx1 = swan_q.front().second;
    sy2 = swan_q.back().first; sx2 = swan_q.back().second;
    swan_q.pop_back();

    visited_swan[sy1][sx1] = 1;

    int turn = 0;

    while(true) {
        while(!swan_q.empty()) {
            int sy = swan_q.front().first;
            int sx = swan_q.front().second;
            swan_q.pop_front();
            for(int i = 0; i < 4; i++) {
                int nsy = sy + dy[i];
                int nsx = sx + dx[i];
                if(0 <= nsy && nsy < r && 0 <= nsx && nsx < c && visited_swan[nsy][nsx] == 0) {
                    if(matrix[nsy][nsx] == 'L') {
                        cout << turn;
                        return 0;
                    }
                    else if(matrix[nsy][nsx] == '.') {
                        visited_swan[nsy][nsx] = 1;
                        swan_q.push_back({nsy, nsx});
                    }
                    else if(matrix[nsy][nsx] == 'X') {
                        visited_swan[nsy][nsx] = 1;
                        next_swan_q.push_back({nsy, nsx});
                    }
                }
            }
        }
        while(!q.empty()) {
            int wy = q.front().first;
            int wx = q.front().second;
            q.pop_front();
            for(int i = 0; i < 4; i++) {
                int nwy = wy + dy[i];
                int nwx = wx + dx[i];
                if(0 <= nwy && nwy < r && 0 <= nwx && nwx < c && visited_water[nwy][nwx] == 0) {
                    if(matrix[nwy][nwx] == '.' || matrix[nwy][nwx] == 'L') {
                        visited_water[nwy][nwx] = 1;
                    }
                    else if (matrix[nwy][nwx] == 'X') {
                        visited_water[nwy][nwx] = 1;
                        matrix[nwy][nwx] = '.';
                        next_q.push_back({nwy, nwx});
                    }
                }
            }
        }
        swan_q = next_swan_q;
        next_swan_q.clear();

        q = next_q;
        next_q.clear();

        turn++;
    }
    return 0;
}