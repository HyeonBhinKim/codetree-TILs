# function partition(arr[], low, high)
#   set pivot = select_pivot(arr, low, high)
#   set i = low - 1
  
#   for j = low ... j <= high - 1
#     if arr[j] < pivot
#       i += 1
#       swap (arr[i], arr[j])
      
#   swap (arr[i+1], arr[high])
#   return i + 1

# function quick_sort(arr[], low, high)
#     if low < high
#       pos = partition(arr, low, high)
    
#       quick_sort(arr, low, pos+1)
#       quick_sort(arr, pos-1, high)

n = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()

print(*n_lst)

# def partition(arr, low, high):
#   pivot =