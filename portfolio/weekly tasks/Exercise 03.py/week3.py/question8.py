num1=int(input('Enter a number: '))
if num1<0:
    #for negative numbers, print tables in reverse
    i=12
    for i in range(12, -1, -1):
        result = num1 * i
        print(num1, '*' ,i ,"=", result)
else:
    #for poitive numbers print normally.
    for i in range(13):
        result = num1 * i
        print(num1, '*' ,i ,"=", result)