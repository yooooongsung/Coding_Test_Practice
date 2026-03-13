#include <bits/stdc++.h>
using namespace std;
int n, ip;
double avg;
vector<int> v;
map<int, int> m;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> ip;
        avg += ip;
        v.push_back(ip);
        m[ip]++;
    }
    // 1. 산술평균
    cout << (int) round(avg / n)  << "\n";

    // 2. 중앙값
    sort(v.begin(), v.end());
    cout << v[n / 2] << "\n";

    // 3. 최빈값
    int max_time = 0;
    for(auto & it : m) {
        max_time = max(it.second, max_time);
    }

    vector<int> mid;
    for(auto & it : m) {
        if(it.second == max_time) mid.push_back(it.first);
    }
    if(mid.size() > 1) cout << mid[1] << "\n";
    else cout << mid[0] << "\n";

    cout << v.back() - v.front() << "\n";
    
    return 0;
}