a=int(input("enter a number"))
opposit=0
while a//10!=0 :
    opposit=(opposit+a%10)*10
    a=a//10
opposit=(opposit+a%10)
print(opposit)
print(opposit*2)
