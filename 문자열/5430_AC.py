import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    func = input().strip()
    n = int(input().strip())
    error = 0
    if n <= 0:
        s = input()
        arr = []
    else:
        s = input()
        s = s[1:-2]
        s = s.split(',')
        arr = [int(i) for i in s]
        
    arr = deque(arr)
    reverse = False
    for f in func:
        if arr and f == 'R': #뒤집기
            reverse = not reverse
        elif arr and f == 'D': #버리기
            if reverse == True:
                arr.pop()
            else:
                arr.popleft()
        elif not arr and f == 'D':
            error = 1
    temp = []
    if reverse:
        while arr:
            temp.append(arr.pop())
    else:
        while arr:
            temp.append(arr.popleft())
    
    if error == 1:
        print('error')
    else:
        print('[' + ','.join(map(str, temp)) + ']')