a, o, c = map(str, input().split())

if o in ('+-/*'):
    if o == '+':
        result = int(a)+int(c)
    elif o == '-':
        result = int(a)-int(c)
    elif o == '*':
        result = int(a)*int(c)
    elif o == '/':
        result = int(a)//int(c)
    print(a,o,c,"=",result)
else:
    print("False")