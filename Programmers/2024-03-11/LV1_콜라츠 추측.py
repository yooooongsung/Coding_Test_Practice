def solution(num):
    answer = 0
    if num == 1:
        answer = 0
    else:
        while num != 1:
            if num % 2 == 0:
                num = num // 2
                answer+=1
                continue
            else:
                num = num * 3 + 1
                answer+=1
                continue
    
    if answer >= 500:
        answer = -1
        
    return answer

print(solution(16))
print(solution(626331))

#https://school.programmers.co.kr/learn/courses/30/lessons/12943