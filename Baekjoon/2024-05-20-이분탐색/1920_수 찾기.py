n = int(input())
given = list(map(int,input().split(' ')))
given.sort() #1 2 3 4 5

m = int(input())
to_find = list(map(int,input().split(' ')))
#to_find.sort()#1 3 5 7 9

def bn_search(given, find, start, end):
    while start <= end:

        mid = (start + end) // 2
        if find == given[mid]:
            return 1
        if find > given[mid]:
            start = mid + 1
        elif find < given[mid]:
            end = mid - 1
        
    return None

for find in to_find:
    if bn_search(given, find, 0, n-1):
        print(1)
    else:
        print(0)
    

