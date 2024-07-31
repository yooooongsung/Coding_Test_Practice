import sys
n = int(input())
stack = []
for _ in range(n):
    x = sys.stdin.readline().strip()
    if 'push' in x:
        new = x.split(' ')
        stack.append(int(new[1]))
    elif x == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif x == 'size':
        print(len(stack))
    elif x == 'empty':
        if stack:
            print(0)
        else:
            print(1)    
    elif x == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
            
            
# for _ in range(n):
#     x = sys.stdin.readline().strip()
#     if 'push' in x:
#         new = x.split(' ')
#         print(new[1])
