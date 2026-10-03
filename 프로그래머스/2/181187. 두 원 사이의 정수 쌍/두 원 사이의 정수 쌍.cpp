#include <bits/stdc++.h>
using namespace std;

long long solution(int r1, int r2) {
    // x축과 y축 위의 점
    long long answer = 4LL * (r2 - r1 + 1);

    long long outerY = r2;
    long long innerY = r1;

    for (long long x = 1; x <= r2; x++) {
        // 바깥 원 위의 점은 포함
        while (x * x + outerY * outerY > 1LL * r2 * r2) {
            outerY--;
        }

        // 안쪽 원의 '내부'만 제외하고, 원 위의 점은 남김
        while (innerY > 0 &&
               x * x + innerY * innerY >= 1LL * r1 * r1) {
            innerY--;
        }

        // x, y가 모두 양수인 점을 세고 네 사분면에 적용
        answer += 4LL * (outerY - innerY);
    }

    return answer;
}