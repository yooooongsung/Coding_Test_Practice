import sys
n, m = map(int,input().split())
arr = {}
for _ in range(m):
    num, a, b = sys.stdin.readline().split()
    if num == '0': #합치기
        if a in arr:
            arr[a].append(b)
        else:
            arr[a] = [b]
    elif num == '1':
        check = arr.get(a)
        if b in check:
            print('YES')
        else:
            print('NO')