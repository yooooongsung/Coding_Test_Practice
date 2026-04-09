#include <bits/stdc++.h>
using namespace std;

int solution(vector<string> want, vector<int> number, vector<string> discount) {
    int answer = 0;
    if(want.size() > discount.size()) return 0;
    int cnt = 0;
    
    for(int i : number) cnt += i;
    
    map<string, int> want_map;
    for(int i = 0; i < want.size(); i++) {
        want_map[want[i]] = number[i];
    }

    int k = 0;
    
    while(k <= discount.size() - cnt) {
        map<string, int> discount_map;
        for(int i = k; i < cnt + k; i++) {
            discount_map[discount[i]]++;
        }
        if(want_map == discount_map) answer++;
        k++;
    }
    return answer;
}