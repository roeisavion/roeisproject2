from random import randint
x=[randint(0,10) for i in range(10)]
print(x)
for i in range(10):
    print(i,"is appearing",x.count(i),"times")
    