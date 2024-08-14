# 첫 번째 직사각형의 좌표를 입력받습니다.
x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
# 두 번째 직사각형의 좌표를 입력받습니다.
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

# 첫 번째 직사각형의 넓이를 계산합니다.
# 두 번째 직사각형의 범위를 고려하여 남아 있는 부분을 계산합니다.

# 남아 있는 부분의 좌표를 계산
remaining_x1 = x1_1
remaining_y1 = y1_1
remaining_x2 = x2_1
remaining_y2 = y2_1

# 두 번째 직사각형이 첫 번째 직사각형을 덮는 경우
if x1_2 < x2_1 and x2_2 > x1_1 and y1_2 < y2_1 and y2_2 > y1_1:
    # 겹치는 부분의 좌표를 계산
    overlap_x1 = max(remaining_x1, x1_2)
    overlap_y1 = max(remaining_y1, y1_2)
    overlap_x2 = min(remaining_x2, x2_2)
    overlap_y2 = min(remaining_y2, y2_2)

    # 겹치는 영역이 존재하는지 확인
    if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
        # 겹치는 부분의 넓이를 계산
        overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)

        # 남아 있는 부분의 넓이 계산
        remaining_area = (remaining_x2 - remaining_x1) * (remaining_y2 - remaining_y1) - overlap_area
    else:
        remaining_area = (remaining_x2 - remaining_x1) * (remaining_y2 - remaining_y1)
else:
    remaining_area = (remaining_x2 - remaining_x1) * (remaining_y2 - remaining_y1)

# 남아 있는 부분을 덮기 위한 최소 직사각형의 넓이를 계산
min_x = min(remaining_x1, remaining_x2)
max_x = max(remaining_x1, remaining_x2)
min_y = min(remaining_y1, remaining_y2)
max_y = max(remaining_y1, remaining_y2)

# 최종 넓이 계산
cover_area = (max_x - min_x) * (max_y - min_y)

print(cover_area)