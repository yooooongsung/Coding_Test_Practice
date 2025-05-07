def solution(skill, skill_trees):
    answer = 0
    arr = []
    for s in skill_trees:
        ss = ''
        for c in s:
            if c in skill:
                ss += c
        if ss: arr.append(ss)
        else: answer += 1
    print(arr)
    for s in arr:
        flag = False
        for i in range(len(s)):
            if s[i] == skill[i]:
                flag = True
            else: 
                flag = False
                break
        if flag:
            answer += 1
    return answer