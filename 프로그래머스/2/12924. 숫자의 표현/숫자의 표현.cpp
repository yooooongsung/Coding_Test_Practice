#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int temp = 1;
    int start = 1;
    int cnt = 0;
    while(temp <= n){
        cnt += temp;
        temp += 1;
        
        if (cnt == n) {
            answer = answer + 1;
            cnt = 0;
            start = start + 1;
            temp = start;
        } 
            
        if (cnt > n) {
            cnt = 0;
            start += 1;
            temp = start;
        }
            
    }
    return answer;
}