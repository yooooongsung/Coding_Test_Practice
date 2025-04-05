#include <iostream>
#include <stack>
#include <iomanip>
using namespace std;

int main() {
    int n;
    cin >> n;

    string notation;
    cin >> notation;

    double values[26];
    for (int i=0; i < n; i++) {
        cin >> values[i];
    }
    
    stack<double> stack; // c++ stack 선언언

    for (char ch : notation) {
        if ('A' <= ch && ch <= 'Z') {
            int idx = ch - 'A';
            stack.push(values[idx]);
        }
        else {
            double a = stack.top(); stack.pop(); // c++ stack 사용법 
            double b = stack.top(); stack.pop();
            double result = 0;

            if (ch == '+') result = b + a;
            else if (ch == '-') result = b - a;
            else if (ch == '*') result = b * a;
            else if (ch == '/') result = b / a;

            stack.push(result);
        }
    }
    cout << fixed << setprecision(2) << stack.top(); // c++ 자릿수 고정 출력력
    return 0;
}