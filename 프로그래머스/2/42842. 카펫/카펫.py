def solution(brown, yellow):
    answer = []
    i = 1
    while True:
        if yellow % i == 0: 
            
            y_r = yellow // i
            y_c = i 
            
            b_r = y_r + 2
            b_c = y_c + 2
            
            if b_r * 2 + b_c * 2 - 4 == brown:
                if b_r >= b_c:
                    answer.append(b_r)
                    answer.append(b_c)
                    break
                else:
                    answer.append('세로가 가로보다 깁니다')
                    break
            else:
                i += 1
        else:
            i+=1
    return answer