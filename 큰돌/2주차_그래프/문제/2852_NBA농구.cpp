#include <bits/stdc++.h>
using namespace std;

// 분:초 문자열을 정수(초)로 변환하는 함수
int to_second(string s) {
    int m = stoi(s.substr(0, 2));
    int sec = stoi(s.substr(3));
    return m * 60 + sec;
}

// 정수(초)를 00:00 포맷 문자열로 변환하는 함수
void print_time(int t) {
    printf("%02d:%02d\n", t / 60, t % 60);
}

int main() {
    int n, team, score1 = 0, score2 = 0;
    int sum1 = 0, sum2 = 0, last_time = 0;
    string goal_time;

    cin >> n;

    while (n--) {
        cin >> team >> goal_time;
        int curr_time = to_second(goal_time);

        // 1. 점수 업데이트 전: 지금까지 누가 이기고 있었는지 확인 후 시간 누적
        if (score1 > score2) sum1 += (curr_time - last_time);
        else if (score2 > score1) sum2 += (curr_time - last_time);

        // 2. 새로운 득점 반영
        if (team == 1) score1++;
        else score2++;

        // 3. 현재 시간을 기록하여 다음 정산의 기준점으로 삼음
        last_time = curr_time;
    }

    // 4. 경기가 끝나는 48:00(2880초)까지의 남은 시간 최종 정산
    if (score1 > score2) sum1 += (2880 - last_time);
    else if (score2 > score1) sum2 += (2880 - last_time);

    print_time(sum1);
    print_time(sum2);

    return 0;
}