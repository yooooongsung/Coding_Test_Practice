import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

distances = [[-1] * m for _ in range(n)]
q = deque()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            q.append([i,j])
            distances[i][j] = 0

while q:
    x,y = q.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and distances[nx][ny] == -1:
            distances[nx][ny] = distances[x][y] + 1
            q.append([nx,ny])
                    


print(max(map(max,distances)))

