N = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
ans = 0

for i in range(len(n_lst)//N):
    tmp = n_lst[i] + n_lst[-1-i]
    ans = max(tmp, ans)

print(ans)