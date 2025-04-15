import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int,input().strip().split())) for _ in range(n)]
dx = [1,0] #아래쪽
dy = [0,1] #오른쪽
visited = [[False] * n  for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append([x,y])

    while q:
        x,y = q.popleft()
        step = matrix[x][y]

        if matrix[x][y] == -1:
            return True
        
        for i in range(2):
            nx = x+dx[i]*step
            ny = y+dy[i]*step

            if 0 <= nx < n and 0 <= ny < n:
                q.append([nx,ny])
                visited[nx][ny] = True
            else:
                continue

if bfs(0,0):
    print('HaruHaru')
else:
    print('Hing')
