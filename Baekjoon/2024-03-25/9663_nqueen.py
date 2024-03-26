block = [list(map(int,input().split())) for _ in range(9)]

not_in_row = []

for i in range(9):
    for j in range(1,10):
        if j not in block[i]:
            not_in_row.append(j)

for i in range(9):
    for j in range(9):
        for k in range(1,10):
            if k not in block[j][i]:
            
    
print(not_in_row)