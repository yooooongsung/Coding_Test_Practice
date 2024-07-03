# n = int(input())
# d = [input() for _ in range(n)]
# y = [input() for _ in range(n)]

# answer = 0
# for i in range(n):
#     x = d[i]
#     if d.index(x) > y.index(x):
#         answer += 1

# print(answer)

#반례
#a b c d - 0 1 2 3
#d a c b - 3 0 2 1
#답 : 2 >> c가 b를 추월했음에도, 인덱스만 비교한다면 이를 찾아내지 못함.
#딕셔너리를 사용하여 상대 위치를 체크할 필요가 있음.

n = int(input())
enter_cars = {}
out_cars = {}

for i in range(n):
    enter = input()
    enter_cars[enter] = i

for i in range(n):
    out = input()
    out_cars[out] = i

answer = 0
out_keys = list(out_cars.keys())

for i in range(len(out_keys)-1): 
    #나온 차와 그 뒤의 차의 순서를 비교하기 때문에, 
    #가장 마지막에 나온 차량은 비교할 필요가 없기 때문에 -1해줌
    out_now = enter_cars[out_keys[i]] #현재 나간 차량의 들어온 순서
    
    for j in range(i+1,len(out_keys)): 
        out_next = enter_cars[out_keys[j]] #현재 나간 차량 이후에 나가는 차량의 순서를 구함
        if out_next < out_now: 
            #만약 현재 나가는 차량보다 뒤에 나가는 차량의 들어온 순서가 
            #더 낮다면(먼저 들어왔다면)
            answer += 1
            break
print(answer)


