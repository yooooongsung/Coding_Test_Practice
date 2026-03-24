#include <bits/stdc++.h>
using namespace std; 
int n, ans = -987654321;
string s;
vector<char> oper;
vector<int> num;

int operFunc(char a, int b, int c) {
    if(a == '+') return b + c;
    if(a == '-') return b - c;
    if(a == '*') return b * c;
}

void sol(int idx, int _num) {
    if(idx == num.size() - 1) {
        ans = max(ans, _num);
        return;
    }
    sol(idx + 1, operFunc(oper[idx], _num, num[idx + 1]));
    if(idx + 2 <= num.size() - 1) {
        int temp = operFunc(oper[idx + 1], num[idx + 1], num[idx + 2]);
        sol(idx + 2, operFunc(oper[idx], _num, temp));
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    cin >> n; cin >> s;
    
    for(int i = 0; i < n; i++) {
        if(i % 2 == 0) num.push_back(s[i] - '0');
        else oper.push_back(s[i]);
    }
    sol(0, num[0]);
    cout << ans;
    return 0;
}

/*
3. 이 유형을 정복하는 '치트키' 설계법
나중에 비슷한 문제를 만났을 때, 이렇게 설계 지도를 그려보세요.

상태(State) 정의: 재귀 함수 인자에 뭘 넘길 것인가? (보통 현재 인덱스, 지금까지의 합)

기저 사례(Base Case): 언제 멈출 것인가? (인덱스가 끝에 도달했을 때)

유효성 검사: 괄호를 칠 수 있는 상황인가? (idx + 2가 범위 내에 있는가?)

수식화: sol(다음 단계, 현재까지의 결과 ⚪ 다음 숫자)
*/