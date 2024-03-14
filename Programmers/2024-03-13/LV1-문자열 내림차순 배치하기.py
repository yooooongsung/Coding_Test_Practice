def solution(s):
    answer = ''
    arr = [i for i in s]
    arr.sort(reverse=True)
    answer = ''.join(arr)
    return answer

print(solution("Zbcdefg")) #"gfedcbZ"