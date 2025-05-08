def solution(n):
    answer = 0
    m = 123456789
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    return dp[n] 

# def solution(n):
#     m = 123456789
#     a, b = 0, 1  # fib(0), fib(1)
#     for _ in range(2, n + 1):
#         a, b = b, (a + b) % m
#     return b