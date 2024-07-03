n = int(input())
matrix = [list(map(int,input().split(' '))) for _ in range(n)]

answer = []

def recall(n,x,y):
    value = matrix[x][y]
    for i in range(x,n+x):
        for j in range(y,n+y):
            if value != matrix[i][j]:
                recall(n//3,x,y)
                recall(n//3,x,y+n//3)
                recall(n//3,x,y+2*(n//3))

                recall(n//3,x+n//3,y)
                recall(n//3,x+n//3,y+n//3)
                recall(n//3,x+n//3,y+2*(n//3))

                recall(n//3,x+2*(n//3),y)
                recall(n//3,x+2*(n//3),y+n//3)
                recall(n//3,x+2*(n//3),y+2*(n//3))

                return
    answer.append(matrix[x][y])
    

recall(n,0,0)
if len(answer) != 0:
    a = answer.count(-1)
    b = answer.count(0)
    c = answer.count(1)
    print(a,b,c)
else:
    print(matrix[0][0])


