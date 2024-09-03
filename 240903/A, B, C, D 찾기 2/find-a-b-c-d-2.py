n_lst = list(map(int, input().split()))
n_lst.sort()

def is_equal_array(arr1, arr2):
    arr1.sort()
    arr2.sort()

    if len(arr1) != len(arr2):
        return False

    for x, y in zip(arr1, arr2):
        if x != y:
            return False

    return True

flag = False
for A in range(1, 41):
    if flag:
        break
    for B in range(1, 41):
        if flag:
            break
        for C in range(1, 41):
            if flag:
                break
            for D in range(1, 41):
                if is_equal_array([
                    A, B, C, D,
                    A + B, B + C, C + D, D + A, A + C, B + D,
                    A + B + C, A + B + D, A + C + D, B + C + D,
                    A + B + C + D
                    ], n_lst):
                    print(A, B, C, D)
                    flag = True
                    break