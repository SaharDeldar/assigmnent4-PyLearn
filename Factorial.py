import math
def Factorial(a):
    flag=0
    for i in range(a):
        if math.factorial(i)==a:
            x=1
            break
    if x==1:
        print('Yes')
    else:
        print('No')
        
number=int(input('enter a number:'))
Factorial(number)