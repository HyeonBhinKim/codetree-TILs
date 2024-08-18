N, M = map(int, input().split())
MAX_R = 1000001

n_lst = [0] * MAX_R
m_lst = [0] * MAX_R

time = 0

for _ in range(N):
    v, t = map(int, input().split())
    for i in range(t):
        time += 1
        n_lst[time] = n_lst[time-1] + v

time = 0

for _ in range(M):
    v, t = map(int, input().split())
    for i in range(t):
        time += 1
        m_lst[time] = m_lst[time-1] + v    

ans = 0
tmp = [0, 0]

for t in range(1, time+1):
    if n_lst[t] > m_lst[t]:
        if tmp[0] == 1 and tmp[1] == 0:
            pass
        else:
            tmp[0], tmp[1] = 1, 0
            ans += 1

    elif n_lst[t] < m_lst[t]:
        if tmp[0] == 0 and tmp[1] == 1:
            pass
        else:
            tmp[0], tmp[1] = 0, 1
            ans += 1

    else:
        if tmp[0] == 1 and tmp[1] == 1:
            pass
        else:
            tmp[0], tmp[1] = 1, 1
            ans += 1

print(ans)