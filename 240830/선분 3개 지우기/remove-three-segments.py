MAX_A = 100

# 변수 선언 및 입력
n = int(input())
section = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
    
# 3개의 선분을 모두 골라보면서
# 모두 겹쳐지지 않도록 하는 가짓수를 구합니다.
ans = 0
for i in range(n):
	for j in range(i + 1, n):
		for k in range(j + 1, n):
            # i, j, k번 선분을 제외했을 때
            # 모든 선분이 겹치지 않으면 정답을 1 추가합니다.
			
			# overlap : 모든 선분이 겹치지 않으면 false
			overlap = False
			arr = [0] * (MAX_A + 1)
			
			for x in range(n):
				# 제외한 3개의 선분이면 넘어갑니다.
				if x == i or x == j or x == k:
					continue
				
				for y in range(section[x][0], section[x][1] + 1):
					arr[y] += 1
				
			for x in range(MAX_A + 1):
				if arr[x] > 1:
					overlap = True
				
			if overlap == False:
				ans += 1

print(ans)