#include <bits/stdc++.h>
using namespace std; 
int n; 
string pt;
string head, rear;
int flag;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n;
    cin >> pt;
    for(char c : pt) {
        if(flag == 1) {
            rear += c;
            continue;
        }
        if(c == '*') {
            flag = 1;
            continue;
        }
        head += c;
    }
    for(int i = 0; i < n; i++) {
        string s; cin >> s;
        if(s.size() < head.size() + rear.size()) {
            cout << "NE" << "\n";
            continue;
        }
        string temp_h = s.substr(0, head.size());
        string temp_r = s.substr(s.size() - rear.size());
        if(head == temp_h && rear == temp_r) cout << "DA" << "\n";
        else cout << "NE" << "\n";
    }

    return 0;
}