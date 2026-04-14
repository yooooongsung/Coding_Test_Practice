#include <string>
#include <vector>

using namespace std;
int solution(vector<vector<int>> signals) {
    int answer = 0;
    int n = signals.size();
    vector<int> total(n);
    vector<pair<int, int>> yel(n);
    for(int i = 0; i < n; i++) {
        int temp = signals[i][0] + signals[i][1] + signals[i][2]; // 전체 주기
        int start = signals[i][0] + 1;                            // 노란불 시작
        int end = signals[i][0] + signals[i][1];                  // 노란불 끝
        total[i] = temp;
        yel[i] = {start, end};
    }
    
    for(int time = 1; time < 2000000; time++) {
        bool all_yellow = true;
        for(int i = 0; i < n; i++) {
            int rem = time % total[i];
            if(rem == 0) rem = total[i];
            
            if(rem < yel[i].first || rem > yel[i].second) {
                all_yellow = false;
                break;
            }
        }
        if(all_yellow) return time;
    }
    return -1;
}