
n, score, p = map(int,input().split())
arr = []
if n > 0:
    arr = list(map(int,input().split()))
    arr.append(score)
    arr.sort(reverse=True)

    for i in range(len(arr)):
        if score == arr[i]:
            if min(arr) >= score and len(arr) > p:
                print(-1)
                break
            print(i+1)
            break
    
else:
    print(1)
