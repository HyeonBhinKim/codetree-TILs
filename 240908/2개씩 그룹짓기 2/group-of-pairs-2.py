def max_min_difference(n, numbers):
    # 2n개의 숫자를 정렬
    numbers.sort()
    
    # 각 그룹의 차이 계산
    min_differences = []
    
    for i in range(n):
        pair_difference = numbers[2 * i + 1] - numbers[2 * i]
        min_differences.append(pair_difference)
    
    # 그룹 내의 차이의 최솟값 중 최대값을 return
    return min(min_differences)

# 입력 처리
n = int(input())
numbers = list(map(int, input().split()))

# 함수 호출 및 결과 출력
result = max_min_difference(n, numbers)
print(result)