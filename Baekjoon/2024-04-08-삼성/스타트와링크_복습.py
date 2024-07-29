import sys
n = int(input())
m = [list(map(int,input().split())) for _ in range(n)]
visited = [False] * n
ans = sys.maxsize

def backTracking(depth, idx):
    global ans
    if depth == n // 2:
        start = 0
        link = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]: #True인 팀이 start
                    start += m[i][j]
                elif not visited[i] and not visited[j]:
                    link += m[i][j]
        ans = min(ans,abs(start-link))
        return

            
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            backTracking(depth+1,idx+1)
            visited[i] = False

backTracking(0,0)
print(ans)
