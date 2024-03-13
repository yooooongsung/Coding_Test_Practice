def solution(arr):
    answer = []
    mn = min(arr)
    arr.remove(mn) #del - slicing과 연계해서 사용 
    # remove - 특정 값을 제거 / 그 자체로 반환
    answer = arr
    
    if len(answer) == 0:
        answer.append(-1)
    
    return answer

print(solution([4,3,2,1])) #[4,3,2]
print(solution([10])) #[-1]

#https://school.programmers.co.kr/learn/courses/30/lessons/12935