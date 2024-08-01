import heapq
import sys
n = int(input())
pq1 = []
pq2 = []
for i in range(n):
    x = int(sys.stdin.readline()) 
    if len(pq1) == len(pq2): #짝수개일때는, 더 작은 값을 출력해야 함
        heapq.heappush(pq1,-x) #최대힙 입력받기
    else:  
        heapq.heappush(pq2,x) #최소힙 입력받기 
    
    if pq2 and pq2[0] < -pq1[0]:
        pq1_cur = heapq.heappop(pq1)
        pq2_cur = heapq.heappop(pq2)
        
        heapq.heappush(pq1,-pq2_cur)
        heapq.heappush(pq2,-pq1_cur)
    print(-pq1[0])

#짝, 홀 이해하기
#다음과 같은 예제를 살펴보자
#1,2,5 >> 이 경우 5는 leftheap에 들어오게 된다(힙의 길이가 1로 같기 때문)
#힙의 첫번쨰 원소를 비교해서 바꿔주는 코드가 없다면
#중간값인 2가 아니라 5가 출력될 것
#고로 pq1의 첫번째 원소는 pq2의 첫번째 원소보다 항상 작아야한다.
#1,2,7,3,5