#include <bits/stdc++.h>
using namespace std;
vector<pair<int,int>> home, chicken;
vector<vector<int>> chicken_list;
int n, m, matrix[54][54], ans = 987654321;
void combi(int start, vector<int> v) {
    if(v.size() == m) {
        chicken_list.push_back(v);
        return;
    }
    for(int i = start; i < chicken.size(); i++) {
        v.push_back(i);
        combi(i + 1, v);
        v.pop_back();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> matrix[i][j];
            if(matrix[i][j] == 1) home.push_back({i, j});
            else if(matrix[i][j]== 2) chicken.push_back({i, j});
        }
    }
    vector<int> v;
    combi(0, v);
    for(auto _chicken : chicken_list) {
        int res = 0;
        for(auto _home : home) {
            int _min = 987654321;
            for(auto _ck : _chicken) {
                int temp = abs(chicken[_ck].first - _home.first) + abs(chicken[_ck].second - _home.second);
                _min = min(_min, temp);
            }
            res += _min;
        }
        ans = min(ans, res);
    }
    cout << ans;
    
    return 0;
}