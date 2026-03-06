#include <bits/stdc++.h>
using namespace std;
string s;

bool isVowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    while(cin >> s && s != "end") {
        bool hasVowel = false;
        bool flag = true;
        int v_cnt = 0;
        int c_cnt = 0;

        for(int i = 0; i < s.size(); i++) {
            if(isVowel(s[i])) { // 모음이 있는지 체크
                hasVowel = true;
                v_cnt += 1;
                c_cnt = 0;
            }
            else {
                c_cnt += 1;
                v_cnt = 0;
            }

            if(c_cnt >= 3 || v_cnt >= 3) { // 실시간으로 자음 모음 3개 연속 막기
                flag = false;
                break;
            }
            if(i > 0 && s[i] == s[i-1]) { // 연속으로 같은 문자 막기
                if(s[i] != 'e' && s[i] != 'o') {
                    flag = false;
                    break;
                }
            } 
        }
        if(!hasVowel) flag = false;

        if(!flag) cout << "<" << s << "> is not acceptable." << "\n";
        else cout << "<" << s << "> is acceptable." << "\n";
    }
    return 0;
}