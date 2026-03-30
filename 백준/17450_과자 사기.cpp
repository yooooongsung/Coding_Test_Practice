#include <bits/stdc++.h>
using namespace std; 
pair<int, int> s;
pair<int, int> n;
pair<int, int> u;
pair<double, char> ss, nn, uu;
vector<pair<double, char>> v;

double cal(int a, int b) {
    if(a * 10 >= 5000) {
        return (double)(b * 10) / (a * 10 - 500);
    }
    else {
        return (double)(b * 10) / (a * 10);
    }   
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> s.first; cin >> s.second; 
    cin >> n.first; cin >> n.second;
    cin >> u.first; cin >> u.second;

    ss.first = cal(s.first, s.second);
    nn.first = cal(n.first, n.second);
    uu.first = cal(u.first, u.second);

    ss.second = 'S'; nn.second = 'N'; uu.second = 'U';
    v.push_back(ss); v.push_back(nn); v.push_back(uu);

    sort(v.begin(), v.end(), [](auto &a, auto &b) {
        return a.first > b.first;
    });
    cout << v[0].second;
    return 0;
}