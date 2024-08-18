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
leader = 0

for t in range(1, time+1):
    if n_lst[t] > m_lst[t]:
        if leader != 1:
            ans += 1
        leader = 1

    elif n_lst[t] < m_lst[t]:
        if leader != 2:
            ans += 1
        leader = 2

    else:
        if leader != 3:
            ans += 1
        leader = 3

print(ans)