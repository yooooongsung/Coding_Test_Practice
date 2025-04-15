#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

int dfs(int node, vector<bool> &visited, unordered_map<int,vector<int>> &dict, int &cnt) {
    // 참조자로 받아라 제발 !!
    visited[node] = true;
    for (int i = 0; i < dict[node].size(); i++) {
        int next = dict[node][i];
        if (!visited[next]) {
            cnt += 1;
            dfs(next, visited, dict, cnt);
        }
    }

    return cnt;
}

int main() {
    int n,m;
    cin >> n >> m;
    unordered_map<int,vector<int>> dict; // 해시 선언 잘해라 !!

    for (int i = 0; i < m; i++) {
        int x,y;
        cin >> x >> y;
        dict[x].push_back(y);
        dict[y].push_back(x);
    }
    vector<bool> visited(n+1,false);
    int cnt = 0;
    dfs(1, visited, dict,cnt);
    cout << cnt << endl;
    return 0;
}