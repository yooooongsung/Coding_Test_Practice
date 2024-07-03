n , m = map(int,input().split(' '))
first = []
for _ in range(n):
    x = list(map(int,input().split(' ')))
    first.append(x)

M, K = map(int,input().split(' '))

second = []

for _ in range(M):
    x = list(map(int,input().split(' ')))
    second.append(x)

answer = []
for i in range(n):
    for k in range(K):
        element = 0
        for j in range(m):
            element += first[i][j] * second[j][k]
        answer.append(element)

for i in range(1,len(answer)+1):
    print(answer[i-1], end=' ')
    if i % K == 0:
        print('') 