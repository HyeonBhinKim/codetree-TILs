N = int(input())
n_lst = [int(input()) for _ in range(N)]
mini = min(n_lst)
maxi = max(n_lst)


ans = 100000
for i in range(mini, maxi+1):
    cost = 0
    for elem in n_lst:
        if i <= elem and elem <= i + 17:
            continue
        elif elem < i:
            cost += (i - elem)**2
        else:
            cost += (elem - (i + 17))**2
    
    ans = min(ans, cost)

print(ans)