
i=0
sum=0
grade = int(input("enter grade"))
while 1 :
    while 0<=grade<=100:
        if grade>=60 :
            sum=sum+grade
            i+=1
        print("avrage",sum/i)
        grade = int(input("enter grade"))
    else:
        print("invalid grade")
        grade = int(input("enter grade"))
