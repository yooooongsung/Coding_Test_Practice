n, m = map(int,input().split(' '))
trees = list(map(int,input().split(' ')))
start = 0
end = max(trees)

def bn_search(start, end, n, m):
    result = []
    while start <= end:
        cnt = 0
        mid = (start + end) // 2
        for i in range(n):
            x = (trees[i] - mid)
            if x > 0:
                cnt += x
        if cnt < m: #mid 높이에 절단기를 위치하고 잘랐을 때 m 이상의 나무를 얻을 수 있는가?
            end = mid - 1
        else: #cnt >= m, 즉, 잘랐을 때 m 이상의 나무를 얻을 수 있기 때문에, 더 많이 잘라야함 (mid를 더 크게 갱신
            #>> 그때의 mid 값을 담아 최댓값을 구하면 됨
            
            #>> 그럼 탈출 조건은? start > end 일 경우
            start = mid + 1
            result.append(mid)
    return max(result)

print(bn_search(start, end, n, m))