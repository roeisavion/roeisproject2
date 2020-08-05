a=int(input("enter a number"))
i=0
while a!=0:
    if a%7==0 or a%3==0 :
        i+=1
    a=int(input("enter a number"))
print(i)