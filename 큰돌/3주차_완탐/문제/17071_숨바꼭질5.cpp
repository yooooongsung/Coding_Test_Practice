#include <bits/stdc++.h>
using namespace std; 
const int MAX = 500000;
int n, k;
int visited[2][MAX + 1];
deque<int> q;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> k;
    if(n == k) {
        cout << 0;
        return 0;
    }
    memset(visited, -1, sizeof(visited));

    deque<pair<int, int>> q;
    q.push_back({n, 0});
    visited[0][n] = 0;
    while(!q.empty()) {
        int now = q.front().first;
        int time = q.front().second;
        q.pop_front();
        int next_time = time + 1;
        int type = next_time % 2;
        for(int next : {now + 1, now - 1, now * 2}) {
            if(0 <= next && next <= MAX) {
                if(visited[type][next] == -1) {
                    visited[type][next] = next_time;
                    q.push_back({next, next_time});
                }
            }
        }

    }
    int bro_pos = k;
    int t = 0;
    while(true) {
        t++;
        bro_pos += t;
        
        if(bro_pos > MAX) {
            cout << -1;
            return 0;
        }

        if(visited[t % 2][bro_pos] != -1 && visited[t % 2][bro_pos] <= t) {
            cout << t;
            return 0;
        }
    }
}