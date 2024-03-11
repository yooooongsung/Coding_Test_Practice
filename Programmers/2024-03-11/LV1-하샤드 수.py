def solution(x):
    answer = True
    arr = list(map(int,str(x))) #이번에도 정수를 배열로 변환(문자열 -> 정수형으로 매핑)
    if x % sum(arr) == 0:
        answer = True
    else:
        answer = False
    return answer

print(solution(13))

#https://school.programmers.co.kr/learn/courses/30/lessons/12947