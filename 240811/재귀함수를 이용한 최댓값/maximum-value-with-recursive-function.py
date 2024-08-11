def maxvalue(n, arr, m):
    if n == 1:
        return max(arr[n-1], m)
    
    m = arr[n-1]
    return max(maxvalue(n-1, arr, m), m)


N = int(input())
n_lst = list(map(int, input().split()))
print(maxvalue(N, n_lst, 0))