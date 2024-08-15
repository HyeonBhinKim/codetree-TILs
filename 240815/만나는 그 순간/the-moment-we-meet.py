N, M = map(int, input().split())
MAX_T = 100001

n_lst = [0 for _ in range(MAX_T)]
m_lst = [0 for _ in range(MAX_T)]

n_flg = 0
m_flg = 0

for _ in range(N):
    d, t = map(str, input().split())
    t = int(t)
    for i in range(t):
        if d == 'L':
            n_lst[n_flg+1] = n_lst[n_flg] - 1
        else:
            n_lst[n_flg+1] = n_lst[n_flg] + 1
        n_flg += 1

for _ in range(M):
    d, t = map(str, input().split())
    t = int(t)
    for i in range(t):
        if d == 'L':
            m_lst[m_flg+1] = m_lst[m_flg] - 1
        else:
            m_lst[m_flg+1] = m_lst[m_flg] + 1
        m_flg += 1

maxflg = max(n_flg,m_flg)
for i in range(1, MAX_T):
    if n_lst[i] == m_lst[i]:
        print(i)
        break

    if i + 1 == maxflg:
        print(-1)
        break