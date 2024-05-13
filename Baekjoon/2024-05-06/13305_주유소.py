#도시의 갯수(주유소의갯수)
#거리
#리터당 가격
n = int(input())
distance = list(map(int,input().split(' ')))
price = list(map(int,input().split(' ')))
start = price[0]
current_distance = distance[0]
answer = 0

for i in range(n-1):
    if start > price[i]:
        answer += (start * current_distance)
        start = price[i]
        current_distance = 0
        continue
    current_distance += distance[i]

print(answer)
#현재 있는 위치에서 다음에 더 싼 주유소가 있는지 확인
#더 싼 주유소까지만 주유하기
#더 싼 주유소를 만나면 그 이후의 주유소 중 더 싼 주유소가 있다면 거기까지만 주유하기



