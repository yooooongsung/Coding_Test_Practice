#include <bits/stdc++.h>
using namespace std;

int main() {
    int a[3] = {1,7,13};
    int* c = a;

    cout << c << endl;
    cout << &a[0] << endl;
    cout << &a << endl;
    cout << endl;

    cout << c + 1 << endl;
    cout << &a[1] << endl;
    cout << endl;

    cout << *c << endl;
    cout << *(c + 1) << endl;
    cout << a[1] << endl;
}