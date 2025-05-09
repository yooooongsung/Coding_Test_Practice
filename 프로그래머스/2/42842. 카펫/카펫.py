def solution(brown, yellow):
    #갈색의 가로 x, 세로 y
    #노란색의 가로 x-2
    #노란색의 세로 y-2
    #노란색의 갯수 (x-2) * (y-2)
    #갈색의 갯수 x*y - 노란색의 갯수
    n = 1
    total = brown + yellow
    row = 0
    col = 0
    while True:
        if total % n == 0:
            row = total // n
            col = n
            if (row-2) * (col-2) == yellow and (row*col) - ((row-2) * (col-2)) == brown:
                return [row, col]
        n += 1