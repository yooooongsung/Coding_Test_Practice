import sys
from collections import deque
n = int(input())
q = deque([])
for _ in range(n):
    x = sys.stdin.readline().strip()
    if 'push' in x:
        new = x.split(' ')
        q.append(int(new[1]))
    elif x == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif x == 'size':
        print(len(q))
    elif x == 'empty':
        if q:
            print(0)
        else:
            print(1)    
    elif x == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif x == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])