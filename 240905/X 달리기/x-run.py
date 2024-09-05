# X = int(input())

# print(int(((X-1)**0.5)*2)) 처음 속도 1만 거리에서 뺀 나머지 거리에 대해 등가속운동 => 이등변 삼각형 넓이
x = int(input())
t = 0
left_dist = x
v = 1

while True:
    left_dist -= v
    t += 1

    if left_dist == 0:
        break

    # 속도를 더 높여도 괜찮은지 결정합니다.
    # 속도를 1 더 높이면, (v + 1) + v + (v - 1) + ... + 2 + 1 만큼 이동하게 됩니다.
    # 즉, 남은 거리가 (v + 1) * (v + 2) / 2 보다 크거나 같아야 합니다.
    if left_dist >= (v + 1) * (v + 2) / 2:
        v += 1
    
    # 속도를 유지해도 괜찮은지 결정합니다.
    # 속도를 유지하면, v + (v - 1) + ... + 2 + 1 만큼 이동하게 됩니다.
    # 즉, 남은 거리가 v * (v + 1) / 2 보다 크거나 같아야 합니다.
    elif left_dist >= v * (v + 1) / 2:
        # 아무 것도 하지 않습니다.
        pass

    # 위 둘을 만족하지 못하면 반드시 속도를 줄여야만 합니다.
    else:
        v -= 1

print(t)