n = int(input())
matrix = [list(map(int,input().strip())) for _ in range(n)]

answer = []
def recall(n,x,y):
    value = matrix[x][y]
    for i in range(x,n+x):
        for j in range(y,n+y):
            if value != matrix[i][j]:
                answer.append('(')
                recall(n//2,x,y)
                recall(n//2,x,y+n//2)
                recall(n//2,x+n//2,y)
                recall(n//2,x+n//2,y+n//2)
                answer.append(')')
                return
    answer.append(str(matrix[x][y]))
    
    

recall(n,0,0)

if len(answer) != 0:
    result =''.join(answer)
    print(result)
else:
    print(matrix[0][0])

