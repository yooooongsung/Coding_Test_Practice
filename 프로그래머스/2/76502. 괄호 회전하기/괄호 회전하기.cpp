#include <string>
#include <vector>

using namespace std;

int solution(string s) {
    int answer = 0;
    int turn = 0;
    while (turn != s.size()) {
        bool valid = true;
        vector<char> stack;
        for (char c : s) {
            if (c == '[' or c == '{' or c == '(') {
                stack.push_back(c);
            }
            else {
                if (stack.empty()) {
                    valid = false;
                    break;
                }
                if (stack.back() == '[' and c == ']') stack.pop_back();
                else if (stack.back() == '{' and c == '}') stack.pop_back();
                else if (stack.back() == '(' and c == ')') stack.pop_back();
                else {
                    valid = false;
                    break;
                }
            }
        }
        if (valid and stack.empty()) answer += 1;
        
        turn += 1;
        s = s.substr(1) + s[0];
    }
    return answer;
}