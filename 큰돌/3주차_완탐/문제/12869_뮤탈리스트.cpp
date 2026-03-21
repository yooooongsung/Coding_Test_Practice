#include <bits/stdc++.h>
using namespace std;
int n, scv[3], visited[64][64][64];

int dam[6][3] = {
    {9, 3, 1}, {9, 1, 3}, {3, 9, 1},
    {3, 1, 9}, {1, 9, 3}, {1, 3, 9}
};

struct S{
    int a, b, c;
};

deque<S> q;

void bfs(int a, int b, int c) {
    q.push_back({a,b,c});
    visited[a][b][c] = 1;
    while(q.size()) {
        int a = q.front().a;
        int b = q.front().b;
        int c = q.front().c;
        q.pop_front();
        if(visited[0][0][0]) break;

        for(int i = 0; i < 6; i++) {
            int na = max(0, a - dam[i][0]);
            int nb = max(0, b - dam[i][1]);
            int nc = max(0, c - dam[i][2]);
            if(visited[na][nb][nc] != 0 ) continue;
            visited[na][nb][nc] = visited[a][b][c] + 1;
            q.push_back({na, nb, nc});
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> scv[i];
    }
    bfs(scv[0], scv[1], scv[2]);
    cout << visited[0][0][0] - 1;
    return 0;
}