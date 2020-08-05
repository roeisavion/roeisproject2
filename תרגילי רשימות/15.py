x=[1,1]
y=int(input("how long do you want your fibonachi?"))
for i in range (y):
    x.append(x[i]+x[i+1])
print(x)