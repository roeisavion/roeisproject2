a=int(input("enter a number1"))
b=int(input("enter a number2"))
if a>b :
    for i in range (b + 1, a):
        if i % 2==0 :
            print(i)

elif b>a :
    for i in range (a + 1, b):
        if i%2==0 :
            print(i)

else: print("equal")
