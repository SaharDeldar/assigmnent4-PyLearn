import math

def second_degree_equation(a,b,c):
    delta=b**2-4*a*c
    if delta < 0:
        print('The equation has no answer!!!')
    elif delta==0:
        x=(-b+math.sqrt(delta))/(2*a)
        print('The root of the equation is equal to ',x)
    else:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a)
        print('The roots of the equation is equal to ',x1,',',x2)

number1=int(input('enter number a:'))
number2=int(input('enter number b:'))
number3=int(input('enter number c:'))

second_degree_equation(number1,number2,number3)