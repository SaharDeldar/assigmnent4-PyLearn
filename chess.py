def chess():
    u1=int(input("r1"))
    u2=int(input("r2")) 
    for i in range(u1): 
        if i %2==0:
            for j in range(u2):
                if j %2==0:
                    print("#",end="")
                else:
                     print("*",end="")   
        print("\n")   
    else:
        for j in range(u2) :
            if j %2==0:
                    print("#",end="")
            else:
                     print("*",end="") 
     
        print("\n") 
chess()                                 