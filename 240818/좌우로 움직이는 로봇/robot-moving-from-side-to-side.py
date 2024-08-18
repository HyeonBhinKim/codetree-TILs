MAX_R = 2000001
n_location = 1000001
m_location = 1000001
n_time = 0
m_time = 0
ans = 0


n_lst = [0 for _ in range(MAX_R)]
m_lst = [0 for _ in range(MAX_R)]

n, m = map(int, input().split())

for i in range(n):
    t, d = map(str, input().split())
    t = int(t)
    if d == "L":
        for j in range(t):
            n_time += 1
            n_location -= 1
            n_lst[n_time] = n_location
    else:
        for j in range(t):
            n_time += 1
            n_location += 1
            n_lst[n_time] = n_location

for i in range(m):
    t, d = map(str, input().split())
    t = int(t)
    if d == "L":
        for j in range(t):
            m_time += 1
            m_location -= 1
            m_lst[m_time] = m_location
    else:
        for j in range(t):
            m_time += 1
            m_location += 1
            m_lst[m_time] = m_location



for i in range(1, max(n_time,m_time)+1):
    if min(n_time, m_time) <= i:
        if n_time < m_time:
            n_lst[i] = n_lst[n_time]
        else:
            m_lst[i] = m_lst[m_time]
            
    if n_lst[i-1] != m_lst[i-1] and n_lst[i] == m_lst[i]:
        ans += 1

print(ans)