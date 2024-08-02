def leafyear(n):
    if n % 4:
        return "false"
    if n % 100 == 0 and n % 400:
        return "false"
    return "true"

y = int(input())

print(leafyear(y))