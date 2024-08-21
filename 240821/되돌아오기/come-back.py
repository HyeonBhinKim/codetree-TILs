N = int(input())

D = {
    "W" : 0,
    "S" : 0,
    "N" : 0,
    "E" : 0
}

ans = 0
prev_west_east = 0
prev_north_south = 0

for _ in range(N):
    d, t = map(str, input().split())
    t = int(t)
    D[d] += t
    ans += t
    # W와 E의 차이와 N과 S의 차이를 계산
    current_west_east = D["W"] - D["E"]
    current_north_south = D["N"] - D["S"]

    # 부호가 바뀌었는지 체크
    if ((prev_west_east > 0 and current_west_east < 0) or (prev_west_east < 0 and current_west_east > 0)) and current_north_south == 0:
        ans -= abs(current_west_east)
        print(ans)
        break

    if ((prev_north_south > 0 and current_north_south < 0) or (prev_north_south < 0 and current_north_south > 0)) and current_west_east == 0:
        ans -= abs(current_north_south)
        print(ans)
        break

    # 이전 값 업데이트
    prev_west_east = current_west_east
    prev_north_south = current_north_south

    # 두 묶음 모두 0인지 체크
    if current_west_east == 0 and current_north_south == 0:
        print(ans)
        break
    
    if _ == N-1:
        print(-1)