MAX_N = 401
N, K = map(int, input().split())
n_lst = [0]*MAX_N

for _ in range(N):
    elem, loc = map(int, input().split())
    n_lst[loc] += elem  # 같은 위치에 여러 바구니가 가능하므로 += 사용

ans = 0

cumsum = [0] * MAX_N
for i in range(1, MAX_N):
    cumsum[i] = cumsum[i - 1] + n_lst[i]

# j의 범위를 K부터 MAX_N-K까지 설정
for j in range(K, MAX_N - K):
    # 구간 [j-K, j+K]의 합 계산
    total_candies = cumsum[j + K] - cumsum[j - K - 1]
    ans = max(ans, total_candies)

print(ans)