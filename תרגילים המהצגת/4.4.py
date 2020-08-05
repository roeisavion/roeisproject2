from random import randint
a=randint(1,100)
i=1
max=100
min=1
print(a,"is this your number?")
answer=input("higher\lower\correct")
while answer!="correct" :
    if answer=="higher" :
        min=a+1
        a = randint(min,max)
        print(a, "is this your number?")
        answer = input("higher\lower\correct")
        i += 1
    elif answer=="lower":
        max=a-1
        a=randint(min,max)
        print(a, "is this your number?")
        answer = input("higher\lower\correct")
        i+=1


print(i,"tries")
