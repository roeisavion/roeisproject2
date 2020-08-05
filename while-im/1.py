a=int(input("enter a number"))
while 99<a<1000 :
    print("sum digits =", (a % 10) + (a // 100) + (a // 10 % 10))
    a=int(input("enter a number"))

print("error")
