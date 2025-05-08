#include <string>
#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std;

string to_bin(int n) {
    string bin = "";
    while(n > 0) {
        bin = to_string(n % 2) + bin;
        n = n / 2;
    }
    return bin;
}


int solution(int n) {
    string before = to_bin(n);  // n 2진수 문자열 변환
    string next = ""; // 다음 숫자의 2진수 문자열 초기화
    int ne_cnt; // 다음 숫자의 2진수 문자열 중 1의 갯수 카운트 변수 초기화
    int be_cnt = count(before.begin(), before.end(), '1'); // count함수로 n의 1의 갯수 카운트
    while(be_cnt != ne_cnt) {
        n += 1;
        next = to_bin(n);
        ne_cnt = count(next.begin(), next.end(), '1');
    }
    
    return n;
}