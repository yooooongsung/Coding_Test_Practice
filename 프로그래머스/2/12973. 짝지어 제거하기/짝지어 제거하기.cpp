#include <iostream>
#include<string>
#include<vector>
#include <algorithm>
using namespace std;

int solution(string s)
{
    vector<char> temp;
    for (int i=0;i<s.size();i++) {
        temp.push_back(s[i]);
        if (temp.size() >= 2 and temp[temp.size() - 1] == temp[temp.size() - 2]) {
            temp.pop_back();
            temp.pop_back();
        }
    }

    if (temp.empty()) return 1;
    else return 0;
}
