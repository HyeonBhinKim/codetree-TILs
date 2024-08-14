N = int(input())

# 숫자를 입력받기 위한 리스트
numbers = []

for _ in range(N):
    target = int(input())
    numbers.append(target)

max_count = 1  # 연속된 최대 횟수
current_count = 1  # 현재 연속된 횟수

for i in range(1, N):
    if numbers[i] == numbers[i - 1]:
        current_count += 1  # 현재 숫자와 이전 숫자가 같으면 카운트 증가
    else:
        # 연속이 끊기면 최대값 갱신
        if current_count > max_count:
            max_count = current_count
        current_count = 1  # 카운트 초기화

# 루프가 끝난 후 마지막 연속 카운트 체크
if current_count > max_count:
    max_count = current_count

print(max_count)