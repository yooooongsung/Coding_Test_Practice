def solution(s):
    answer = ''
    s = s.split(' ')
    arr = []
    for i in s:
        arr.append(int(i))
    ma = max(arr)
    mi = min(arr)
    answer = str(mi) + ' ' + str(ma)
    return answer