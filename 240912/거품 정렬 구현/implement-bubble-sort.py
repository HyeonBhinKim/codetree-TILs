n = int(input())

n_lst = list(map(int, input().split()))

def bubble_sort():
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(n - 1):
            if n_lst[i] > n_lst[i + 1]:
                n_lst[i], n_lst[i + 1] = n_lst[i + 1], n_lst[i]
                is_sorted = False


bubble_sort()

print(*n_lst)