import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if scoville[0] >= K:
            break
        elif len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        a = heapq.heappop(scoville) 
        b = heapq.heappop(scoville)
        temp = a + 2 * b
        heapq.heappush(scoville,temp)
        answer += 1
    return answer