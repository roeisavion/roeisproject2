max_order=0
max=0
for i in range (5) :
    a = int(input("enter a number"))
    if a>max :
        max=a
        max_order=i
print(max_order+1)