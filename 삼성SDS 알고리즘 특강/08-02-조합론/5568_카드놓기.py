import sys
import itertools
n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
arr = []
answer = []
for _ in range(n):
    x = sys.stdin.readline().strip()
    arr.append(x)

for i in itertools.permutations(arr, k):
    answer.append(''.join(i))
print(set(answer))
print(len(set(answer)))