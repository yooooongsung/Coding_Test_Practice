from collections import deque
def bfs(x,y,current): #1~real_max 사이의 (i) 값보다 큰 좌표와 그 i 값을 매개변수로 받음
    deq = deque() 
    deq.append((x,y)) #우선 데크에 좌표 둘은 넣음. 왜냐면 얘네는 이미 메인에서 조건을 만족한 애들임. 그리고 조만간 얘네를 기준으로 작업단위별로 검사진행할겨
    visited[x][y] = True #그리고 방문했다고 체크

    while deq: #데크가 비어있을 때까지 반복
        x, y = deq.popleft() #우선 처음에 조건을 만족했던 좌표를 팝시킴
 
        for i in range(4): #그리고 작업단위 반복 (매개변수로 받은 좌표 기준으로 상하좌우)
            nx = dx[i] + x 
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n: #만약 상하좌우 값들이 격자의 범위를 벗어나지 않을때
                if m[nx][ny] > current and visited[nx][ny] == False: #그 상하좌우의 좌표값이 비교값current보다 크고, 방문한 적이 없다면
                    visited[nx][ny] = True #방문체크하고
                    deq.append((nx,ny)) #데크에 넣음


n = int(input()) 
m = [list(map(int, input().split())) for _ in range(n)] #격자

maximum = []
for i in range(n):
    maximum.append(max(m[i]))
real_max = max(maximum) #격자 중에서 가장 큰 값을 구함

dx = [0,0,-1,1] #이동단위 설정
dy = [1,-1,0,0]

answer = []

for i in range(1,real_max): #1부터 가장 높은 높이 값까지 검사
    cnt = 0
    visited = [[False] * n for _ in range(n)] #2차원 방문대장
    for j in range(n):
        for k in range(n):
            if m[j][k] > i and visited[j][k] == False: #격자의 좌표값이 1~real_max값보다 크고, 방문한 적이 없을때
                bfs(j,k,i) #bfs 호출
                cnt += 1 #bfs가 끝나고 나면 안전지대의 갯수를 카운트
    answer.append(cnt)

print(max(answer)) #1~real_max값을 비교하며 생긴 안전지대중에서 가장 큰 값을 출력

#https://whitehairhan.tistory.com/332