n = int(input())
start = []
end = []
meetings = []
for _ in range(n):
    a,b = map(int,input().split())
    start.append(a)
    end.append(b)

for i in range(n):
    if b[i] - a[i] > b[i+1] - a[i+1]:
        if b[i] < b[i+1]:
            meetings.append([a[i],b[i]])
        else:
            meetings.append(a[i+1],b[i+1])
        
