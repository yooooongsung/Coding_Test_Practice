#include <bits/stdc++.h>
using namespace std;

// 1. map
// map<int, int> mp;
// int main() {
//     vector<int> v = {1,1,2,3,4,5};
//     for(int i : v) {
//         if(mp[i]) {
//             continue;
//         }
//         else {
//             mp[i] = 1;
//         }
//     }
//     vector<int> ret;
//     for(auto item : mp) {
//         ret.push_back(item.first);
//     }
    
//     for (int i : ret) cout << i << endl;
// }

// 2. unique()

int main() {
    vector<int> v = {9,9,1,1,2,2,3,3,4,4,5,5};
    sort(v.begin(),v.end());

    auto it = unique(v.begin(),v.end());
    auto idx = it - v.begin();

    for (int i = 0; i < idx; i++) cout << v[i] << " ";
    cout << endl;

    v.erase(unique(v.begin(), v.end()), v.end());
    for (int i : v) cout << i << " ";
    
}