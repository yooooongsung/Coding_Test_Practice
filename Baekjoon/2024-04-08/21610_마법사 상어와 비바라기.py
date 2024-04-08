n, m = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]
moves = [tuple(map(int,input().split())) for _ in range(m)]

#8 direction
dr8 = ['',0,-1,-1,-1,0,1,1,1]
dc8 = ['',-1,-1,0,1,1,1,0,-1]

dr4 = [-1,-1,1,1]
dc4 = [-1,1,-1,1]

clouds = [(n-1,0),(n-1,1),(n-2,0),(n-2,1)] #구름좌표

for d, s in moves:#움직임 정보 하나에 따라서 1) 이동 후 물의 양 추가 2) 대각 4방향 검사 후 물 추가 3) 다음 구름 좌표 넣어주기
    moved_clouds = []

    for r, c in clouds:
        nr = (r + dr8[d] * s) % n
        nc = (c + dc8[d] * s) % n
        matrix[nr][nc] += 1
        moved_clouds.append((nr,nc)) #이동한 구름좌표에 추가

    for r, c in moved_clouds: #이동을 마친 구름대상 대각 4방향 조사
        cnt = 0
        for i in range(4):
            nr = r + dr4[i]
            nc = c + dc4[i]
            if 0 <= nr < n and 0 <= nc < n:
                if matrix[nr][nc] > 0:
                    cnt += 1
        matrix[r][c] += cnt #이동을 마친 구름 좌표에 4방향 대각선 검사 값을 더해줌
    
    new_clouds = []
    for r in range(n):
        for c in range(n):
            if (r,c) in moved_clouds or matrix[r][c] < 2: #이동완료한 구름이거나 좌표 값이 2보다 작으면 패스
                continue
            matrix[r][c] -= 2 #이동한 구름 좌표가 아니고, 2 이상이면 좌표값 -2
            new_clouds.append((r,c)) #그리고 그 좌표값을 새로운 구름배열로 추가
    clouds = new_clouds

answer = 0
for r in range(n):
    for c in range(n):
        answer += matrix[r][c]
print(answer)