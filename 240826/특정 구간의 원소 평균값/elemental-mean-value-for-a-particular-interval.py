N = int(input())
n_lst = list(map(int, input().split()))

ans = 0

for i in range(N):
    for j in range(N):
        elem = 0
        elsum = 0
        for k in range(i, j+1):
            elsum += n_lst[k]
            elem += 1
        if elem != 0 and ((elsum/elem) in n_lst[i:j+1]):
            ans += 1
        
print(ans)