n = int(input())
n_lst = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(n_lst[i]+1,n_lst[j]):
            if n_lst[j]-k == k-n_lst[i]:
                cnt += 1

print(cnt)