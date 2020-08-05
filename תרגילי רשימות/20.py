from random import randint
a=int(input("how long do you want your list"))
x=[randint(0,10) for i in range(a)]
print(x)
b=int(input("for which number do u want to check index?"))
for i in range(a) :
    if b==x[i] :
        print(i)
        break
else:
    print("no",b,"founds" )
