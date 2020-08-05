from random import randint
a=50
i=1
max=100
min=1
print(a,"is this your number?")
answer=input("higher\lower\correct")
while answer!="correct" :
    if answer=="higher" :
        min=a
        a = (min+max)//2
        print(a, "is this your number?")
        answer = input("higher\lower\correct")
        i += 1
    elif answer=="lower":
        max=a
        a = (min+max)//2
        print(a, "is this your number?")
        answer = input("higher\lower\correct")
        i+=1


print(i,"tries")