def iseven(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i] = arr[i]//2

N = int(input())
n_lst = list(map(int, input().split()))

iseven(n_lst)

for i in n_lst:
    print(i, end=" ")