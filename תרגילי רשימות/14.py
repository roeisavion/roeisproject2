a=int(input("enter a number"))
x=[]
for i in range(1,a):
    if a%i==0:
        x.append(i)
print(x)
