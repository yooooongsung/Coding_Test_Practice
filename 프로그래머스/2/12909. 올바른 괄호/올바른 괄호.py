def solution(s):
    answer = True
    stack = []
    if s[0] == ')':
        return False
    for c in s:
        if c == '(':
            stack.append(c)
        elif stack and stack[-1] == '(':
                stack.pop()
    if stack: 
        return False
    else:
        return True