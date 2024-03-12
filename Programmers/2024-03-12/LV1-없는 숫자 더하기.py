def solution(numbers):
    answer = 0
    arr = [0,1,2,3,4,5,6,7,8,9]
    for i in arr:
        if i not in numbers:
            answer = answer + i
            
    return answer

print(solution([1,2,3,4,6,7,8,0])) #14

#https://school.programmers.co.kr/learn/courses/30/lessons/86051