#include <string>
#include <vector>
#include <iostream>
#include <unordered_map>

using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;

    unordered_map<string, int> want_number; //비정렬 맵, unordered_map 사용, map도 사용법 똑같음
    for (int i = 0; i < number.size(); i++) {
        want_number[want[i]] = number[i];                                   
    }
    
    for (int i = 0; i <= discount.size() - 10; i++) {
        unordered_map<string,int> discount_count;
        for (int j = i; j < i + 10; j++) {
            discount_count[discount[j]]++;
        }
        
        bool valid = true;
        for(const auto &pair : want_number) {
            if (discount_count[pair.first] < pair.second) {
                valid = false;
                break;
            } 
        }
        if (valid) answer++;
    }
    return answer;
}