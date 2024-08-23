R, C = map(int, input().split())

arr = [
    list(map(str, input().split()))
    for _ in range(R)
]

cnt = 0

# 완전 탐색
for i in range(1, R):
    for j in range(1, C):
        for k in range(i+1, R-1):
            for l in range(j+1, C-1):
                # 그 중 색깔이 전부 달라지는 경우에만 개수를 세줍니다.
                if (arr[0][0] != arr[i][j] and
                   arr[i][j] != arr[k][l] and
                   arr[k][l] != arr[R-1][C-1]):
                    cnt += 1

print(cnt)