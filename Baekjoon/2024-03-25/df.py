n, k = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

# 각 색깔별로 x좌표와 y좌표의 최소값, 최대값을 저장할 딕셔너리 초기화
color_ranges = {color: [float('inf'), float('-inf'), float('inf'), float('-inf')] for color in range(1, k+1)}

# 각 점을 순회하며 색깔별 좌표 범위 업데이트
for x, y, color in points:
    color_ranges[color][0] = min(color_ranges[color][0], x)  # x 최소값
    color_ranges[color][1] = max(color_ranges[color][1], x)  # x 최대값
    color_ranges[color][2] = min(color_ranges[color][2], y)  # y 최소값
    color_ranges[color][3] = max(color_ranges[color][3], y)  # y 최대값

# 모든 색깔을 포함하는 직사각형의 좌표 범위 찾기
min_x = min([range_[0] for range_ in color_ranges.values()])
max_x = max([range_[1] for range_ in color_ranges.values()])
min_y = min([range_[2] for range_ in color_ranges.values()])
max_y = max([range_[3] for range_ in color_ranges.values()])

# 최소 넓이 계산
min_area = (max_x - min_x) * (max_y - min_y)
print(min_area)
