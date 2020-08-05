from random import randint
x=[randint(1,20) for i in range(20)]
y=[]
a=int(input("enter a number you want to delete"))
print("original",x)
for i in range(20):
    if x[i]!=a :
        y.append(x[i])
print("new     ", y)

