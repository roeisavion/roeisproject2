a=int(input("enter a number"))
i=0
if a!=0 :
    while a!=0 :
        a=a//10
        i+=1

print("number of digits",i)
