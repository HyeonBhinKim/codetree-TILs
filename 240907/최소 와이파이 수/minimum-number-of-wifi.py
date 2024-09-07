n, m  = map(int, input().split())
n_lst = list(map(int, input().split()))

def min_wifi_installations(n, m, people):
    wifi_count = 0
    i = 0

    while i < n:
        # 현재 위치에서 가장 오른쪽에 설치할 수 있는 위치 찾기
        while i < n and people[i] == 0:
            i += 1
        
        if i >= n:  # 더 이상 사람을 찾을 수 없는 경우
            break
        
        # 와이파이를 설치할 위치를 결정 (사람이 있는 위치에서 m 거리만큼 오른쪽)
        wifi_count += 1
        wifi_position = i + m
        
        # 설치한 와이파이로 커버하는 최대한 오른쪽 위치 찾기
        while i < n and i <= wifi_position + m:
            i += 1

    return wifi_count


result = min_wifi_installations(n, m, n_lst)
print(result)