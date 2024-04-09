from collections import deque

wheels = [deque(list(map(int,input().rstrip()))) for _ in range(4)]

k = int(input())

for _ in range(k):
    r = []
    for i in range(4):
        r.append([wheels[i][6],wheels[i][2]])
    n, d = map(int,input().split())
    n = n -1

    if n != 0 :
        for i in range(n,0,-1):
            if r[i][0] != r[i-1][1]: #현재 톱니바퀴의 왼쪽과 왼쪽 톱니바퀴의 오른쪽 부분 비교
                if (n-(i-1)) % 2 == 0:
                    wheels[i-1].rotate(d)
                elif (n-(i-1)) % 2 != 0:
                    wheels[i-1].rotate(-1*d)
            elif r[i][0] == r[i-1][1]:
                break
    
    if n != 3:
        for i in range(n,3):
            if r[i][1] != r[i+1][0]:
                if (n-(i+1)) % 2 == 0:
                    wheels[i+1].rotate(d)
                elif (n-(i+1)) % 2 != 0:
                    wheels[i+1].rotate(-1*d)
            elif r[i][1] == r[i+1][0]:
                break
    
    wheels[n].rotate(d)

res = 0
if wheels[0][0] == 1:
	res+=1
if wheels[1][0] == 1:
	res+=2
if wheels[2][0] == 1:
	res+=4
if wheels[3][0] ==1:
	res+=8
print(res)