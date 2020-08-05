def hezka (a,b):
    x=1
    for i in range(1,b+1):
        x=x*a
    return x
a=int(input("enter a"))
b=int(input("enter b"))
print(hezka(a,b))
