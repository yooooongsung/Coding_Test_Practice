#include <string>
#include <vector>
#include <iostream>
#include <cctype>

using namespace std;

string solution(string s) {
    string answer = "";
    vector<string> v; // 문자열 공백 기준 파싱 값을 저장하는 벡터
    string temp = "";
    for (int i = 0; i < s.size(); i++) {
        temp += s[i];
        if (s[i] == ' ') {
            if (isalpha(temp[0])) {
                temp[0] = toupper(temp[0]);
                for (int j = 1; j < temp.size(); j++) {
                    temp[j] = tolower(temp[j]);
                }
            }
            else {
                for (int j = 1; j < temp.size(); j++) {
                    temp[j] = tolower(temp[j]);
                }
            }
            answer += temp;
            temp = "";
        }
    }
    temp[0] = toupper(temp[0]);
    for (int j = 1; j < temp.size(); j++) {
        temp[j] = tolower(temp[j]);
    }
    answer += temp;
    return answer;
}