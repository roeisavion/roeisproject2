x=[i for i in range(1,11)]
print(x)
x_3=x[-3:]
print(x_3)
print(x[::-1])
print(x[1::2])
x[4:6]=input("enter 3 numbers").split()
y=x
x[x.index(4):x.index(5)+1]=input("enter 3 numbers").split()
# print(x)
y=[i*2 for i in range(1,11)]
print(y)
# z=[x[0], x[-1]]

z=[x[0]] + [x[-1]]
print(z)


