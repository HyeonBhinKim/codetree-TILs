T, a, b = map(int, input().split())

# S와 N의 위치를 저장할 리스트
s_positions = []
n_positions = []

for _ in range(T):
    alpha, loc = input().split()
    loc = int(loc)
    if alpha == 'S':
        s_positions.append(loc)
    else:
        n_positions.append(loc)

cnt = 0

for i in range(a, b + 1):
    # S와 N의 가장 가까운 거리 초기화
    nears = min(abs(i - pos) for pos in s_positions)
    nearn = min(abs(i - pos) for pos in n_positions)
    
    # 조건 확인
    if nears <= nearn:
        cnt += 1

print(cnt)