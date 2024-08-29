N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

max_area = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        for k in range(N):
            if k == i or k == j:
                continue
            
            # i와 j 점을 연결하여 x축에 평행한 변을 만든다.
            if points[i][1] == points[j][1]:  # y좌표가 같음
                base_length = abs(points[i][0] - points[j][0])  # 밑변 길이
                height = abs(points[k][1] - points[i][1])  # 높이
                area = base_length * height
                max_area = max(max_area, area)

            # i와 k 점을 연결하여 x축에 평행한 변을 만든다.
            if points[i][1] == points[k][1]:  # y좌표가 같음
                base_length = abs(points[i][0] - points[k][0])  # 밑변 길이
                height = abs(points[j][1] - points[i][1])  # 높이
                area = base_length * height
                max_area = max(max_area, area)

            # j와 k 점을 연결하여 x축에 평행한 변을 만든다.
            if points[j][1] == points[k][1]:  # y좌표가 같음
                base_length = abs(points[j][0] - points[k][0])  # 밑변 길이
                height = abs(points[i][1] - points[j][1])  # 높이
                area = base_length * height
                max_area = max(max_area, area)

print(max_area)