import sys
n, q = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))

for _ in range(q):
    answer = 0
    x,y,a,b = map(int,sys.stdin.readline().split())
    print(arr)
    for i in range(x-1,y):
        answer += arr[i]
    arr[a-1] = b
    print(answer)