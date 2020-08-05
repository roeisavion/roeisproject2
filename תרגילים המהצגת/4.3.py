from random import randint
num1=randint(1,9)
a=int(input("guess your number"))
if a==num1 :
    print("correct!")
while num1!=a :
    if a>num1:
        print("the number is lower")
        a = int(input("guess your number"))
    elif a<num1 :
        print("the number is higher")
        a = int(input("guess your number"))
print("correct!")