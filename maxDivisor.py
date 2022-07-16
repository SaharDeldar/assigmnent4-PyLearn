def Divisor(x):
    List = []
    for i in range(1,x+1):
        if x % i == 0:
            List.append(i)
    return List

def maxdivided(x,y):
    divided = []
    for i in Divisor(x):
        for j in Divisor(y):
            if i == j:
                divided.append(i)
    print("Greatest divisor :" , max(divided))

number1 = int(input("enter number1:"))
number2 = int(input("enter number2:"))
maxdivided(number1,number2)