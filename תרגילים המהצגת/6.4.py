from random import randint
x=[randint(1,100) for i in range(10)]
x=tuple(x)
y=x+tuple(input("enter a number you want to add"))
print(y)
print(x[:4]+x[-4:])