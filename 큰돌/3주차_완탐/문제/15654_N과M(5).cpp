#include <bits/stdc++.h>
using namespace std;
int n, m, visited[10];
vector<int> v;
vector<vector<int>> ans;
void combi(int start, vector<int> res) {
    if(res.size() == m) {
        ans.push_back(res);
        return;
    }
    for(int i = 0; i < v.size(); i++) {
        if(visited[i] == 1) continue;
        visited[i] = 1;
        res.push_back(v[i]);
        combi(i, res);
        res.pop_back();
        visited[i] = 0;
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    
    for(int i = 0; i < n; i++) {
        int ip; cin >> ip;
        v.push_back(ip);
    }
    sort(v.begin(), v.end());
    vector<int> res;
    combi(0,res);
    for(auto its : ans) {
        for(auto it : its) {
            cout << it << " ";
        }
        cout << "\n";
    }
    
    return 0;
}