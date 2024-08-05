import sys
n = int(input())
S = []

for _ in range(n):
    x = sys.stdin.readline().strip()
    
    if x == 'all':
        S = [i for i in range(1,21)]
    elif x == 'empty':
        S.clear()
    else:
        a = x.split()
        oper = a[0]
        num = int(a[1])
        if oper == 'add':
            if num in S:
                continue
            S.append(num)
        elif oper == 'remove':
            if num in S:
                S.remove(num)
        elif oper == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        elif oper == 'toggle':
            if num in S:
                S.remove(num)
            else:
                S.append(num)
    
    