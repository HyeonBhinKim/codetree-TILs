N, C, G, H = map(int, input().split())
Ta, Tb = [0]*N, [0]*N

for i in range(N):
    Ta[i], Tb[i] = map(int, input().split())

def single_efficiency(Ta, Tb, t):
    if t<Ta:
        return C
    elif t<=Tb:
        return G
    else:
        return H

# 온도 t에 대한 작업량을 계산합니다.
def performance(t):
    total_efficiency = 0
    
    # 장비별 작업량의 합을 계산합니다.
    for i in range(N):
        total_efficiency += single_efficiency(Ta[i], Tb[i], t)
    return total_efficiency

    # 해설 전 코드
# n_lst = [tuple(map(int, input().split()))for _ in range(N)]

# 각 온도에 대해 작업량을 계산하여
# 그 중 최댓값을 구해줍니다.
max_work = 0
for t in range(1001):
    max_work = max(max_work, performance(t))

    # 해설 전 코드
# for i in range(1001):
#     tmp_work = 0
#     for j in n_lst:
#         Ta, Tb = j
#         if i < Ta:
#             tmp_work += C
#         elif i <= Tb:
#             tmp_work += G
#         else:
#             tmp_work += H
    
#     max_work = max(max_work, tmp_work)

print(max_work)