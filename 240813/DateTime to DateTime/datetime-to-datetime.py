def DateTime(a,b,c):
    total = 0
    if a >= 11:
        if a == 11 and b < 11:
            return -1
        if a == 11 and b == 11 and c < 11:
            return -1
        total += 24*60*(a-11) + 60*(b-11) + (c-11)

        return total
    else:
        return -1


a, b, c = map(int, input().split())

print(DateTime(a,b,c))