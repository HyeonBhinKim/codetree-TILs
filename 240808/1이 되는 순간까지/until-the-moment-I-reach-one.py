ans = 0

def onetime(n):
    if n == 1:
        return
    global ans
    ans += 1

    if n % 2:
        return onetime(n//3)
    else:
        return onetime(n//2)


N = int(input())
onetime(N)
print(ans)