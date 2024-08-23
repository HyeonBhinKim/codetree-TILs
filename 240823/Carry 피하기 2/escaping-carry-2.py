def carry(i, j, k):
    while (i+j+k):
        if i%10 + j%10 + k%10 > 9:
            return False
        i //= 10
        j //= 10
        k //= 10
    return True


n = int(input())

n_lst = list(int(input()) for _ in range(n))

ans = -1

for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if carry(n_lst[i], n_lst[j], n_lst[k]):
                ans = max(ans, n_lst[i]+n_lst[j]+n_lst[k])

print(ans)