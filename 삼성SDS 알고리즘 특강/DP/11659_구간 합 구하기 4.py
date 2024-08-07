import sys
n, m = map(int,input().split())
num = list(map(int,input().split()))
dp = [0] * n
dp[0] = num[0]
dp[1] = num[0] + num[1]

for i in range(2,n):
    dp[i] = dp[i-1] + num[i]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    if a == 1:
        print(dp[b-1])
    elif a == b:
        print(num[b-1])
    else:
        print(dp[b-1] - dp[a-2])
    
