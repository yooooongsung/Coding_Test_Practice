#include <bits/stdc++.h>
using namespace std;
int n, c, ip;
vector<int> v;
unordered_map<int, int> m;
vector<pair<int,int>> ans;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> c;
    for(int i = 0; i < n; i++) {
        cin >> ip;
        if(find(v.begin(), v.end(), ip) == v.end()) {
            v.push_back(ip); // 나온 순서를 담은 유니크한 값만 담긴 벡터
        }
        m[ip]++; // 빈도수 체크
    }
    for(const auto & it : m) {
        ans.push_back({it.first, it.second});
    }
    
    sort(ans.begin(), ans.end(), [&](auto & a, auto & b) {
        if(a.second != b.second) {
            return a.second > b.second;
        }
        auto it_a = find(v.begin(), v.end(), a.first);
        auto it_b = find(v.begin(), v.end(), b.first);
        return it_a < it_b;
    });


    for(const auto & it : ans) {
        for(int i = 0; i < it.second; i++) {
            cout << it.first << " ";
        }
    }

    return 0;
}