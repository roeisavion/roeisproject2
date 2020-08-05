def big(a,b):
    if a>b:
        return a
    return b
def small(a,b) :
    if b>a:
        return a
    return b

def between(x,y):
    for i in range(x,y+1) :
        print(i,end=' ')
a=int(input("enter a"))
b=int(input("enter b"))
between(small(a,b),big(a,b))




