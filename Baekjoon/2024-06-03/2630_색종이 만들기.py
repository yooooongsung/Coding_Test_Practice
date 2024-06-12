n = int(input())
matrix = []

for _ in range(n):
    x = list(map(int,input().split(' ')))
    matrix.append(x)

answer = []

def recall(n, x, y):
    value = matrix[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if value != matrix[i][j]:
                recall(n//2, x, y)
                recall(n//2, x, y + n//2)
                recall(n//2, x+n//2, y)
                recall(n//2, x+n//2, y+n//2)
                return
    if value == 0: 
        answer.append(0)
    else:
        answer.append(1)

recall(n, 0, 0)

print(answer.count(0))
print(answer.count(1))
