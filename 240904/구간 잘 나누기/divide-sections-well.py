def can_divide(arr, m, max_sum):
    current_sum = 0
    required_parts = 1  # 최소 1개의 구간

    for num in arr:
        if current_sum + num > max_sum:
            # 현재 구간의 합이 max_sum을 초과하면 새 구간 시작
            current_sum = num
            required_parts += 1
            if required_parts > m:  # 필요한 구간 수가 m을 초과하는 경우
                return False
        else:
            current_sum += num
            
    return True

def min_max_partition_sum(arr, n, m):
    left, right = max(arr), sum(arr)  # 구간 합의 최솟값과 최댓값
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_divide(arr, m, mid):
            result = mid  # 가능한 경우의 최솟값 업데이트
            right = mid - 1  # 더 작은 값으로 확인
        else:
            left = mid + 1  # 더 큰 값으로 확인

    return result

# 입력 받기
n, m = map(int, input().split())
n_lst = list(map(int, input().split()))

# 결과 출력
print(min_max_partition_sum(n_lst, n, m))