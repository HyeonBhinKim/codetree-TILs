n = int(input())
n_lst = list(input().split())

ans_lst = sorted(n_lst)

cnt = 0
while n_lst != ans_lst:
    for i in range(1, n):
        if n_lst[i] < n_lst[i-1]:
            cnt += 1
            n_lst[i-1], n_lst[i] = n_lst[i], n_lst[i-1]
    
print(cnt)