#include <bits/stdc++.h>

using namespace std;
string res;
void dfs(vector<vector<int>> &arr, int n, int y, int x) {
    int value = arr[y][x];
    for(int i = y; i < y + n; i++) {
        for(int j = x; j < x + n; j++) {
            if(value != arr[i][j]) {
                res += '(';
                dfs(arr, n / 2, y, x);
                dfs(arr, n / 2, y, x + n / 2);
                dfs(arr, n / 2, y + n / 2, x);
                dfs(arr, n / 2, y + n / 2, x + n / 2);
                res += ')';
                return;
            }
        }
    }
    res += to_string(value);
}

vector<int> solution(vector<vector<int>> arr) {
    vector<int> answer;
    dfs(arr, arr.size(), 0, 0);
    int zero = 0;
    int one = 0;
    for(char c : res) {
        if(c == '0') zero++;
        else if(c == '1') one++;
    }
    answer.push_back(zero);
    answer.push_back(one);
    return answer;
}