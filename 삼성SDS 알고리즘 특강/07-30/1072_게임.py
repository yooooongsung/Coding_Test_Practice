x, y = map(int,input().split(' '))
start = 0
end = x
r = int(y * 100 / x )
def bn_search(start, end, x, y):
    if x == y or r == 99: #99퍼 유의.....
        return -1
    result = []
    while start <= end:
        mid = (start + end) // 2
        c = int((y+mid) * 100 / (x+mid))
        if r >= c:
            start = mid + 1
        else: 
            end = mid - 1
            result.append(mid)
    
    return min(result)

print(bn_search(start, end, x, y))
        