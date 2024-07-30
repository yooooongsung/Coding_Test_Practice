#DFS
#갈 수 있는 범위 내에서 더 작은 수를 택 >> 배열에 저장 후 min값 이용
#더 이상 갈 곳이 없다면 +1 하고 출력
# >>> 틀렸음.
import sys
sys.setrecursionlimit(10**6)
def dfs(x, y, cnt):
    global answer
    answer = max(answer, cnt)
    for i in range(4):
        nx = x + int(matrix[x][y]) * dx[i]
        ny = y + int(matrix[x][y]) * dy[i]
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] != 'H' and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt+1
                visited[nx][ny] = True
                dfs(nx, ny, cnt+1)
                visited[nx][ny] = False
    
n, m = map(int,input().split(' '))

matrix = []

for _ in range(n):
    x = list(input().strip())
    matrix.append(x)
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False] * m  for _ in range(n)]

dp = [[0] * m for _ in range(n)]

answer = 0

dfs(0,0,0)

print(answer+1)



