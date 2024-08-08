def absolute(arr):
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i] *= -1

N = int(input())
n_lst = list(map(int, input().split()))
absolute(n_lst)
print(*n_lst)