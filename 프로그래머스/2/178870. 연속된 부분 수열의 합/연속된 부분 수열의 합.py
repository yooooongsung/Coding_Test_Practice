def solution(seq, k):
    answer = []
    left = 0
    right = 0
    temp = seq[0]
    ranger = []
    length = []
    while left <= right and right < len(seq):
        if temp == k:
            ranger.append([left, right])
            length.append(right - left + 1)
            temp -= seq[left]
            left += 1
        elif temp > k:
            temp -= seq[left]
            left += 1
            
        elif temp < k:
            right += 1
            if right >= len(seq):
                break
            temp += seq[right]

    a = min(length)
    for h in range(len(ranger)):
        if length[h] == a:
            return ranger[h]
    print("쌍값 배열 : ", ranger)
    print("범위 배열 : ", length)
    
    return answer

