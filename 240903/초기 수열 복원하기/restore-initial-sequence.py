N = int(input())
n_lst = [i for i in range(1, N+1)]
arr = list(map(int, input().split()))

ni = 0
mi = 0
for idx in ranage(N-1):
    for i in n_lst:
        for j in n_lst:
            if i == j or ni != i or mi != j:
                continue
            if arr[idx] == i+j:
                ni = i
                mi = j