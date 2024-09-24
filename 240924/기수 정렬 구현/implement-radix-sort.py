# function radix_sort(arr, k)
#   for pos = k - 1 ... pos >= 0:
#     set arr_new = [10][]
#     for i = 0 ... i < arr.size
#       set digit = posth digit of arr[i]
#       arr_new[digit].append(arr[i])

#     set store_arr = []
#     for i = 0 ... i < 10
#       for j = 0 ... j < arr_new[i].size
#         store_arr.append(arr_new[i][j])
  
#     arr = store_arr

#   return arr

MAX_K = 6
MAX_DIGIT = 10

# 변수 선언 및 입력
n = int(input())
arr = list(map(int, input().split()))


def radix_sort():
    global arr

    p = 1
    for pos in range(MAX_K):
        arr_new = [[] for _ in range(MAX_DIGIT)]
        for elem in arr:
            digit = (elem // p) % 10
            arr_new[digit].append(elem)

        arr = []
        for digit in range(MAX_DIGIT):
            for elem in arr_new[digit]:
                arr.append(elem)
        
        p *= 10


radix_sort()

for elem in arr:
    print(elem, end=" ")