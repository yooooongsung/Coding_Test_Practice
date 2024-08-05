import sys
n = int(input())
matrix = [list(sys.stdin.readline().strip()) for _ in range(n)]
find = []
left_arm = 0
right_arm = 0
mid = 0
left_leg = 0
right_leg = 0
for x in range(n):
    for y in range(n): 
        if matrix[x][y] == '*': #처음 만나는 별은 무조건 머리임
            find.append(x+1)
            find.append(y)

heartx = find[0] #심장위치 저장
hearty = find[1]

print(heartx+1,hearty+1)

for i in range(hearty-1,-1,-1): #왼쪽팔
    if matrix[heartx][i] == '*':
        left_arm += 1

for i in range(hearty+1,n,1):#오른쪽팔
    if matrix[heartx][i] == '*':
        right_arm += 1

for i in range(heartx+1,n,1):
    if matrix[i][hearty] == '*': #허리
        mid += 1
    elif matrix[i][hearty] == '_':
        llx, lly = i,hearty-1
        rlx, rly = i,hearty+1
        break
        
for l in range(llx,n,1): #왼쪽다리
    if matrix[l][lly] == '*':
        left_leg += 1
        
for r in range(rlx,n,1): #오른쪽다리
    if matrix[r][rly] == '*':
        right_leg += 1

print(left_arm,right_arm,mid,left_leg,right_leg)