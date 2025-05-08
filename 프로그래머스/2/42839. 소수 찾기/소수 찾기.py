import math
from itertools import permutations

def solution(numbers):
    def is_prime_number(x):
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return False
        return True
    
    answer = 0
    prime_set = set()  # 소수를 저장할 집합
    
    # 모든 가능한 조합을 생성
    for i in range(1, len(numbers) + 1):
        for p in permutations(numbers, i):
            num = int(''.join(p))
            if num not in prime_set and num > 0:  # 중복 소수 및 0 제외
                if is_prime_number(num):
                    prime_set.add(num)
    
    return len(prime_set)


