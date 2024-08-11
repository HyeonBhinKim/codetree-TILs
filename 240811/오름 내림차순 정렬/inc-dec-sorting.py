arr = [12, 41, 37, 81, 19, 25, 60, 20]
arr.sort()
arr.sort(reverse=True)
arr = sorted(arr)

arr.sort()
arr = arr[::-1] # reversed array
arr.sort()
arr = list(reversed(arr)) # reversed array

n = int(input())
n_lst = list(map(int, input().split()))
n_lst.sort()
print(*n_lst)
n_lst.sort(reverse=True)
print(*n_lst)