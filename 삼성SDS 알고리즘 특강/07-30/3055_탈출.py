from collections import deque
r , c = map(int,input().split())
matrix = [list(input().strip()) for _ in range(r)]
visited = [[-1] * c for _ in range(r)] 
#-1로 visited를 초기화한 이유 : 방문 체크, 시간 저장 용도 (고슴이의 첫 위치는 0으로 바꾸고, 1씩 증가시킬 것)
q = deque([])
dx = [-1,1,0,0] 
dy = [0,0,-1,1] 

for i in range(r):
    for j in range(c):
        if matrix[i][j] == 'S':
            q.append([i,j]) #고슴이는 나중에 이동
            visited[i][j] = 0 #출발 시 0으로 초기화 (시간이 될 것임)
        elif matrix[i][j] == '*':
            q.appendleft([i,j]) #물 먼저 앞에 넣기
        elif matrix[i][j] == 'D':
            a,b = i,j
            
while q:
    x, y = q.popleft()
    current = matrix[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= r or ny < 0 or ny >= c: #범위 밖 무시
            continue 
        if visited[nx][ny] != -1: #다음이 방문한 곳 무시
            continue
        if matrix[nx][ny] == 'X': #다음이 돌이면 무시
            continue
        if matrix[nx][ny] == '*': #다음이 물이면 무시
            continue
        if current == '*' and matrix[nx][ny] == 'D': #물이 비버네 가는거 무시
            continue 
        if current == 'S':
            visited[nx][ny] = visited[x][y] + 1
        elif current == 'S' and matrix[nx][ny] == 'D':
            break
        
        matrix[nx][ny] = current #현재 고슴 or 물을 다음 좌표에 표시
        q.append([nx,ny])
        
if visited[a][b] != -1:
    print(visited[a][b])
else:
    print('KAKTUS')