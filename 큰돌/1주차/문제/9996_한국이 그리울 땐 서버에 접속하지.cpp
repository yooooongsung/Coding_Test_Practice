#include <bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;

    string s, ip;
    cin >> s;

    int pos = s.find('*');
    string head = s.substr(0, pos);
    string rear = s.substr(pos+1);


    for(int i = 0; i < n; i++) {
        cin >> ip;
        if(ip.length() < head.length() + rear.length()) 
        {
            cout << "NE" << endl;
            continue;
        }
        string t1 = ip.substr(0,head.length());
        string t2 = ip.substr(ip.length()-rear.length());

        if(t1 == head && t2 == rear) cout << "DA" << endl;
        else cout << "NE" << endl;

    }
    return 0;
}