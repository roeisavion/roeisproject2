x=input("enter numbers").split()
print(x)
for i in range (len(x)):
    x[i]=int(x[i])
print("max",max(x))
print("min",min(x))
print("average",sum(x)/len(x))
