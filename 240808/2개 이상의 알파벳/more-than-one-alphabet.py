def isdifferent(string):
    diction = {}
    for s in string:
        if s in diction:
            diction[s] += 1
        else:
            diction[s] = 1
    return diction


A = input()

dt = isdifferent(A)

if any(count >= 2 for count in dt.values()):
    print("Yes")
else:
    print("No")