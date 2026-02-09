#include <bits/stdc++.h>
using namespace std;

int k;
int cnt = 0;
vector<int> v = {1, 2, 3, 4, 5, 6};

void print(vector<int> b) {
    for(int i = 0; i < b.size(); i++) cout << v[b[i]] << " ";
    cout << endl;
}

void combi(int start, vector<int>& b) {
    if(b.size() == k) {
        cnt++;
        print(b);
        return;
    }
    for (int i = start + 1; i < v.size(); i++) {
        b.push_back(i); // b[i] 가 아니라 i 로 한다. 중복 값이 있을 수 있기 때문에 index 기준으로 push하기.
        combi(i, b);
        b.pop_back();}
    }

int main() {
    cin >> k;
    vector<int> b;
    combi(-1, b);
    cout << cnt << endl;
    return 0;
}