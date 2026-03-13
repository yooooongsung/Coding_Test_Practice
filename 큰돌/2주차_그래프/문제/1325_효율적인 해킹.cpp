#include <bits/stdc++.h>
using namespace std;
vector<int> tree[10005];
int n, m;
int visited[10005];
int bfs(int i) {
    int cnt = 1;
    deque<int> q;
    q.push_back(i);
    visited[i] = 1;
    while(!q.empty()) {
        int cur = q.front();
        q.pop_front();
        for(int next : tree[cur]) {
            if(visited[next] == 0) {
                visited[next] = 1;
                q.push_back(next);
                cnt++;
            }
            
        }
    }
    return cnt;

}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        tree[b].push_back(a);
    }

    int max_hack = 0;
    vector<int> ans;
    for(int i = 1; i <= n; i++) {
        memset(visited, 0, sizeof(visited));
        int hacks = bfs(i);
        if(hacks > max_hack) {
            max_hack = hacks;
            ans.clear();
            ans.push_back(i);
        }
        else if(hacks == max_hack) ans.push_back(i);
    }
    for(int i : ans) cout << i << " ";
    return 0;
}