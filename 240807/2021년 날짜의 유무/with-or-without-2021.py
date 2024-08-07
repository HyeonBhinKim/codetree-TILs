M, D = map(int, input().split())

if M == 2:
    if D <= 28:
        print("Yes")
    else:
        print("No")
elif M <= 7:
    if M % 2:
        if D <= 31:
            print("Yes")
        else:
            print("No")
    else:
        if D <= 30:
            print("Yes")
        else:
            print("No")
elif M <= 12:
    if M % 2:
        if D <= 30:
            print("Yes")
        else:
            print("No")
    else:
        if D <= 31:
            print("Yes")
        else:
            print("No")
else:
    print("No")