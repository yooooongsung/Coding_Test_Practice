import sys
sys.setrecursionlimit(10000)
def dfs_m1(r,c):

    visited[r][c] = True
    focus = m1[r][c]
    for k in range(4):
        nr = dr[k] + r
        nc = dc[k] + c
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
            if m1[nr][nc] == focus:
                dfs_m1(nr,nc)

def dfs_m2(r,c):

    visited[r][c] = True
    focus = m2[r][c]
    for k in range(4):
        nr = dr[k] + r
        nc = dc[k] + c
        if 0 <= nr < n and 0 <= nc < n and visited[nr][nc] == False:
            if m2[nr][nc] == focus:
                dfs_m2(nr,nc)


n = int(input())
m1 = [list(input()) for _ in range(n)]

visited = [[False] * n for _ in range(n)]
dr = [-1,1,0,0]
dc = [0,0,-1,1]

cnt_m1 = 0
cnt_m2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs_m1(i,j)
            cnt_m1 += 1
m2 = m1

for i in range(n):
    for j in range(n):
        if m2[i][j] == 'R':
            m2[i][j] = 'G'
        visited[i][j] = False

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs_m2(i,j)
            cnt_m2 += 1


print(cnt_m1, cnt_m2)
