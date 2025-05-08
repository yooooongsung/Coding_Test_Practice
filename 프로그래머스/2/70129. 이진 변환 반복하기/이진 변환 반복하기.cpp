#include <string>
#include <vector>
#include <algorithm>
using namespace std;

vector<int> to_bin(string s, int bin_cnt, int zero_cnt) {

    if (s == "1") return vector<int> {bin_cnt, zero_cnt}; // 벡터로 반환
    int x;
    
    int zeros = count(s.begin(), s.end(), '0'); // 0 갯수 세기
    zero_cnt += zeros;
    
    s.erase(remove(s.begin(), s.end(),'0'),s.end()); // 0 삭제
    
    x = s.size();
    string binary = "";
    while(x > 0) {
        binary = to_string(x % 2) + binary;
        x /= 2;
    }
    bin_cnt++;
    return to_bin(binary,bin_cnt,zero_cnt);
}

vector<int> solution(string s) {
    vector<int> answer;
    return to_bin(s,0,0);
    
}

        
        
        
