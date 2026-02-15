#include <bits/stdc++.h>
using namespace std;

int main() {
    vector<int> v = {2, 1, 3, 20, 10, 50};
    int count = 0;
    sort(v.begin(), v.end());
    do{
        for(int i = 0; i < 2; i++) {
            cout << v[i] << " ";
        }
        cout << endl;
        count += 1;
    }while(next_permutation(v.begin(), v.end()));
    cout << count << endl;
}