import sys
from itertools import permutations
input = sys.stdin.readline
n,k = map(int,input().split())
a = list(map(int,input().split()))
li = list(permutations(a,n))
cnt = 0


for i in range(len(li)):
    flag = 0
    temp = 0

    for j in range(n):
        temp = temp + li[i][j] - k

        if temp < 0:
            flag = 0
            break

        elif temp >= 0:
            flag = 1

    if flag == 1:
        cnt += 1

print(cnt)