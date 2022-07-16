def Multiplicationtable(n,m):
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(i*j,end=' ')
            if j==5:
                print()
    
number1=int(input('enter of Row:'))
number2=int(input('enter of column:'))

Multiplicationtable(number1,number2)