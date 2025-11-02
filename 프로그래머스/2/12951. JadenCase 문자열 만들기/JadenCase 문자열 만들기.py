def solution(s):
    answer = ''
    s = s.split(' ')
    print(s)
    for i in s:
        if i != '':
            temp = ''
            temp += i[0].upper()
            for j in range(1,len(i)):
                temp += i[j].lower()
            answer += temp + ' '
        else:
            answer += ' '
    return answer[:-1]