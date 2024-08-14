N = int(input())

n_lst = [int(input()) for _ in range(N)]

max_length = 1  # 최대 길이 초기화
current_length = 1  # 현재 연속 길이 초기화

for i in range(1, N):
    # 이전 숫자와 현재 숫자의 부호가 같으면
    if (n_lst[i] > 0 and n_lst[i - 1] > 0) or (n_lst[i] < 0 and n_lst[i - 1] < 0):
        current_length += 1  # 연속 길이 증가
    else:
        # 부호가 다르면 현재 길이 초기화
        max_length = max(max_length, current_length)  # 최대 길이 갱신
        current_length = 1  # 현재 길이 초기화

# 마지막 연속 길이 체크
max_length = max(max_length, current_length)

print(max_length)