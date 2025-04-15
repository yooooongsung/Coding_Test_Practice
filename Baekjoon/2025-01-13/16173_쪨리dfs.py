import sys
input = sys.stdin.readline
n = int(input())
matrix = [list(map(int,input().strip().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n or visited[x][y] == 1: #범위를 벗어날 때 탈출조건
        return
    if matrix[x][y] == -1:
        visited[x][y] = True
        return
    visited[x][y] = True #방문처리
    dfs(x+matrix[x][y],y) #밑부터 ㄱㄱ
    dfs(x,y+matrix[x][y]) #리턴 생기면 오른쪽 ㄱㄱ

dfs(0,0)

if visited[-1][-1]:
    print('HaruHaru')
else:
    print('Hing')