#include <bits/stdc++.h>
using namespace std; 
int n, k, visited[200004], cnt[200004], parent[200004];
deque<int> q;
deque<int> ans;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> k;
    if(n == k) {
        cout << 0 << "\n";
        cout << n;
        return 0;
    }
    visited[n] = 1;
    cnt[n] = 1;
    q.push_back(n);
    
    while(!q.empty()) {
        int now = q.front();
        q.pop_front();
        for(int next : {now + 1, now - 1, now * 2}) {
            if(0 <= next && next <= 100004) {
                if(visited[next] == 0) {
                    visited[next] = visited[now] + 1;
                    parent[next] = now;
                    q.push_back(next);
                }
            }
        }
    }
    cout << visited[k] - 1 << "\n";
    int cur = k;
    while(cur != n) {
        ans.push_front(cur);
        cur = parent[cur];
    }
    ans.push_front(n);
    for(int i : ans) cout << i << " ";
    
    return 0;
}