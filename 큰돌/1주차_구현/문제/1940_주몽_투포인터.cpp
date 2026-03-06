#include <bits/stdc++.h>
using namespace std;
int n, m;
int ip;
int head, rear, temp;
int res;
vector<int> v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        cin >> ip;
        v.push_back(ip);
    }
    sort(v.begin(), v.end());
    
    head = 0;
    rear = n - 1;

    while(head < rear) {
        temp = v[head] + v[rear];

        if(temp == m) {
            res += 1;
            head += 1;
        }
        else if(temp < m) {
            head += 1;
        }
        else if(temp > m) {
            rear -= 1;
        }
    }
    cout << res;
    return 0;
}