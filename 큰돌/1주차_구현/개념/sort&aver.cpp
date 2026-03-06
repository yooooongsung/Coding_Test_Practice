#include <bits/stdc++.h>
using namespace std;


int main() {
    int n, temp;
    double sum = 0;

    cin >> n;
    vector<int> arr(n);

    for(int i = 0; i < n; i++) {
        cin >> temp;
        sum += temp;
        arr[i] = temp;
    }
    sort(arr.begin(), arr.end());

    for(int i = 0; i < n; i++) cout << arr[i] << ' ';
    cout << endl;

    cout << fixed << setprecision(2) << sum / n << endl;
}