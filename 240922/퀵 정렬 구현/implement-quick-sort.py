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

def partition(low, high):
    pivot = n_lst[high]                   # pivot을 고릅니다.
    i = low - 1                         # 파란색 화살표 위치를 정해줍니다.
                                        # 파란색 화살표는 pivot보다 같거나 큰 
                                        # 원소를 가리키고 있습니다.
    for j in range(low, high):          # 빨간색 화살표를 움직입니다.
        if n_lst[j] < pivot:              # 빨간색 화살표가 가리키는 원소가
            i += 1                      # pivot보다 작다면, 왼쪽으로 가야하므로
            n_lst[i], n_lst[j] = n_lst[j], n_lst[i]       # 두 원소의 위치를 바꿔줍니다.
    
    n_lst[i + 1], n_lst[high] = n_lst[high], n_lst[i + 1] # 최종적으로 pivot을
                                        
                                        # 경계에 있는 원소와 교환해줍니다.
                                        # 이때 경계는 마지막 파란색 화살표 위치에
                                        # 1을 더한 위치입니다.
    return i + 1                        # pivot의 최종 위치를 반환해줍니다.


def quick_sort(low, high):
    if low < high:                    # 원소의 개수가 2개 이상인 경우에만 진행
        pos = partition(low, high)    # pivot 기준으로 좌우로 분할 한 후
                                      # 해당 pivot의 위치를 pos에 넣어줍니다.
        quick_sort(low, pos - 1)      # pivot의 왼쪽 구간에 있는 원소들을 정렬합니다. 
        quick_sort(pos + 1, high)     # pivot의 오른쪽 구간에 있는 원소들을 정렬합니다.


quick_sort(0, n - 1)

print(*n_lst)