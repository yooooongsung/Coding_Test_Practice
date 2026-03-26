#include <bits/stdc++.h>
using namespace std;

int n, m, jy, jx, bj, bx;
char matrix[304][304];
int visited[304][304];
int dy[4] = {-1, 0, 1, 0};
int dx[4] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    cin >> jy >> jx >> bj >> bx;
    // 인덱스 맞추기 (1번부터 시작하니까 -1)
    jy--; jx--; bj--; bx--;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> matrix[i][j];
        }
    }

    queue<pair<int, int>> q;
    q.push({jy, jx});
    visited[jy][jx] = 1;
    int turn = 0;

    while (true) {
        turn++;
        queue<pair<int, int>> next_q; // 이번 파동에 '1'을 만나서 멈춘 지점들

        while (!q.empty()) {
            int y = q.front().first;
            int x = q.front().second;
            q.pop();

            // 범인을 찾으면 바로 종료!
            if (y == bj && x == bx) {
                cout << turn - 1 << "\n"; // 첫 진입을 1로 잡았으니 -1 (또는 로직에 맞춰 조절)
                return 0;
            }

            for (int i = 0; i < 4; i++) {
                int ny = y + dy[i];
                int nx = x + dx[i];

                if (ny < 0 || ny >= n || nx < 0 || nx >= m || visited[ny][nx]) continue;

                visited[ny][nx] = 1;

                if (matrix[ny][nx] == '0') {
                    // 0이면 파동이 계속 퍼짐 (현재 큐에 넣음)
                    q.push({ny, nx});
                } else {
                    // 1이나 범인이면 파동이 여기서 멈춤 (다음 턴 큐에 넣음)
                    matrix[ny][nx] = '0'; // 친구가 쓰러짐
                    next_q.push({ny, nx});
                }
            }
        }
        // 이번 턴에 멈췄던 지점들이 다음 턴의 시작점이 됨
        q = next_q;
    }

    return 0;
}