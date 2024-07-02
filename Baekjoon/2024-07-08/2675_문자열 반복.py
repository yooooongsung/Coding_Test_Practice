n = int(input())
arr = [list(input().split(' ')) for _ in range(n)]

for i in range(n):
    answer = ''
    m = int(arr[i][0])
    for j in arr[i][1]:
        for k in range(m):
            answer += j
    print(answer)
    
#더 좋은 다른 풀이

# a = int(input())
# for i in range(a):
#   b, c = input().split()
#   for i in range(len(c)):
#     print(int(b) * c[i], end='')
#   print()
