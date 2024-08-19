import sys
n, k = map(int,input().split())
nations = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
gold = []
silver = []
bronze = []

nations.sort(key=lambda x:(x[1],x[2],x[3]), reverse=True)
for i in range(n):
    if nations[i][0] == k:
        idx = i

for i in range(n):
    if nations[idx][1:] == nations[i][1:]:
        print(i+1)
        break
