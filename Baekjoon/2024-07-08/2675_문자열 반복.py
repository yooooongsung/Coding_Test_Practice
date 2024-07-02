n = int(input())
arr = [list(input().split(' ')) for _ in range(n)]

for i in range(n):
    answer = ''
    m = int(arr[i][0])
    for j in arr[i][1]:
        for k in range(m):
            answer += j
    print(answer)
    

