#include <bits/stdc++.h>
using namespace std;

int main () {
    string dopa = "umzunsik";

    // Q1 : substr
    string q1 = dopa.substr(0,3);
    cout << q1 << endl;

    // Q2-1 : for
    for(int i = q1.size()-1; i >= 0; i--) cout << q1[i];
    cout << endl;

    // Q2-2 : reverse
    reverse(q1.begin(), q1.end());
    cout << q1 << endl;

    // Q3-1 : +
    string q3 = dopa + "umzunsik";
    cout << q3 << endl;

    // Q3-1 : insert
    string q4 = dopa.insert(dopa.size(),"umzunsik");
    cout << q4 << endl;

    

}