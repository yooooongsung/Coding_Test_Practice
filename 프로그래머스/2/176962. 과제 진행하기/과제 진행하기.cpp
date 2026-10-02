#include <bits/stdc++.h>

using namespace std;

vector<string> solution(vector<vector<string>> plans) {
    vector<string> answer;
    deque<vector<string>> stck;

    sort(plans.begin(), plans.end(),
         [](const vector<string>& a, const vector<string>& b) {
             return a[1] < b[1];
         });

    for (int i = 0; i < plans.size(); i++) {
        int hour = 60 * stoi(plans[i][1].substr(0, 2));
        int minute = stoi(plans[i][1].substr(3, 2));
        int start = hour + minute;
        int playtime = stoi(plans[i][2]);

        // 마지막 과제는 다음 시작 시각이 없으므로 끝까지 진행
        if (i == plans.size() - 1) {
            answer.push_back(plans[i][0]);
            break;
        }

        int next_hour = 60 * stoi(plans[i + 1][1].substr(0, 2));
        int next_minute = stoi(plans[i + 1][1].substr(3, 2));
        int gap = next_hour + next_minute - start;

        // 다음 과제 시작 전까지 끝내지 못한 경우
        if (playtime > gap) {
            stck.push_back({plans[i][0], to_string(playtime - gap)});
            continue;
        }

        // 현재 과제를 끝낸 경우
        answer.push_back(plans[i][0]);
        gap -= playtime;

        // 다음 과제까지 남은 시간에 멈춰 둔 과제 진행
        while (gap > 0 && !stck.empty()) {
            int remaining = stoi(stck.back()[1]);

            if (remaining <= gap) {
                gap -= remaining;
                answer.push_back(stck.back()[0]);
                stck.pop_back();
            } else {
                stck.back()[1] = to_string(remaining - gap);
                gap = 0;
            }
        }
    }

    // 모든 새 과제를 시작한 뒤에는 멈춘 과제를 역순으로 완료
    while (!stck.empty()) {
        answer.push_back(stck.back()[0]);
        stck.pop_back();
    }

    return answer;
}