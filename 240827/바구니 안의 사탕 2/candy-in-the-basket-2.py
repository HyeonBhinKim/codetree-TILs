MAX_N = 401
N, K = map(int, input().split())
n_lst = [0]*MAX_N

for i in range(N):
    elem, loc = map(int,input().split())
    n_lst[loc] = elem

ans = 0

for j in range(1, MAX_N-2*K):
    ans = max(ans, sum(n_lst[j:j+2*K+1]))

print(ans)