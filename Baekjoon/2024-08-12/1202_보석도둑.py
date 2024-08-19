import sys
import heapq
n, k = map(int,input().split()) #보석의 개수 / 가방의 개수

jew = []
for _ in range(n):
    m, v = map(int,sys.stdin.readline().split())
    heapq.heappush(jew, [m,v])
    
bags = [int(sys.stdin.readline()) for _ in range(k)]
bags.sort()

ans = 0
temp = []

for i in bags:
    while jew and i >= jew[0][0]:
        heapq.heappush(temp, -heapq.heappop(jew)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not jew:
        break
print(ans)
