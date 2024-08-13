N = int(input())
n_lst = list(map(int,input().split()))
ans = [0]*N

for idx,i in enumerate(n_lst): 
    n_lst[idx] = [idx, i]

n_lst.sort(key=lambda x:(x[1],x[0]))

for j in range(N):
    ans[n_lst[j][0]] = j+1

print(*ans)