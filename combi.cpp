#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void combi(int start, vector<int> b) {
    if(b.size() == k) {
        return;
    }
    for (int i = start + 1; i < n; i++) {
        b.push_back(i); // b[i] 가 아니라 i 로 한다. 중복 값이 있을 수 있기 때문에 index 기준으로 push하기.
        combi(i, b);
        b.pop_back();}
    }

int main() {
    vector<int> v = {2, 1, 3, 100, 200};
    sort(v.begin(), v.end());
    do{
        for(int i = 0; i < v.size(); i++){
            cout << v[i] << " ";
        }
        cout << endl;
    }while(next_permutation(v.begin(), v.end()));
}