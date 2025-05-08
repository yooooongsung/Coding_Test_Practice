def solution(s):
    answer = True
    s_open = 0
    s_close = 0
    if s[0] == ')':
            return False
    else:
        for i in range(len(s)):
            if s_close > s_open:
                return False
            else:
                if s[i] == '(':
                    s_open += 1
                else:
                    s_close += 1
    if s_open == s_close:
        answer = True
    else:
        answer = False
    

    return answer