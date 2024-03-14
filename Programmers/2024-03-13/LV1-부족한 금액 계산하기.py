def solution(price, money, count):
    answer = -1
    summ = 0
    for i in range(1,count+1):
        summ = summ + (price * i)
    result = money - summ
    if result < 0:
        answer = abs(result)
    else:
        answer = 0
    return answer

print(solution(3,20,4)) #10

#https://school.programmers.co.kr/learn/courses/30/lessons/82612