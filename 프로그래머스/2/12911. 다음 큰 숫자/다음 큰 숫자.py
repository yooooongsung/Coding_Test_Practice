def solution(n):
    answer = 0
    cnt_n = bin(n)[2:].count("1")
    cnt_nxt = 0
    for i in range(1,1000000):
        nxt = n + i
        cnt_nxt = bin(nxt)[2:].count("1")
        if cnt_nxt == cnt_n:
            return nxt
