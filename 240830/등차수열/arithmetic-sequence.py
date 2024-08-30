n = int(input())
n_lst = list(map(int, input().split()))

cnt = 0

for i in range(n):
    for j in range(i+1, n):
        if n_lst[i] < n_lst[j]:
            for k in range(n_lst[i]+1,n_lst[j]):
                if n_lst[j]-k == k-n_lst[i]:
                    cnt += 1
        else:
            for k in range(n_lst[i]-1, n_lst[j], -1):
                if n_lst[i]-k == k-n_lst[j]:
                    cnt += 1

print(cnt)