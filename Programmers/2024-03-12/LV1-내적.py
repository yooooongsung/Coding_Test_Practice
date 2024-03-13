def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer = answer + (a[i] * b[i])
    return answer

print(solution([1,2,3,4],[-3,-1,0,2]))

#https://school.programmers.co.kr/learn/courses/30/lessons/70128