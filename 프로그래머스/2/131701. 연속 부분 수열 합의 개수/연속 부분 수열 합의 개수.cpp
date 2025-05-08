#include <string>
#include <vector>
#include <set> //코테에서 만약 헤더를 건드리지 말라고 한다면, 어쩔 수 없이 vector find를 쓰거나, visited를 쓴다.
#include <iostream>
using namespace std;

int solution(vector<int> arr) {
    vector<int> circle;
    for (int i = 0; i <  2; i++) { // 배열 이어 붙이기
        for (int j : arr) {
            circle.push_back(j);
        }
    }
    
    set<int> answer;
    
    int left = 0;
    int right = 0;
    int n = 0;
    int cnt = 0;
    
    while (n != arr.size()) {
        for (int i = 0; i < arr.size(); i++) {
            for (int j = left; j <= right; j++) {
                cnt += circle[j];
            }
            left++;
            right++;
            answer.insert(cnt);
            cnt = 0;
        }
        n += 1;
        right = n;
        left = 0;
    }
    
    return answer.size();
}