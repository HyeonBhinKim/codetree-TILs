def numbers(num):
    for i in range(num*num):
        print(i%9+1, end=' ')
        if (i+1) % num == 0:
            print()

n = int(input())
numbers(n)