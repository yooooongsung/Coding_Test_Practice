def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
            answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

print(solution([2,36,1,3],1)) #[1, 2, 3, 36]
print(solution([3,2,6],10)) #[-1]

#https://school.programmers.co.kr/learn/courses/30/lessons/12910