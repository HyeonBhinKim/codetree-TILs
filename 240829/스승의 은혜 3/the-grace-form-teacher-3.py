N, B = map(int, input().split())

n_lst = []

for _ in range(N):
    p, s = map(int, input().split())
    total_cost = p + s
    n_lst.append([total_cost, p, s])

ans = 0

for i in range(N):
    # 쿠폰을 i번째 학생의 선물에 적용
    coupon_price = n_lst[i][1] // 2
    coupon_total_cost = coupon_price + n_lst[i][2]
    
    # 나머지 학생들의 선물 가격을 포함
    costs = []
    for j in range(N):
        if j == i:
            costs.append(coupon_total_cost)  # 쿠폰 사용한 학생
        else:
            costs.append(n_lst[j][0])  # 쿠폰 사용하지 않은 학생

    # 비용 정렬
    costs.sort()

    budget = 0
    count = 0

    for cost in costs:
        if budget + cost > B:
            break
        budget += cost
        count += 1

    ans = max(ans, count)

print(ans)