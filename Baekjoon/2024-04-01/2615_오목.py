import sys

matrix = [list(map(int,input().split())) for _ in range(19)]
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]


# → ↓ ↘ ↗
dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]

for x in range(19):
    for y in range(19):
        if matrix[x][y] != 0:
            focus = matrix[x][y]
            for i in range(4):
                cnt = 1
                nx = x + dx[i]
                ny = y + dy[i]

                while 0 <= nx < 19 and 0 <= ny < 19 and matrix[nx][ny] == focus:
                    cnt += 1

                    if cnt == 5:
                        # 육목 체크
                        if 0 <= x - dx[i] < 19 and 0 <= y - dy[i] < 19 and matrix[x - dx[i]][y - dy[i]] == focus:
                            break
                        if 0 <= nx + dx[i] < 19 and 0 <= ny + dy[i] < 19 and matrix[nx + dx[i]][ny + dy[i]] == focus:
                            break
                        # 육목이 아니면 성공한거니까 종료
                        print(focus)
                        print(x + 1, y + 1)
                        sys.exit(0)

                    nx += dx[i]
                    ny += dy[i]

print(0)

    

