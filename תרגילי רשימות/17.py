x=(input("enter numbers"))
a=x.split()
y=(input("enter numbers"))
b=y.split()
print(a, b)
for i in range(len(a)):
    if a[i] in b:
        print("there is at least 1 common number")
        break
else:
    print("no common numbers")

