import sys
import itertools
n = int(sys.stdin.readline())
m = sys.stdin.readline().split()

arr = []

for i in range(n):
    arr.append(i+1)
    
cnt = 0
x = ''
if m[0] == '1':
    for j in itertools.permutations(arr,n):
        cnt += 1
        if int(m[1]) == cnt:
            for i in range(n):
                print(j[i], end=' ')
else:
    for i in range(1,len(m)):
        x += i
        


    