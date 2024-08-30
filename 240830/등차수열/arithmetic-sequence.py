n = int(input())
n_lst = list(map(int, input().split()))

max_count = 0

# 모든 쌍 (ai, aj)를 선택합니다.
for i in range(n):
    for j in range(i + 1, n):
        ai = n_lst[i]
        aj = n_lst[j]

        # k를 계산합니다.
        k = (ai + aj) // 2  # k는 ai와 aj의 중간값이 될 수 있습니다.

        # k가 ai와 aj 사이에 있는지 확인합니다.
        if ai < k < aj or aj < k < ai:
            count = 1  # 이 쌍에 대해 하나의 등차수열이 존재합니다.

            # k값을 바꿔가며 추가적인 등차수열을 찾습니다.
            count += (ai + aj) % 2  # 중간값이 정수가 아닐 경우 추가로 k를 조정할 수 있습니다.

            max_count = max(max_count, count)

print(max_count)