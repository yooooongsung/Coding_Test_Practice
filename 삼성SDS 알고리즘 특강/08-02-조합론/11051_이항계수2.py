import sys
n, k = map(int,sys.stdin.readline().split())

result = 1
for _ in range(k):
    result *= n
    n -= 1

div = 1
for i in range(k,0,-1):
    div *= i

print((result// div) % 10007)