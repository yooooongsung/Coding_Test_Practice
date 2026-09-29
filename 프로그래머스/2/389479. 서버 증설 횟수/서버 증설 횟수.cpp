#include <bits/stdc++.h>
using namespace std;

int solution(vector<int> players, int m, int k) {
    vector<int> added(24, 0); // 각 시각에 증설한 서버 수
    int active = 0;           // 현재 운영 중인 서버 수
    int answer = 0;

    for (int i = 0; i < 24; i++) {
        // k시간 전에 증설한 서버는 이 시각부터 운영하지 않음
        if (i >= k) {
            active -= added[i - k];
        }

        int n = players[i] / m;

        if (active < n) {
            int newServers = n - active;
            added[i] = newServers;
            active += newServers;
            answer += newServers;
        }
    }

    return answer;
}