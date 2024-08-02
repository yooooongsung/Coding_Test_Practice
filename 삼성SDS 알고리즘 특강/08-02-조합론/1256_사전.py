import sys
n,m,k = map(int,sys.stdin.readline().split())

dp = [[1]*(m+1) for _ in range(n+1)] #3x3 dp 만들기

for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] #dp[i-1][j] >> n개의 a와, m개의 z로 만들 수 있는 경우의 수

if dp[n][m] < k: #만약 모든 경우의 수가 k값보다 작을 때 에러
    print(-1)
else:
    ans = ''
    while True:
        if n == 0 or m == 0 : #while문 탈출조건
            #a나 z로만 이루어져 있거나, 혹은 n과 m 중 하나를 소진시, 나머지 부분을 채워준다
            ans += 'a' * n
            ans += 'z' * m
            break
        flag = dp[n-1][m] #해당 좌표값을 기준으로 몇 번째인지 판별
        if flag >= k: #찾고자 하는 k번째가 flag보다 작다면 >> a로 시작한다면
            ans += 'a'
            n -= 1
        else:
            ans += 'z'
            m -= 1
            k -= flag
    print(ans)
            