matrix = [list(map(int,input().split())) for _ in range(19)]
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]


def right(i,j,color,cnt):
    if j+1 < 19:
        nx = matrix[i][j+1]
        if matrix[i][j] == nx:
            right(i,j+1)
            cnt += 1
            if cnt == 5:
                if color == 1:
                    print(1)
                else:
                    print(2)
        else:
            return

for i in range(19):
    for j in range(19):
        if matrix[i][j] == 1:
            cnt = 1
            right(i,j,matrix[i][j],cnt)
        elif matrix[i][j] == 2:
            d = 1
        else:
            d = 1


    

