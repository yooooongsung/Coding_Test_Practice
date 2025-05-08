#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <iostream>
using namespace std;

int solution(int k, vector<int> tangerine) {
    
    unordered_map<int, int> countMap;
    for (int i : tangerine) {
        countMap[i]++;
    }
    
    vector<int> cnt;
    for (auto &pair : countMap) {
        cnt.push_back(pair.second);
    }
    
    sort(cnt.rbegin(),cnt.rend());
    
    int sum = 0;
    int answer = 0;
    for(int i : cnt) {
        if (sum >= k) break;
        sum += i;
        answer++;
    }
    
    return answer;
}