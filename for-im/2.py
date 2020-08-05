x = [0,0,0,0,0,0]
sum = 0
count=0
for i in range(6) :
    x[i]=int(input("enter number"))
    if x[i]%2==0:
        sum=sum+x[i]
        count+=1

print("avrage" , sum/count)