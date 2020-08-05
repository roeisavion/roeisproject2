grade=int(input("enter grade"))
max=grade
i=0
sum=0
while 0<=grade<=100 :
    i+=1
    sum=sum+grade
    if grade>max :
        max=grade
    grade = int(input("enter grade"))
print("max" ,max)
if i!=0 :
    print("average", sum/i )
print("max-average=", max-sum/i)