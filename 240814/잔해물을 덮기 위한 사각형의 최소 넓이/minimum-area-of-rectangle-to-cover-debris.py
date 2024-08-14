# 첫 번째 직사각형의 좌표를 입력받습니다.
x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
# 두 번째 직사각형의 좌표를 입력받습니다.
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

# OFFSET을 적용
OFFSET = 1000
x1_1 += OFFSET
y1_1 += OFFSET
x2_1 += OFFSET
y2_1 += OFFSET
x1_2 += OFFSET
y1_2 += OFFSET
x2_2 += OFFSET
y2_2 += OFFSET

# 첫 번째 직사각형의 넓이를 계산합니다.
area1 = (x2_1 - x1_1) * (y2_1 - y1_1)

# 두 번째 직사각형과의 겹치는 부분의 좌표 계산
overlap_x1 = max(x1_1, x1_2)
overlap_y1 = max(y1_1, y1_2)
overlap_x2 = min(x2_1, x2_2)
overlap_y2 = min(y2_1, y2_2)

# 겹치는 영역이 존재하는지 확인
if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
    # 겹치는 부분의 넓이를 계산
    overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)
else:
    overlap_area = 0  # 겹치는 영역이 없으면 넓이는 0

# 남아 있는 첫 번째 직사각형의 넓이 계산
remaining_area = area1 - overlap_area

# 남아 있는 부분을 덮기 위한 최소 직사각형의 넓이를 계산
if remaining_area > 0:
    min_x = min(x1_1, x2_1)
    max_x = max(x1_1, x2_1)
    min_y = min(y1_1, y2_1)
    max_y = max(y1_1, y2_1)

    # 최종 넓이 계산
    cover_area = (max_x - min_x) * (max_y - min_y)
else:
    cover_area = 0  # 남아 있는 부분이 없을 경우

print(cover_area)