#include <bits/stdc++.h>
using namespace std;

int i;
int main() {
    // 1. memory
    // cout << &i << endl;
    // i = 0;
    // cout << &i << endl;

    // 2. pointer
    // type * 변수명 = 해당 타입의 변수의 주소
    // pointer 
    int a = 4;
    int* b = &a;
    
    double c = 4.7;
    double* d = &c;

    cout << sizeof(a) << endl;
    cout << sizeof(b) << endl;
    cout << sizeof(c) << endl;
    cout << sizeof(d) << endl;


    cout << &a << endl;
    cout << &b << endl;

    cout << &c << endl;
    cout << &d << endl;

    cout << b << endl;
    cout << *b << endl;

    cout << d << endl;
    cout << *d << endl;
    
}

