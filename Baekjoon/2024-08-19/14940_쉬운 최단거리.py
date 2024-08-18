import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

queue = deque([])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            queue.append([i,j]) #좌표가 2인 타겟 좌표를 찾았다면, 큐에 넣기

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                queue.append([nx, ny])
                

bfs()

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 0:
            print(matrix[i][j], end=' ')
        else:
            print(matrix[i][j] - 2, end=' ')
    print()