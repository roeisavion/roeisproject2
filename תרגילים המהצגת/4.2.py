a=int(input("enter a number1"))
for i in range (2,a) :
    if i!=a and a%i==0 :
        print("the number is non-prime")
        break
else:
    print("the number is prime")
