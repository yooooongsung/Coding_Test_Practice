#include <bits/stdc++.h>
using namespace std;
int n;
vector<int> adj[100004];
deque<int> q;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    int ans[n + 1] = {0,};
    int visited[n + 1] = {0,};
    int a, b;
    while(cin >> a >> b) {
        adj[a].push_back(b); adj[b].push_back(a);
    }
    q.push_back(1);
    visited[1] = 1;
    while(q.size()) {
        int temp = q.front();
        q.pop_front();
        for(int k : adj[temp]) {
            if(visited[k] == 1) continue;
            ans[k] = temp;
            visited[k] = 1;
            q.push_back(k);
        }
    }
    for(int i = 2; i <= n; i++) cout << ans[i] << "\n";
    return 0;
}