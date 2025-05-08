#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int solution(vector<int> people, int limit) {
    int answer = 0;
    sort(people.begin(),people.end());
    int left = 0;
    int right = people.size() - 1;
    while (left <= right) {
        if (people[right] + people[left] <= limit) { // 젤 무거운 사람이 보트에 탈 수 있으면
            left++;
            right--;
        }
        else right--;
        answer++;
    }
    return answer;
}