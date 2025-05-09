#include <string>
#include <vector>

using namespace std;

long long solution(int n) {
    long long answer = 0;
    if (n==1) return 1;
    else {
        vector<int> dp(n+1,0);
        dp[1] = 1;
        dp[2] = 2;
        for (int i=3;i<n+1;i++) {
            dp[i] = (dp[i-1] + dp[i-2]) % 1234567;
        }
        return dp[n];
    }
    
}