N = int(input())
n_lst = list(map(int, input()))

def dist():
    tmp = 1000
    for i in range(N): # 기준
        if not n_lst[i]: # 1이 아닌곳은 넘어감
            continue
        for j in range(N):
            if i == j: # 같은곳은 넘어감
                continue
            if n_lst[j]: # 사람이 있으면 조건문 실행
                tmp = min(tmp, abs(i-j))
    
    return tmp


ans = 0
for i in range(1,N-1):
    if n_lst[i] != 1:
        n_lst[i] = 1
        ans = max(ans, dist())
        n_lst[i] = 0

print(ans)