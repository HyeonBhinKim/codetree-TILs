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

# 남아 있는 잔해물을 덮기 위한 최소 직사각형의 좌표를 계산
min_x = min(x1_1, x1_2)
max_x = max(x2_1, x2_2)
min_y = min(y1_1, y1_2)
max_y = max(y2_1, y2_2)

# 최소 직사각형의 넓이를 계산
cover_area = (max_x - min_x) * (max_y - min_y)

# 남아 있는 영역이 겹치는 경우 넓이를 다시 계산
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

# 남아 있는 부분을 덮기 위한 최소 직사각형의 넓이에서 겹치는 부분 넓이를 제외
final_area = cover_area - overlap_area

print(final_area)