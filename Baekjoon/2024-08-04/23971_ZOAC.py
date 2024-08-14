h, w, n, m = map(int,input().split())
r , c = 0 , 0
cnt_r = 0
cnt_c = 0
while True:
    
    cnt_r += 1
    r += n
    result = cnt_r + r
    if result >= h:
        print(cnt_r)
        break

while True:
    cnt_c += 1
    c += m
    result = cnt_c + c 
    if result >= w:
        print(cnt_c)
        break

print(cnt_r * cnt_c)
    