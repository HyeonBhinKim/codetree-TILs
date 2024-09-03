n, k = map(int, input().split())
n_lst = list(map(int, input().split()))

def is_possible(max_val):
    # 시작 위치는 0 (1번 돌)
    current_position = 0
    
    # 1번 돌부터 n번 돌까지 도달할 수 있는지 체크
    for i in range(n):
        # 현재 위치에서 k 이내로 점프할 수 있는 범위 내에서 숫자가 max_val 이하인지 체크
        if n_lst[i] <= max_val:
            # 가능한 위치를 업데이트
            if i - current_position > k:
                # 점프할 수 없는 경우, 현재 max_val로는 불가능
                return False
            current_position = i  # 현재 위치 업데이트
    
    return True

# 가능한 최대 숫자의 범위는 1에서 100까지
left, right = 1, 100
result = 100

while left <= right:
    mid = (left + right) // 2
    if is_possible(mid):
        result = mid  # 가능한 경우의 최솟값 업데이트
        right = mid - 1  # 더 작은 값으로 확인
    else:
        left = mid + 1  # 더 큰 값으로 확인

print(result)