#include <bits/stdc++.h>

using namespace std;

int solution(int n, vector<vector<int>> q, vector<int> ans) {
    vector<vector<int>> results;
    int answer = 0;
    for(int a = 1; a <= n - 4; a++) {
        for(int b = a + 1; b <= n - 3; b++) {
            for(int c = b + 1; c <= n - 2; c++) {
                for(int d = c + 1; d <= n - 1; d++) {
                    for(int e = d + 1; e <= n; e++) {
                        int comb[5] = {a, b, c, d, e};
                        bool check = true;
                        for(int i = 0; i < q.size(); i++) {
                            int hit = 0;
                            for(int j = 0; j < 5; j++) {
                                for(int k = 0; k < 5; k++) {
                                    if(comb[k] == q[i][j]) hit++;
                                }
                            }
                            if(hit != ans[i]) check = false;
                        }
                        if(check == true) answer++;
                    }
                }
            }
        }
    }
    return answer;
}