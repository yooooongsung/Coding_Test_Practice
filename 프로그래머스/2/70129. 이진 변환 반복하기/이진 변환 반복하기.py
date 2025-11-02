def solution(s):
    cnt_zero = s.count("0")
    one = s.count("1")
    cnt_time = 1
    while True:
        if one == 1:
            break
        temp = bin(one)[2:]
        one = temp.count("1")
        cnt_zero += temp.count("0")
        cnt_time += 1
    
    return [cnt_time, cnt_zero]