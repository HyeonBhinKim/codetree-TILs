def max_distance_after_adding_one_seat(N, chairs):
    occupied_positions = [i for i in range(N) if chairs[i] == '1']
    
    def get_min_distance(positions):
        if len(positions) < 2:
            return float('inf')
        min_dist = float('inf')
        for i in range(1, len(positions)):
            min_dist = min(min_dist, positions[i] - positions[i - 1])
        return min_dist
    
    max_min_distance = 0
    
    # 모든 빈 좌석에 대해 새로운 사람을 추가해봅니다.
    for i in range(N):
        if chairs[i] == '0':
            new_positions = occupied_positions + [i]
            new_positions.sort()
            min_distance = get_min_distance(new_positions)
            max_min_distance = max(max_min_distance, min_distance)
    
    return max_min_distance

# 입력 받기
N = int(input())
chairs = input().strip()

# 결과 출력
print(max_distance_after_adding_one_seat(N, chairs))