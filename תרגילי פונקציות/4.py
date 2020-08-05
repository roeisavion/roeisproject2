def factorial (a):
    sums=0
    for i in range(1,a+1) :
        sums+=i
    return (sums)
a=int(input("enter a"))
print(factorial(a))
