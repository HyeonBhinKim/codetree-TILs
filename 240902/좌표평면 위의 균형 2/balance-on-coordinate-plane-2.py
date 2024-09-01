N = int(input())

MAX_xy = 101

points = [tuple(map(int, input().split()))for _ in range(N)]

# sum_diff = 101
ans = 0
distance = 101
n_div = int(N/4)

for i in range(2, MAX_xy, 2): # x
    for j in range(2, MAX_xy, 2): # y
        fir_stage = 0
        sec_stage = 0
        thr_stage = 0
        fth_stage = 0

        for x, y in points:
            if x > i and y > j:
                fir_stage += 1
            elif x < i and y > j:
                sec_stage += 1
            elif x < i and y < j:
                thr_stage += 1
            elif x > i and y < j:
                fth_stage += 1
        
        tmp_abs = abs(max(fir_stage, sec_stage, thr_stage, fth_stage) - n_div)
        if tmp_abs < distance:
            distance = tmp_abs
            ans = max(fir_stage, sec_stage, thr_stage, fth_stage)

        # tmp_diff = max(fir_stage, sec_stage, thr_stage, fth_stage) - min(fir_stage, sec_stage, thr_stage, fth_stage)
        # if sum_diff > tmp_diff:
        #     sum_diff = tmp_diff
        #     ans = max(fir_stage, sec_stage, thr_stage, fth_stage)
            # print('fir_stage, sec_stage, thr_stage, fth_stage')
            # print(fir_stage, sec_stage, thr_stage, fth_stage)

print(ans)