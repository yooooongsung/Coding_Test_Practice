#include <bits/stdc++.h>
using namespace std; 
int k;
vector<int> v;
vector<vector<int>> ans;

void dfs(int start, int end, int level) {
    if(level == k) return;
    int mid = (start + end) / 2;
    ans[level].push_back(v[mid]);
    dfs(start, mid - 1, level + 1);
    dfs(mid + 1, end, level + 1);
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> k;
    ans.resize(k);
    for(int i = 0; i < pow(2, k) - 1; i++) {
        int ip; cin >> ip;
        v.push_back(ip);
    }
    dfs(0, v.size() - 1, 0);
    for(int i = 0; i < k; i++) {
        for(int j : ans[i]) cout << j << " ";
        cout << "\n";
    }
    
    return 0;
}