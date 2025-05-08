#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <deque>
using namespace std;

string solution(string number, int k) {
    string answer = "";
    deque<int> n;
    deque<int> temp;
    
    for (char c : number) {
        int a = c-'0';
        n.push_back(a);
    }
    while (k > 0 and n.size() >= 2) { // k > 0
        if (n[0] < n[1]) { // n.size() >= 2
            n.pop_front();
            k -= 1;
            
            while(!temp.empty() and k > 0 and temp.back() < n.front()) { // k > 0
                temp.pop_back();                            
                k -= 1; // k = 2
            }
        }
        else {
            temp.push_back(n.front());
            n.pop_front();
        }
            
    }
        // 남은 temp를 앞에 붙이기
    while (!temp.empty()) {
        n.push_front(temp.back());
        temp.pop_back();
    }

    // 만약 아직도 k가 남아 있으면 뒤에서 제거
    while (k > 0 && !n.empty()) {
        n.pop_back();
        k--;
    }
        
    for (int i : n) answer = answer + (char)(i + '0');
    return answer;    
}


// deque 풀이
// while (k > 0 and n.size() >= 2) { // k > 0
//         if (n[0] < n[1]) { // n.size() >= 2
//             n.pop_front();
//             k -= 1;
            
//             while(!temp.empty() and k > 0 and temp.back() < n.front()) { // k > 0
//                 temp.pop_back();                            
//                 k -= 1; // k = 2
//             }
//             }
//         else {
//             temp.push_back(n.front());
//             n.pop_front();
//         }
            
//     }
//         // 남은 temp를 앞에 붙이기
//     while (!temp.empty()) {
//         n.push_front(temp.back());
//         temp.pop_back();
//     }

//     // 만약 아직도 k가 남아 있으면 뒤에서 제거
//     while (k > 0 && !n.empty()) {
//         n.pop_back();
//         k--;
//     }