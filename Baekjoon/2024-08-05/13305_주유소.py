n = int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

answer = 0

for i in range(n-1):
    if i+1 <= n-2:
        if price[i] > price[i+1]:
            answer += price[i] * dist[i]
        else:
            for j in range()
            answer += price[i] * (dist[i]+dist[i+1])
#i+1 ~ n 사이의 가장 작은 값과 현재를 비교해서
#현재가 더 작다면 남은 거리를 더하기
#더 작은 값이 있다면 그 지점까지만 거리를 더해서 곱하기
print(answer)
            