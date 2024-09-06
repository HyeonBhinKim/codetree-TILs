arr = [list(input())for _ in range(10)]

L = [0,0]
R = [0,0]
B = [0,0]

for i in range(10):
    for j in range(10):
        if arr[i][j] == 'L':
            L = [i, j]
        elif arr[i][j] == 'R':
            R = [i, j]
        elif arr[i][j] == 'B':
            B = [i, j]


if L[0] == R[0] == B[0] or L[1] == R[1] == B[1]:
    print(abs(L[0]-B[0])+abs(L[1]-B[1])+1)
else:
    print(abs(L[0]-B[0])+abs(L[1]-B[1])-1)