#include <bits/stdc++.h>
using namespace std;

vector<string> split(const string & input, string delimiter) {
    vector<string> result;
    auto start = 0;
    auto end = input.find(delimiter);
    while(end != string::npos) {
        result.push_back(input.substr(start, end - start));
        start = end + delimiter.size();
        end = input.find(delimiter, start);
    }
    result.push_back(input.substr(start));
    return result;
}

int main() {
    string str = "apple->banana->orange->grape"; 
    vector<string> fruits = split(str,"->");
    for (const string& fruit : fruits) {
        cout << fruit << " ";
    }
}


// find(찾을 값, 탐색 시작 인덱스)
// substr(시작 인덱스, 잘라낼 길이)
// substr(시작 인덱스) 만 있다면 시작 인덱스부터 끝까지 잘라내기