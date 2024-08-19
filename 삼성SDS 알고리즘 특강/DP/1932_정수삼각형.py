n = int(input())
t = [list(map(int,input().split())) for _ in range(n)]

for i in range(1,n):
    x = len(t[i])
    for j in range(x):
        if j == 0:
            t[i][j] = t[i-1][j] + t[i][j]
        elif j == x - 1:
            t[i][j] = t[i-1][j-1] + t[i][j]
        else:
            t[i][j] = max(t[i-1][j-1], t[i-1][j]) + t[i][j] 

print(max(t[n-1]))