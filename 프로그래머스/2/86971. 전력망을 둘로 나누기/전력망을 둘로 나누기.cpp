#include <bits/stdc++.h>

using namespace std;
int dfs(vector<vector<int>> &wires, int cur_node, int cut, vector<bool> &visited) {
    int cnt = 1;
    visited[cur_node] = true;
    for(int i = 0; i < wires.size(); i++) {
        if(i == cut) continue;
        
        int next_node = -1;
        if(wires[i][0] == cur_node) next_node = wires[i][1];
        else if(wires[i][1] == cur_node) next_node = wires[i][0];
        
        if(next_node != -1 && !visited[next_node]) {
            cnt += dfs(wires, next_node, cut, visited);
        }
    }
    return cnt;
}

int solution(int n, vector<vector<int>> wires) {
    int answer = 1000;
    int k = wires.size();
    
    for(int i = 0; i < wires.size(); i++) {
        vector<bool> visited(n + 1, false);
        int start_node = wires[i][0];
        int a = dfs(wires, start_node, i, visited);
        int b = n - a;
        answer = min(answer, abs(a-b));
    }
    
    return answer;
}