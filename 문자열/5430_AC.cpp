#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <deque>
using namespace std;

deque<int> string_to_arr(string &s) {
    deque<int> result;
    if (s == "[]") return result;

    s = s.substr(1,s.size()-2);
    stringstream ss(s);

    string token;
    while(getline(ss,token,',')) {
        result.push_back(stoi(token));
    }

    return result;
}

int main() {
    int t;
    cin >> t;

    for(int i = 0; i < t; i++) {
        string func;
        cin >> func;
        
        int n;
        cin >> n;
        string s;
        cin >> s;

        deque<int> arr = string_to_arr(s);
        bool reverse = false;
        int error = 0;

        for (char f : func) {
            if (f == 'R') {
                reverse = !reverse;
            }
            else if (f == 'D') {
                if (arr.empty()) {
                    error = 1;
                    break;
                }
                if (reverse) arr.pop_back();
                else arr.pop_front();
            }
        }
        if (error) cout << "error" << endl;
        else if (reverse) {
            cout << "[";
            for (int j = arr.size()-1; j >=0; j--) {
                cout << to_string(arr[j]);
                if (j != 0) cout << ",";
            }
            cout << "]" << endl;;
        }
        else if (!reverse) {
            cout << "[";
            for (int j = 0; j < arr.size(); j++) {
                cout << to_string(arr[j]);
                if (j != arr.size()-1) cout << ",";
            }
            cout << "]" << endl;
        }
    }
    return 0;
}