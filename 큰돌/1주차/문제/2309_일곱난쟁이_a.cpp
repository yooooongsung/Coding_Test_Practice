#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v;
    int ip;
    for(int i = 0; i < 9; i++) {
        cin >> ip;
        v.push_back(ip);
    }
    sort(v.begin(), v.end());

    do{
        int sum = 0;
        for(int i = 0; i < 7; i++) sum += v[i];
        
        if(sum == 100) break;
    }while(next_permutation(v.begin(), v.end()));

    for(int k = 0; k < 7; k++) cout << v[k] << endl;
    return 0;
}