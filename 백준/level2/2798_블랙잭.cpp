#include <bits/stdc++.h>
using namespace std; 
int n, m;
vector<int> v;
vector<int> res;
int ans;
void dfs(int idx) {
    if(res.size() == 3) {
        int temp = 0;
        for(int i = 0; i < 3; i++) {
            temp += res[i];
        }
        if(temp <=  m) ans = max(ans, temp);
        return;
    }
    if(idx == n) return;
    res.push_back(v[idx]);
    dfs(idx + 1);
    res.pop_back();
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        int ip; cin >> ip;
        v.push_back(ip);
    }
    dfs(0);
    cout << ans;
    
    return 0;
}