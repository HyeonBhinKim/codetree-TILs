def isdifferent(string):
    tmp = ''
    for s in string:
        if tmp:
            if tmp != s:
                return True
        else:
            tmp = s
    return False


A = input()

if isdifferent(A):
    print("Yes")
else:
    print("No")