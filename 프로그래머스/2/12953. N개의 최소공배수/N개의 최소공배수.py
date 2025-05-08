import math
def lcm(a,b):
    x = math.gcd(a,b)
    return a * b // x

def solution(arr):
    answer = 0
    arr.sort()
    
    for i in range(len(arr)-1):
        left = arr[i]
        right = arr[i+1]
        arr[i+1] = lcm(left,right)
    answer = arr[-1]
    return answer