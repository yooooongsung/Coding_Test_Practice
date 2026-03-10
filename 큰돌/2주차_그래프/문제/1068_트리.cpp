#include <bits/stdc++.h>
using namespace std;
int n, res;
map<int, vector<int>> tree;

void delNode(int node) {
    deque<int> q;
    q.push_back(node);
    while(q.size()) {
        int temp = q.front();
        q.pop_front();
        if(!tree[temp].empty()) {
            for(int i : tree[temp]) {
                q.push_back(i);
            }
        }
        tree.erase(temp);
    }
    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n;
    int ip;
    for(int i = 0; i < n; i++) {
        tree[i];
    }
    for(int i = 0; i < n; i++) {
        cin >> ip;
        if(ip != -1) tree[ip].push_back(i);
    }

    int del; cin >> del;

    for(auto & it : tree) {
        auto &v = it.second;
        for(int i = 0; i < v.size();) {
            if(del == v[i]) v.erase(v.begin() + i);
            else i++;
        }
    }

    delNode(del);

    for(auto & it : tree) {
        auto &v = it.second; 
        if(v.empty()) res++;
    }
    cout << res;
    return 0;
}
