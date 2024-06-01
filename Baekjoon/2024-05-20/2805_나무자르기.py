n, m = map(int,input().split(' '))
trees = list(map(int,input().split(' ')))

def bn_search(start, end, n, m):
    result = []
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in range(n):
            x = trees[i] - mid
            if x > 0:
                cnt += x
        
        if cnt < m:
            end = mid - 1
            
        else:
            start = mid + 1
            result.append(mid)
    return max(result)

start = 0
end = max(trees)


print(bn_search(start, end, n, m))
