def even5(n):
    if n % 2:
        return "No"
    else:
        if (n//10 + n%10)%5:
            return "No"
        else:
            return "Yes"
        
print(even5(int(input())))