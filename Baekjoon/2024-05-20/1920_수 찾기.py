n = int(input())
given = list(map(int,input().split(' ')))
given.sort() #1 2 3 4 5

m = int(input())
to_find = list(map(int,input().split(' ')))
#to_find.sort()#1 3 5 7 9
start = given[0]
end = given[-1]


def bn_search(find,start,end):
    while start <= end:

        mid = (start + end) // 2
        if find == mid:
            return 1
        if find > mid:
            start = mid + 1
            bn_search(find,start,end)
        elif find < mid:
            end = mid - 1
            bn_search(find,start,end)
        
        elif find > end:
            return 0

for i in to_find:
    if bn_search(i,start,end):
        print(1)
    else:
        print(0)
    

