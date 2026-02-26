#include <bits/stdc++.h>
using namespace std;
int n, m;
int arr[150004];
int res;

void combi(int idx, vector<int> & v){
    if(v.size() == 2) {
        int a = arr[v[0]];
        int b = arr[v[1]];
        if(a + b == m) res++;
        return;
    }
    for(int i = idx + 1; i < n; i++) {
        v.push_back(i);
        combi(i, v);
        v.pop_back();
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        int ip;
        cin >> ip;
        arr[i] = ip;
    }
    vector<int> v;
    combi(-1, v);   
    cout << res;
    return 0;
}