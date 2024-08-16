MAX_R = 1000001
MAX_T = 0
ans = 0
flg = 0
N, M = map(int, input().split())

n_lst = [0 for _ in range(MAX_R)]
m_lst = [0 for _ in range(MAX_R)]

for _ in range(N):
    v, t = map(int, input().split())
    if MAX_T == 0:
        for i in range(t):
            n_lst[i+1] = n_lst[i] + v
    else:
        for i in range(MAX_T, MAX_T+t):
            n_lst[i+1] = n_lst[i] + v
    MAX_T += t

MAX_T = 0

for _ in range(M):
    v, t = map(int, input().split())
    if MAX_T == 0:
        for i in range(t):
            m_lst[i+1] = m_lst[i] + v
    else:
        for i in range(MAX_T, MAX_T+t):
            m_lst[i+1] = m_lst[i] + v
    MAX_T += t


for i in range(MAX_T):
    if flg != 0 and (n_lst[i] - m_lst[i]) * flg < 0:
        flg *= -1
        ans += 1
    else:
        if n_lst[i] - m_lst[i] > 0:
            flg = 1
        elif n_lst[i] - m_lst[i] < 0:
            flg = -1

print(ans)