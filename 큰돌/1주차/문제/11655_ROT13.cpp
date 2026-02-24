#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    getline(cin, s);

    for (char c : s) {
        if (islower(c)) {
            // 소문자 처리: 13을 더했을 때 'z'를 넘어가면 13을 빼줌
            if (c + 13 > 'z') c -= 13;
            else c += 13;
        } 
        else if (isupper(c)) {
            // 대문자 처리: 13을 더했을 때 'Z'를 넘어가면 13을 빼줌
            if (c + 13 > 'Z') c -= 13;
            else c += 13;
        }
        // 공백이나 숫자는 위 조건에 안 걸리므로 원래 값 그대로 출력됨
        cout << c;
    }

    return 0;
}