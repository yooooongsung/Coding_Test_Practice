#include <bits/stdc++.h>
using namespace std;
int n, ip[1000004], ret[1000004];
deque<int> q;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    fill(ret, ret + n, -1);
    for(int i = 0; i < n; i++) cout << ret[i] << " ";
    for(int i = 0; i < n; i++) {
        cin >> ip[i];
        while(q.size() && ip[q.back()] < ip[i]) {
            ret[q.back()] = ip[i];
            q.pop_back();
        }
        q.push_back(i);
    }
    for(int i = 0; i < n; i++) cout << ret[i] << " ";
    
    return 0;
}