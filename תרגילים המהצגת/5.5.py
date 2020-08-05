x=input("enter grades with passes beetwin").split()
passed=0
failed=0
for i in range(len(x)):
        x[i]=int(x[i])
        if 60<=x[i]<=100 :
            passed+=1
        else:
            failed+=1

print("passed",passed)
print("failed",failed)

