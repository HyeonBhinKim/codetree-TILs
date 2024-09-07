N = int(input())
n_lst = list(map(int, input().split()))
sort_lst = sorted(n_lst)
cnt = 0

# 현재 리스트가 정렬된 리스트와 다를 때까지 반복
while sort_lst != n_lst:
    # 가장 작은 값의 위치 찾기
    for i in range(1, len(n_lst)):
        if n_lst[0] > n_lst[i]:
            # n_lst의 첫 번째 요소와 현재 인덱스의 요소를 교환
            n_lst[0], n_lst[i] = n_lst[i], n_lst[0]
            cnt += 1
            break
    else:
        # 첫 번째 요소가 가장 작을 경우
        if n_lst and sort_lst and n_lst[0] == sort_lst[0]:
            n_lst = n_lst[1:]  # 첫 번째 요소를 제거
            sort_lst = sort_lst[1:]  # 정렬된 리스트의 첫 번째 요소도 제거
            cnt += 1

print(cnt)