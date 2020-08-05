a=int(input("enter the bigger number"))
b=int(input("enter the smaller number"))
x=0
y=0
for i in range (a):
   y += 1
   if y==b:
       x+=1
       y=0

print(x)
print(y)
