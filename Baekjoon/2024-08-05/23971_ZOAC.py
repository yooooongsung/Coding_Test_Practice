h, w, n, m = map(int,input().split())
visited_h = [False] * h
visited_w = [False] * w

for i in range(0,h,n+1):
    visited_h[i] = True

for i in range(0,w,m+1):
    visited_w[i] = True
    i += n

cnt_h = 0
for i in range(h):
    if visited_h[i] == True:
        cnt_h += 1

cnt_w = 0
for i in range(w):
    if visited_w[i] == True:
        cnt_w += 1

print(cnt_h*cnt_w)