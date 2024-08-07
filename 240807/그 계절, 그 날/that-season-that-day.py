def isleapyear(Y):
    if (Y % 4) or ((Y%4 == 0 and Y%100 == 0) and (Y%400)):
        return 0
    return 1

def last_day_number(m, L):
    if m == 2 and L:
        return 29
    if m == 2:
        return 28
    if m == 4 or m == 6 or m == 9 or m == 11:
        return 30
    return 31

def isreal(y, m, d):
    if d <= last_day_number(m, isleapyear(y)):
        if m <= 2 or m == 12:
            return print("Winter")
        elif m <= 5:
            return print("Spring")
        elif m <= 8:
            return print("Summer")
        elif m <= 11:
            return print("Fall")

    return print("-1")

Y, M, D = map(int, input().split())

isreal(Y, M, D)