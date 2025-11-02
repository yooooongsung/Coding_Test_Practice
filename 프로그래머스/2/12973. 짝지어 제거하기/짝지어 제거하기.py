def solution(s):
    answer = -1
    stack = []
    stack.append(s[0])
    for i in range(1,len(s)):
        if stack and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])
    if stack:
        return 0
    else:
        return 1