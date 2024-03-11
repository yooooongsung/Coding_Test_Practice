import math
def solution(n):
    answer = 0
    a = math.sqrt(n)
    if int(a) == a:
        answer = (a+1) * (a+1)
    else:
        answer = -1

    return int(answer)

print(solution(121))

#https://school.programmers.co.kr/learn/courses/30/lessons/12934#