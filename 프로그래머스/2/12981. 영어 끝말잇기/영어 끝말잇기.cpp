#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(int n, vector<string> words) {
    vector<int> answer;
    vector<string> stack;
    for (int i=0;i<words.size();i++) {
        if (find(stack.begin(),stack.end(),words[i]) != stack.end()) {
            int num = stack.size() % n + 1;
            int turn = stack.size() / n + 1;
            return {num,turn};
        }
        if (!stack.empty() and words[i][0] != stack.back().back()) {
            int num = stack.size() % n + 1;
            int turn = stack.size() / n + 1;
            return {num,turn};
        }
        stack.push_back(words[i]);
    }
    
    return {0,0};
}