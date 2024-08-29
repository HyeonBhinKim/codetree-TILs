N = int(input())

n_lst = [tuple(map(int, input().split())) for _ in range(N)]

max_tri = 0

for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if n_lst[i][1] == n_lst[j][1]:  # i, j 의 y좌표가 같으면 i,j 차이가 밑변
                if n_lst[i][0] == n_lst[k][0]:  # i, k 의 x좌표가 같으면 k,i 차이가 높이
                    tri = abs((n_lst[i][0] - n_lst[j][0]) * (n_lst[i][1] - n_lst[k][1]))
                    max_tri = max(max_tri, tri)
                elif n_lst[j][0] == n_lst[k][0]:  # j,k x좌표
                    tri = abs((n_lst[i][0] - n_lst[j][0]) * (n_lst[j][1] - n_lst[k][1]))
                    max_tri = max(max_tri, tri)
            elif n_lst[k][1] == n_lst[j][1]:  # k, j 의 y좌표가 같으면 k,j 차이가 밑변
                if n_lst[i][0] == n_lst[k][0]:  # i, k 의 x좌표가 같으면 k,i 차이가 높이
                    tri = abs((n_lst[k][0] - n_lst[j][0]) * (n_lst[i][1] - n_lst[k][1]))
                    max_tri = max(max_tri, tri)
                elif n_lst[j][0] == n_lst[i][0]:  # j,i x좌표
                    tri = abs((n_lst[k][0] - n_lst[j][0]) * (n_lst[j][1] - n_lst[i][1]))
                    max_tri = max(max_tri, tri)
            elif n_lst[i][1] == n_lst[k][1]:  # i, k 의 y좌표가 같으면 i,k 차이가 밑변
                if n_lst[i][0] == n_lst[k][0]:  # i, j 의 x좌표가 같으면 k,i 차이가 높이
                    tri = abs((n_lst[i][0] - n_lst[k][0]) * (n_lst[i][1] - n_lst[j][1]))
                    max_tri = max(max_tri, tri)
                elif n_lst[j][0] == n_lst[k][0]:  # j,k x좌표
                    tri = abs((n_lst[i][0] - n_lst[k][0]) * (n_lst[j][1] - n_lst[k][1]))
                    max_tri = max(max_tri, tri)

print(max_tri)