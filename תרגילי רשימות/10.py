x=[i for i in range(1,11)]
print(x)
y=[]

for i in range(10):
    if x[i]%3==0:
        y.append(i)

while len(y)>0 :
    z=y.pop()
    del (x[z])
print(x)