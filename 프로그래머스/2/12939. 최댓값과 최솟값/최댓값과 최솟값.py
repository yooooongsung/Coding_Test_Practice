def solution(s):
    answer = ''
    temp = s.split()
    for i in range(len(temp)):
        temp[i] = int(temp[i])
    answer = str(min(temp)) + " " + str(max(temp))
    return answer

# def solution(s):
#     temp = list(map(int, s.split()))  # split과 int 변환을 map으로 한 번에 처리
#     return f"{min(temp)} {max(temp)}"  # f-string으로 간결하게 반환