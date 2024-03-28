n = int(input())
m1 = [list(input()) for _ in range(n)]
m2 = [list(input()) for _ in range(n)]
mine_exploded = False
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

for i in range(n):
    for j in range(n): 
        if m1[i][j] == '*' and m2[i][j] == 'x': #지뢰가 있는 칸이 열려있는 칸이라면
           mine_exploded = True #지뢰터짐 

if mine_exploded: #지뢰가 터졌다면 모든 지뢰위치를 표시해줘야함 문제를 개같이 써놔서 이해를 못했네
    for i in range(n):
        for j in range(n):
            if m1[i][j] == '*':
                m2[i][j] = '*'
    for x in range(n):
        for y in range(n):
            if m2[x][y] == 'x': #m2에서 x라면 (열린칸이라면)
                cnt = 0
                for i in range(8):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    
                    if 0 <= nx < n and 0 <= ny < n and m1[nx][ny] == '*':
                        cnt += 1
                            
                m2[x][y] = cnt #for문 끝나고 cnt를 m2에 반영
else:
    for x in range(n):
        for y in range(n):
            if m2[x][y] == 'x': #m2에서 x라면 (열린칸이라면)
                cnt = 0
                for i in range(8):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    
                    if 0 <= nx < n and 0 <= ny < n and m1[nx][ny] == '*':
                        cnt += 1
                            
                m2[x][y] = cnt #for문 끝나고 cnt를 m2에 반영


for i in range(n):
    print(''.join(map(str,m2[i])))
        


    