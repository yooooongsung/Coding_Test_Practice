def solution(n):
    answer = 0
    
    arr = list(map(int,str(n))) #문자열로 바꾼 수 -> 정수형으로 리스트로 매핑
    arr.sort(reverse=True) #내림차순 정렬
    answer = ''.join(str(i) for i in arr) 
    #정수형이던 배열을 join으로 합치기 위해 문자열로 변경 후 join
    return answer
print(solution(12345))

#map(function, iterable)
#arr = [int(i) for i in str(n)]

#https://school.programmers.co.kr/learn/courses/30/lessons/12933