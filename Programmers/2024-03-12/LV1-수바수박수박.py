def solution(n):
    answer = ''
    for i in range(1,n+1):
        if i % 2 == 1:
            answer = answer + '수'
        else:
            answer = answer + '박'
    return answer

print(solution(3))
#https://school.programmers.co.kr/learn/courses/30/lessons/12922