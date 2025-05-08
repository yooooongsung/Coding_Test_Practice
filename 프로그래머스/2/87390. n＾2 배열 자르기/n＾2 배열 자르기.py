def solution(n, left, right):
    answer = []

    for i in range(left, right + 1):
        row = i // n  # 현재 위치의 행 번호
        col = i % n   # 현재 위치의 열 번호
        value = max(row, col) + 1  # 해당 위치의 값 (패턴에서 유도됨)
        answer.append(value)

    return answer