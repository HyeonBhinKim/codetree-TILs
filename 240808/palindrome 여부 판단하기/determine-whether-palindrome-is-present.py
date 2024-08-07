def ispalindrome(string):
    for i in range(len(string)):
        if string[i] != string[len(string)-1-i]: 
            return print("No")
    return print("Yes")

A = input()

ispalindrome(A)