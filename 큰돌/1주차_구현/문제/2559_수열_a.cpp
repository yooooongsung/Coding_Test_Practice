#include <bits/stdc++.h>
using namespace std;
int main() {
    int n,k;
    cin >> n >> k;
    int arr[n];
    for(int i = 0; i < n; i++) {
        int ip;
        cin >> ip;
        arr[i] = ip;
    }
    vector<int> res;
    for(int i = 0; i <= n-k; i++) {
        int temp = 0;
        for(int j = i; j < i + k; j++) {
            temp += arr[j];
        }
        res.push_back(temp);
    }
    cout << *max_element(res.begin(), res.end());
    return 0;
}