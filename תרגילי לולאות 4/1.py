a=int(input("enter a number"))
min=a
while a!=0:
    if a>0 and a<min:
        min=a
    a = int(input("enter a number"))
print(min)
