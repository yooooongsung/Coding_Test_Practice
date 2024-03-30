def dfs(ax,ay,bx,by,cnt):
    global answer
    if cnt == 6: # 움직임이 4번일 때(초기 위치 포함)
        answer = max(answer, visited_sum())
        return

    for i in range(4):
        nax = dx[i] + ax
        nay = dy[i] + ay
        if 0 <= nax < n and 0 <= nay < n and not visited[nax][nay]:
            visited[nax][nay] = True
            dfs(nax, nay, bx, by, cnt+1)
            visited[nax][nay] = False

    for i in range(4):
        nbx = dx[i] + bx
        nby = dy[i] + by
        if 0 <= nbx < n and 0 <= nby < n and not visited[nbx][nby]:
            visited[nbx][nby] = True
            dfs(ax, ay, nbx, nby, cnt+1)
            visited[nbx][nby] = False

def visited_sum():
    total = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                total += matrix[i][j]
    return total

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
ax, ay = map(int,input().split())
bx, by = map(int,input().split())
visited = [[False] * n for _ in range(n)]
dx = [0,0,-1,1]
dy = [1,-1,0,0]

answer = 0
visited[ax-1][ay-1] = True
visited[bx-1][by-1] = True
dfs(ax-1, ay-1, bx-1, by-1, 0)
print(answer)
