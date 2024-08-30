n = int(input())
n_lst = list(map(int, input().split()))

ans = 101

for i in range(n):
    n_lst[i] *= 2

    for j in range(n):
        arr = []
        for k in range(n):
            if j == k:
                continue
            arr.append(n_lst[k])

        sum_dif = 0
        for l in range(n-2):
            sum_dif += abs(arr[l]-arr[l+1])
        
        ans = min(ans, sum_dif)
    
    n_lst[i] //= 2

print(ans)